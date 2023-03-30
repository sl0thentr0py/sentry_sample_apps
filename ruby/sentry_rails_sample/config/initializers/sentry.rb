Sentry.init do |config|
  config.breadcrumbs_logger = [:active_support_logger, :http_logger]
  config.traces_sample_rate = 1.0
  config.profiles_sample_rate = 0.5
  config.debug = true
  config.logger.level = ::Logger::DEBUG
  config.include_local_variables = true
  config.release = "test-sessions-#{Time.now.utc}"
end
