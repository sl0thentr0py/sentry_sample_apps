require 'sentry-ruby'
require 'debug'

Sentry.init do |config|
  config.logger.level = :debug
end

e = Sentry::Event.new(configuration: Sentry.configuration)
b = Sentry::BreadcrumbBuffer.new
b.record(Sentry::Breadcrumb.new(message: "\x76\xab\x99\xb5"))
e.breadcrumbs = b

Sentry.send_event(e, background: false)
