#!/usr/bin/env ruby
# Publish gate for case studies. Ruby stdlib only (YAML), so it runs on any Mac
# and in GitHub Actions without a Gemfile.
#
#   ruby scripts/check_cases.rb            # report problems, exit 1 if any
#   ruby scripts/check_cases.rb --allow-placeholders   # scaffold mode: skip P3-copy checks
#
# Enforces: required fields, 3–5 screenshots with alt text for every case,
# caveat when beta / early alpha / paid key, repo links only when audited,
# strand ids that exist, no unfinished "[P3" copy at publish time.
require "yaml"
require "date"

ROOT = File.expand_path("..", __dir__)
# Strict (publish) mode once _config.yml has `launched: true`, or with --strict.
# Before launch, P3-copy checks are skipped so scaffold pushes stay green;
# structural rules (link modes, alt text, audited repo links, strand ids) always run.
launched = (YAML.safe_load(File.read(File.join(ROOT, "_config.yml"), encoding: "UTF-8")) || {})["launched"] == true
allow_placeholders = ARGV.include?("--allow-placeholders") || (!launched && !ARGV.include?("--strict"))
puts "check_cases: #{allow_placeholders ? 'pre-launch mode (placeholder copy allowed)' : 'publish mode'}"

strand_ids = YAML.safe_load(File.read(File.join(ROOT, "_data/strands.yml"), encoding: "UTF-8")).map { |s| s["id"] }
required = %w[title summary status link_mode]
# audience, tools, division_of_labor and dates may stay empty: the layout hides
# empty rows, and docs/pending_inputs.md (Project) tracks what is still owed.
statuses = ["live", "in use", "beta", "prototype", "early alpha", "partial"]
modes = %w[live walkthrough excerpt]

problems = []
Dir[File.join(ROOT, "_case_studies/*.md")].sort.each do |path|
  name = File.basename(path)
  next if name.start_with?("_")
  text = File.read(path, encoding: "UTF-8")
  fm = text[/\A---\s*\n(.*?)\n---\s*\n/m, 1]
  if fm.nil?
    problems << "#{name}: no front matter"
    next
  end
  d = YAML.safe_load(fm, permitted_classes: [Date]) || {}
  body = text.sub(/\A---.*?\n---\s*\n/m, "")
  err = ->(m) { problems << "#{name}: #{m}" }

  unless allow_placeholders
    required.each do |k|
      v = d[k]
      err.("missing #{k}") if v.nil? || (v.respond_to?(:empty?) && v.empty?)
    end
    err.("placeholder: true is still set") if d["placeholder"]
    err.("unfinished [P3] copy in body") if body.include?("[P3")
    err.("[needs you] marker still in case") if text.include?("[needs you")
  end

  err.("status '#{d['status']}' not one of #{statuses.join(', ')}") if d["status"].to_s != "" && !statuses.include?(d["status"])
  err.("link_mode '#{d['link_mode']}' not one of #{modes.join(', ')}") unless modes.include?(d["link_mode"])

  shots = Array(d["screenshots"]).select { |s| s.is_a?(Hash) && s["src"].to_s != "" }
  unless allow_placeholders
    err.("needs 3 to 5 screenshots, has #{shots.size}") unless (3..5).cover?(shots.size)
  end
  shots.each_with_index do |s, i|
    err.("screenshot #{i + 1} has no alt text") if s["alt"].to_s.strip.empty?
    local = File.join(ROOT, s["src"].sub(%r{\A/}, ""))
    err.("screenshot #{i + 1} file not found: #{s['src']}") if s["src"].start_with?("/") && !File.exist?(local)
  end

  needs_caveat = ["beta", "early alpha"].include?(d["status"]) || d["paid_key"]
  err.("caveat required (beta, early alpha, or paid key)") if needs_caveat && d["caveat"].to_s.strip.empty? && !allow_placeholders

  links = d["links"] || {}
  if links["repo"].to_s != "" && !links["repo_public_audited"]
    err.("repo link set but repo_public_audited is false (Invariant 7)")
  end
  err.("link_mode is live but links.live is empty") if d["link_mode"] == "live" && links["live"].to_s == "" && !allow_placeholders

  Array(d["aied_strands"]).each { |id| err.("unknown strand id '#{id}'") unless strand_ids.include?(id) }
end

unless allow_placeholders
  site_files = Dir[File.join(ROOT, "{index.html,work.html,approach.html,about.md,_includes/*.html,_data/*.yml}")]
  site_files.each do |f|
    s = File.read(f, encoding: "UTF-8")
    problems << "#{f.sub(ROOT + '/', '')}: unfinished copy marker" if s.include?("[needs you") || s.include?("[P3")
  end
end

if problems.empty?
  puts "check_cases: OK"
else
  puts problems.map { |p| "check_cases: #{p}" }
  exit 1
end
