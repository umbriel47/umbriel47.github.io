#!/usr/bin/env ruby
# Fails the build if any internal href/src in _site points at a path that was
# not generated. Catches broken language switches, chapter links and typos in
# data files before they reach production.
require "set"

SITE = File.expand_path("../_site", __dir__)
abort "no _site/ — run `jekyll build` first" unless Dir.exist?(SITE)

existing = Set.new
Dir.glob("#{SITE}/**/*", File::FNM_DOTMATCH).each do |p|
  next if File.directory?(p)
  rel = p.sub(SITE, "")
  existing << rel
  existing << File.dirname(rel) + "/" if File.basename(rel) == "index.html"
end

broken = []
Dir.glob("#{SITE}/**/*.html").each do |file|
  html = File.read(file)
  page = file.sub(SITE, "")
  html.scan(/(?:href|src)="([^"]+)"/) do |(raw)|
    url = raw.split("#").first.to_s.split("?").first.to_s
    next if url.empty?
    next if url.start_with?("http://", "https://", "mailto:", "data:", "//", "tel:")
    next unless url.start_with?("/")
    target = begin
      require "uri"
      URI::DEFAULT_PARSER.unescape(url)
    rescue StandardError
      url
    end
    next if existing.include?(target)
    next if target.end_with?("/") && existing.include?("#{target}index.html")
    next if existing.include?("#{target}/") || existing.include?("#{target}/index.html")
    broken << [page, raw]
  end
end

if broken.empty?
  puts "link check: OK (#{Dir.glob("#{SITE}/**/*.html").size} pages)"
else
  broken.uniq.each { |page, url| warn "BROKEN #{url}  (in #{page})" }
  abort "link check: #{broken.uniq.size} broken internal link(s)"
end
