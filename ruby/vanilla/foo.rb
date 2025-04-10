require 'sentry-ruby'
require 'concurrent'
require 'debug'

Sentry.init do |config|
  config.logger.level = :debug
  config.traces_sample_rate = 1.0
end

transaction = Sentry.start_transaction(name: 'transaction')
Sentry.get_current_scope.set_span(transaction)

hub_to_propagate = Sentry.get_current_hub

results = 5.times.map do |i|
  Concurrent::Promises.future(i) do |t|
    Thread.current.thread_variable_set(Sentry::THREAD_LOCAL, hub_to_propagate)

    Sentry.with_child_span(op: 'promise') do
      t*123123123**213131  # expensive operation
    end
  end
end.map(&:value)

transaction.finish
