Sentry.init do |config|
  config.breadcrumbs_logger = [:active_support_logger, :http_logger]
  config.traces_sample_rate = 1.0
  config.debug = true
  config.logger.level = ::Logger::INFO
  config.capture_exception_frame_locals = true
  config.release = "test-sessions-#{Time.now.utc}"
  config.before_send_transaction = lambda do |event, _h|
    # filter out SQL queries from spans with sensitive data
    event.spans.each do |span|
      span[:description] = '<FILTERED>' if span[:op].start_with?('db')
    end
    event
  end
end
