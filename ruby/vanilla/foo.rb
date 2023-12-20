require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.logger = Logger.new($stdout)
end

transport = Sentry.get_current_client.transport

100.times { transport.record_lost_event(:ratelimit_backoff, "event") }
40.times { transport.record_lost_event(:backpressure, "transaction") }
