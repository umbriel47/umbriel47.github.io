source "https://rubygems.org"

gem "jekyll", "~> 4.3"

# The site ships plain CSS, so no Sass is actually compiled. Pinned to the 2.x
# converter because 3.x pulls sass-embedded, whose prebuilt protobuf binaries
# do not resolve on every host architecture.
gem "jekyll-sass-converter", "~> 2.0"

group :jekyll_plugins do
  gem "jekyll-feed",    "~> 0.17"
  gem "jekyll-sitemap", "~> 1.4"
  gem "jekyll-seo-tag",      "~> 2.8"
  gem "jekyll-redirect-from", "~> 0.16"
end

# Windows / JRuby lack zoneinfo files.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
gem "webrick", "~> 1.8"

# ffi >= 1.17 requires Ruby >= 3.0; pinned so the site can also be built with an
# older system Ruby locally. CI uses Ruby 3.3 and is unaffected.
gem "ffi", "< 1.17"
