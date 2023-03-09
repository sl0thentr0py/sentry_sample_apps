require 'sentry-ruby'
require 'pry'
require 'pry-nav'

Sentry.init do |config|
  config.debug = true
  config.traces_sample_rate = 1.0
end


transaction = Sentry.start_transaction(name: 'testing long desc')
long_ass_string = (1..10000).map(&:to_s).join('-')
transaction.with_child_span(description: long_ass_string) do
  sleep(1)
end
transaction.finish
