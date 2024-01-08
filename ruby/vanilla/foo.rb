require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.debug = true
  config.logger.level = ::Logger::DEBUG
end

10.times do |i|
  crumb = Sentry::Breadcrumb.new(
    data: { foo: 42 },
    category: 'crumb',
    message: "crumb no: #{i}"
  )

  Sentry.add_breadcrumb(crumb)
end

config = Sentry::Cron::MonitorConfig.from_interval(1, :minute)
Sentry.capture_check_in('test-scope', :in_progress, monitor_config: config)
