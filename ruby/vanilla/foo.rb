require 'sentry-ruby'
require 'pry'
require 'pry-nav'

Sentry.init do |config|
  config.debug = true
  config.before_send = lambda do |event, hint|
    puts("Before send called")
    puts event
    event
  end
end

def recurse
  recurse
end

begin
  recurse
rescue SystemStackError => exception
  Sentry.capture_exception(exception, hint: { background: false })
end
