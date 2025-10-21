Sentry.init do |config|
  config.breadcrumbs_logger = [:active_support_logger, :http_logger, :redis_logger]
  config.traces_sample_rate = 1.0
  config.profiles_sample_rate = 1.0
  config.profiler_class = Sentry::Vernier::Profiler
  config.enable_logs = true
  config.send_default_pii = true
  config.sdk_logger.level = ::Logger::DEBUG
  config.include_local_variables = true
  config.release = "test-neel-#{Time.now.utc}"
  config.enabled_patches << :graphql
end
