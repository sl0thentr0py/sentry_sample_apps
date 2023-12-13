class PaymentsController < ActionController::Base
  before_action :set_sentry_user, except: [:cable, :profile]
  skip_forgery_protection

  def error
    1 / 0
  end

  def view_error;end

  def twp
    HTTParty.get('http://127.0.0.1:5000/error')
    420 / 0
    render(plain: "twp")
  end

  def success
    foo
    HTTParty.get('https://www.google.com')
    bar
    render(plain: "success")
  end

  def http
    HTTParty.get('https://username:password@example.com/foo?bar=23&baz=cow#fragment_foobar')
    render(plain: "success")
  end

  def measurement
    transaction = Sentry.get_current_scope.get_transaction
    transaction.set_measurement("metrics.foo", 0.5, "millisecond")
    render(plain: "metrics.foo: 0.5 ms")
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

    Redis.new.set("mykey", "hello world")

    payment.amount = payment.items.map { |i| i.quantity * i.price }.sum
    payment.save

    discounted_amount = payment.amount / discount_factor
    payment.update(amount: discounted_amount)

    @success = payment.charge
  end

  def cable_test
  end

  def profile
    slow_ass_function
    render(plain: "ok")
  end

  def sidekiq
    ::OuterLongAssName::InnerLongAssNameLongAssNameLongAssName::SidekiqJob.perform_in(5.seconds, 'https://google.com')
    render(plain: 'queued')
  end

  private

  def slow_ass_function
    garbage_code
  end

  def garbage_code
    (1e7).to_i.times { 2 * 2 }
  end

  def foo
    sleep 0.2
  end

  def bar
    (1e6).to_i.times { 2*2 }
  end


  def set_sentry_user
    @user = User.find_by_email('jane.doe@example.com')
    return unless @user
    Sentry.set_user(username: @user.username, email: @user.email) if defined?(Sentry)
  end
end
