class PaymentsController < ActionController::Base
  before_action :set_sentry_user
  skip_forgery_protection

  def checkout
    return unless request.post?

    params = JSON.parse(request.body.read).with_indifferent_access

    payment = Payment.new(user: @user,
                           currency: params[:payment][:currency],
                           address: params[:payment][:address])

    params[:items].each do |item_params|
      payment.items << Item.new(item_params)
    end

    payment.amount = payment.items.map { |i| i.quantity * i.price }.sum
    payment.save

    1 / 0
    @success = payment.charge
  end

  private

  def set_sentry_user
    @user = User.find_by_email('jane.doe@example.com')
    Sentry.set_user(username: @user.username, email: @user.email)
  end
end
