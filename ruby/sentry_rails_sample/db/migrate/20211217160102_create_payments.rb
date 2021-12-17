class CreatePayments < ActiveRecord::Migration[6.1]
  def change
    create_table :payments do |t|
      t.references :user, null: false, foreign_key: true
      t.integer :amount
      t.string :currency
      t.string :address

      t.timestamps
    end
  end
end
