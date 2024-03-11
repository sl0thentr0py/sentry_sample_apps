require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.debug = true
  config.logger.level = ::Logger::DEBUG
  config.metrics.enabled = true
  config.enable_tracing = true
  config.release = "testing-metrics"
end

transaction = Sentry.start_transaction(name: 'metrics tx')
Sentry.get_current_scope.set_span(transaction)
10.times { Sentry::Metrics.increment('foo') }
100.times { Sentry::Metrics.gauge('gauge', Random.rand, unit: 'ratio', tags: { 'with' => 'transaction' }) }
Sentry::Metrics.timing('time', unit: 'microsecond') do
  sleep(1.5)
end
transaction.finish

sleep 10
