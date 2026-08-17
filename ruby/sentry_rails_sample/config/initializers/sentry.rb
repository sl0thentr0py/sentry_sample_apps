Sentry.init do |config|
  config.breadcrumbs_logger = [:active_support_logger, :http_logger, :redis_logger]
  config.traces_sample_rate = 1.0
  config.trace_ignore_status_codes = []
  config.enable_logs = true
  config.wololo = true
  config.wololo_openrouter_api_key = ENV.fetch("OPENROUTER_API_KEY_WORK")
  config.send_default_pii = true
  config.sdk_logger = ::Sentry::Logger.new(Rails.root.join("log/sentry.log"))
  config.sdk_logger.level = ::Logger::DEBUG
  config.include_local_variables = true
  config.release = "test-neel-#{Time.now.utc}"
  config.enabled_patches << :graphql
end
