require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.debug = true
  config.logger.level = ::Logger::DEBUG
  config.metrics.enabled = true
  config.metrics.enable_code_locations = true
  config.enable_tracing = true
  config.release = "testing-metrics"
end

class Foo
  def foo
    bar
  end

  def bar
    baz
  end

  def baz
    record_metric
  end

  def record_metric
    Sentry::Metrics.increment('foo')
  end
end

Foo.new.foo

sleep 10
