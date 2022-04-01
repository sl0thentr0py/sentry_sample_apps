class PaymentsController < ActionController::Base
  before_action :set_sentry_user, except: :cable
  skip_forgery_protection

  def error
    1 / 0
  end

  def success
    render(plain: "success")
  end

  def checkout
    return unless request.post?

    params = JSON.parse(request.body.read).with_indifferent_access

    discount_factor = params[:discount].to_i

    payment = Payment.new(user: @user,
                           currency: params[:payment][:currency],
                           address: params[:payment][:address])

    params[:items].each do |item_params|
      payment.items << Item.new(item_params)
    end

    payment.amount = payment.items.map { |i| i.quantity * i.price }.sum
    payment.save

    discounted_amount = payment.amount / discount_factor
    payment.update(amount: discounted_amount)

    @success = payment.charge
  end

  def cable_test
  end

  private

  def set_sentry_user
    @user = User.find_by_email('jane.doe@example.com')
    return unless @user
    Sentry.set_user(username: @user.username, email: @user.email)
  end
end
