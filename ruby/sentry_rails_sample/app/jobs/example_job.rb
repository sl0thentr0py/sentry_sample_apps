class ExampleJob < ApplicationJob
  queue_as :default

  def perform(*args)
    420 / 0
  end
end
