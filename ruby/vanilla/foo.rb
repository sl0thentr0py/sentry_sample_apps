require 'sentry-ruby'
require 'debug'
require 'image_processing/vips'

Sentry.init do |config|
  config.logger.level = :debug
  config.excluded_exceptions += ['Vips::Error']
end

begin
  ImageProcessing::Vips::Processor.call(
    source: 'sample1.jfiadsadf',
    loader: { page: 0 },
    operations: [[:resize_to_limit, [200, 200]]],
    saver: {},
    destination: 'output.jfif'
  )
rescue => e
  Sentry.capture_exception(e)
end

sleep 2
