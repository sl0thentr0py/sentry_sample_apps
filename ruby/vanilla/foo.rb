require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.release = "crons-testing"
  config.debug = true
  config.traces_sample_rate = 1.0
end

config = Sentry::Cron::MonitorConfig.from_interval(300, :minute)
Sentry.capture_check_in("Crontab_300", :ok, monitor_config: config)

sleep 1
