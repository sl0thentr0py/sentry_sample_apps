Sentry.init do |config|
  config.breadcrumbs_logger = [:active_support_logger, :http_logger]
  # config.traces_sample_rate = 1.0
  config.debug = true
  config.capture_exception_frame_locals = true
  config.transport.ssl = { min_version: OpenSSL::SSL::TLS1_3_VERSION }
end
