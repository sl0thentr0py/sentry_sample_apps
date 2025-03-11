class User < ApplicationRecord
  has_many :payments

  def self.broken_method
    raise "error"
  end
end
