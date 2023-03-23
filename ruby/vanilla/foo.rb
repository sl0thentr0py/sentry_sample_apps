require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.release = "profiling"
  config.debug = true
  config.traces_sample_rate = 1.0
end

def t1
  10000.times { 2 + 2 }
  sleep 0.2
  puts('t1')
end

def t2
  transaction = Sentry.start_transaction(name: 'profiling')
  Sentry.get_current_scope.set_span(transaction)

  sleep 0.5
  t1
  20000.times { 2 * 2 }
  puts('t2')

  transaction.finish
end

def main
  sleep 0.2
  20000.times { 2 ** 2 }
  puts('main')
end


# transaction = Sentry.start_transaction(name: 'profiling')
# Sentry.get_current_scope.set_span(transaction)

threads = [Thread.new { t1 }, Thread.new { t2 }]
main
threads.each(&:join)

# transaction.finish
