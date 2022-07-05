require 'sentry-ruby'
# require 'pry'
# require 'pry-nav'

Sentry.init do |config|
  config.debug = true
end

begin
  1 / 0
rescue => e
  Sentry.capture_exception(e)
end
