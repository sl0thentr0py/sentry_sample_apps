class Payment < ApplicationRecord
  belongs_to :user
  has_many :items

  def charge; end
end
