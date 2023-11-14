module OuterLongAssName
  module InnerLongAssNameLongAssNameLongAssName
    class SidekiqJob
      include Sidekiq::Job
      include Sentry::Cron::MonitorCheckIns

      sentry_monitor_check_ins monitor_config: Sentry::Cron::MonitorConfig.from_crontab("0 * * * *")

      def perform(site, user = true)
        HTTParty.get(site)
        User.all.to_a if user
      end
    end
  end
end
