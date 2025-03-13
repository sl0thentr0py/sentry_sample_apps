require 'opentelemetry/sdk'
require 'opentelemetry/instrumentation/all'

OpenTelemetry::SDK.configure do |c|
  config = { 'OpenTelemetry::Instrumentation::Redis' => { trace_root_spans: false } }
  c.use_all(config)
  c.add_span_processor(Sentry::OpenTelemetry::SpanProcessor.instance)
end

OpenTelemetry.propagation = Sentry::OpenTelemetry::Propagator.new
