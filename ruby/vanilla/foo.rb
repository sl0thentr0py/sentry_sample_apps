require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.release = 'backpressure-testing'
  config.traces_sample_rate = 1.0
  config.logger.level = :warn
  config.enable_backpressure_handling = true
end


last = Time.now
times = []

puts 'running heavy load'

50.times do
  1000.times do
    transaction = Sentry.start_transaction(name: 'backpressure')
    10.times { transaction.with_child_span(op: 'sleep', description: 'zzz') {} }
    transaction.finish
  end

  puts "queue: #{Sentry.background_worker.instance_variable_get(:@executor).queue_length}"

  now = Time.now
  times.append(now - last)
  last = now
end

puts times.join(' ')
puts 'waiting for stuff to clear'
sleep(5)

times = []
print 'running normal load'

10.times do
  50.times do
    transaction = Sentry.start_transaction(name: 'backpressure')
    10.times { transaction.with_child_span(op: 'sleep', description: 'zzz') {} }
    transaction.finish
  end

  now = Time.now
  times.append(now - last)
  last = now
end

puts times.join(' ')
