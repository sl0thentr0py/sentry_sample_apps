class DsController < ApplicationController
  before_action :set_sentry_user, except: :cable
  skip_forgery_protection

  def items
    items = []
    items = Item.joins(:payment).where(payments: { user: @user }) if @user
    render(json: items)
  end

  private

  def set_sentry_user
    @user = User.find_by_email('jane.doe@example.com')
    return unless @user
    Sentry.set_user(username: @user.username, email: @user.email)
  end
end
