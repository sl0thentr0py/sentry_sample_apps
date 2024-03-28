require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.debug = true
  config.logger.level = ::Logger::DEBUG
end

begin
  1/0
rescue => e
  Sentry.capture_exception(e)
end

sleep 2
