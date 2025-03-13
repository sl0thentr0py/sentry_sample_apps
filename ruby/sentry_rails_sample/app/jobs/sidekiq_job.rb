class SidekiqJob
  include Sidekiq::Job

  def perform(site, user)
    HTTParty.get(site)
    User.all.to_a if user
  end
end
