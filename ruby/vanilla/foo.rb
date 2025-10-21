require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.sdk_logger.level = :debug
end

def recurse(n=0)
  recurse(n+1)
end

def caller
  recurse
end

begin
  caller
rescue Exception => e
  Sentry.capture_exception(e)
end

sleep(2)
