require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.debug = true
  config.logger.level = ::Logger::DEBUG
  config.enable_metrics = true
  config.release = "testing-metrics"
end

3.times { Sentry::Metrics.incr('foo') }
3.times { Sentry::Metrics.incr('bar') }

sleep 2

10.times { Sentry::Metrics.distribution('dist', Random.rand, 'millisecond', tags: { unicode: 'snöwmän', fortytwo: 42 }) }
100.times { Sentry::Metrics.gauge('gauge', Random.rand, 'ratio', tags: { 'normal' => 'cow', 'normalize snöwmän' => 'potato' }) }
50.times { Sentry::Metrics.set('settt', [1, 2, 3].sample, 'second') }

sleep 5

2.times { Sentry::Metrics.incr('foo') }
7.times { Sentry::Metrics.incr('bar') }

sleep 10
