class ExampleJob < ApplicationJob
  def perform(site, user: true)
    HTTParty.get(site)
    User.all.to_a if user
  end
end
