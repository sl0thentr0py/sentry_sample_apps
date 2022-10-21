require 'opentelemetry/sdk'
require 'opentelemetry/instrumentation/all'

OpenTelemetry::SDK.configure do |c|
  c.use_all
  c.add_span_processor(Sentry::OpenTelemetry::SpanProcessor.new)
end

Rails.application.config.middleware.move_after(
  Sentry::Rails::CaptureExceptions,
  OpenTelemetry::Instrumentation::Rack::Middlewares::TracerMiddleware
)
