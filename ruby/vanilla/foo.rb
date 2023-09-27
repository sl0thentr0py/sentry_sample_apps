require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.release = "crons-testing"
  config.debug = true
  config.traces_sample_rate = 1.0
end

schedule = Sentry::Cron::MonitorSchedule::Crontab.new("blablabla")
config = Sentry::Cron::MonitorConfig.new(schedule)
Sentry.capture_check_in("crontab_bad_test", :ok, monitor_config: config)

sleep 1
