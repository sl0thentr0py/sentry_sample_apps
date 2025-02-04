require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.metrics.enabled = true
  config.metrics.bla = 42
end

Sentry::Metrics.incr(42)
Sentry::Metrics.foobar('foo', unit: 'asdas')
