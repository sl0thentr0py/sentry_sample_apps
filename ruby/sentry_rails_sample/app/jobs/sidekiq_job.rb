class SidekiqJob
  include Sidekiq::Job
  include Sentry::Cron::MonitorCheckIns

  sentry_monitor_check_ins slug: 'sidekiq_slug', monitor_config: Sentry::Cron::MonitorConfig.from_interval(1, :minute)

  def perform(site, user = true)
    HTTParty.get(site)
    User.all.to_a if user
  end
end
