require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.release = "profiling"
  config.debug = true
  config.traces_sample_rate = 1.0
end

def foo
  Sentry.with_child_span(op: 'foo') do |span|
    10000.times { 2 + 2 }
    sleep 0.2
    print('foo')
  end
end

def bar
  Sentry.with_child_span(op: 'bar') do
    sleep 0.5
    foo
    20000.times { 2 * 2 }
    print('bar')
  end
end


transaction = Sentry.start_transaction(name: 'profiling')
Sentry.get_current_scope.set_span(transaction)
foo
bar
transaction.finish
