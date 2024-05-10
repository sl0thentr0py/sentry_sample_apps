class DsController < ApplicationController
  before_action :set_sentry_user, except: :cable
  skip_forgery_protection

  def items
    items = []
    items = Item.joins(:payment).where(payments: { user: @user }) if @user

    # turn flask on in same repo/python/flask_sqlalchemy for this
    begin
      res = HTTParty.get('http://127.0.0.1:5000/ds', format: :plain)
      external = JSON.parse(res)
    rescue
    ensure
      external ||= {}
    end

    render(json: { items: items }.merge(external))
  end

  def ds_rails_head; end

  private

  def set_sentry_user
    @user = User.find_by_email('jane.doe@example.com')
    return unless @user
    Sentry.set_user(username: @user.username, email: @user.email)
  end
end
