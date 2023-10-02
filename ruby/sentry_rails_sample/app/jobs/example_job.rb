class ExampleJob < ApplicationJob
  queue_as :default

  def perform(*args)
    HTTParty.get('https://www.google.com')
    User.all.to_a
  end
end
