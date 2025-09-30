require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.sdk_logger.level = :debug
  config.metrics.enabled = true
end

Sentry::Metrics.increment('foo')
