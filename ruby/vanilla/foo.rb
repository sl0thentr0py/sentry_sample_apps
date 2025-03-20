require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.logger.level = :debug
  config.traces_sample_rate = 1.0
end

transaction = Sentry.start_transaction(name: 'transaction')
Sentry.get_current_scope.set_span(transaction)

Sentry.with_child_span(op: 'child_same_thread') do
  Thread.new do
    Sentry.with_child_span(op: 'child_new_thread') do
      sleep 0.3
    end
  end

  sleep 0.5
end

transaction.finish
