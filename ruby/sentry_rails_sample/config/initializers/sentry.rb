Sentry.init do |config|
  config.breadcrumbs_logger = [:active_support_logger, :http_logger, :redis_logger]
  config.traces_sample_rate = 1.0

  config.data_collection.user_info = true
  config.data_collection.cookies.mode = :deny_list
  config.data_collection.cookies.terms = ["session", "token"]
  config.data_collection.http_headers.request.mode = :allow_list
  config.data_collection.http_headers.request.terms = ["X-Public-Data"]
  config.data_collection.http_bodies = [:incoming_request]
  config.data_collection.url_query_params.mode = :deny_list
  config.data_collection.graphql.document = true
  config.data_collection.graphql.variables = true
  config.data_collection.database_query_data = true
  config.data_collection.queues = true
  config.data_collection.stack_frame_variables = true
  config.data_collection.frame_context_lines = 5

  config.release = "test-neel-#{Time.now.utc}"
  config.enabled_patches << :graphql
end
