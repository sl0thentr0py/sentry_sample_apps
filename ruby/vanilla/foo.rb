require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.debug = true
  config.logger.level = ::Logger::DEBUG
  config.enable_metrics = true
  config.enable_tracing = true
  config.release = "testing-metrics"
end

transaction = Sentry.start_transaction(name: 'metrics tx')
Sentry.get_current_scope.set_span(transaction)
10.times { Sentry::Metrics.incr('foo') }
100.times { Sentry::Metrics.gauge('gauge', Random.rand, unit: 'ratio', tags: { 'with' => 'transaction' }) }
transaction.finish

sleep 10
