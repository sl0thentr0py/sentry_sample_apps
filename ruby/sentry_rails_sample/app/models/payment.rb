class Payment
  attr_accessor :amount, :currency, :address

  def initialize(amount, currency, address)
    @amount = amount
    @currency = currency
    @address = address
  end
end
