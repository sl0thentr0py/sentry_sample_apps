require 'sentry-ruby'
require 'pry'

Sentry.init do |config|
  config.debug = true
end

Sentry.capture_message("testing default TLS")
