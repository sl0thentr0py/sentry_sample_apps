class SidekiqJob
  include Sidekiq::Job
  def perform(*args)
    raise 'test'
  end
end
