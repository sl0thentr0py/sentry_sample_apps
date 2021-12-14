class ErrorsController < ActionController::Base
  before_action :set_sentry_user

  def failed_payment
    amount = 100
    currency = 'USD'
    address = 'Times Square'
    payment = Payment.new(amount, currency, address)

    1 / 0

    head(:ok)
  end

  private

  def set_sentry_user
    Sentry.set_user(email: 'jane.doe@foobar.com')
  end
end
