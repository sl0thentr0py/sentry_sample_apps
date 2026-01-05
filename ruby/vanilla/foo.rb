require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.sdk_logger.level = :debug
  config.traces_sample_rate = 1.0
  config.enable_metrics = true
  config.send_default_pii = true
end

transaction = Sentry.start_transaction(name: 'test metrics')
Sentry.get_current_scope.set_span(transaction) if transaction
Sentry.get_current_scope.set_user({ id: '1234', username: 'jane', email: 'jane.doe@sentry.io' })

Sentry.with_child_span(op: 'one', description: 'stuff') do
  Sentry.metrics.count('counter')
  sleep 0.2

  Sentry.with_child_span(op: 'many', description: 'more stuff') do
    sleep 6
    Sentry.metrics.count('counter', value: 20)
  end
end

transaction.finish

sleep 3
