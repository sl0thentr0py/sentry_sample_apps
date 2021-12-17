class CreateItems < ActiveRecord::Migration[6.1]
  def change
    create_table :items do |t|
      t.references :payment, null: false, foreign_key: true
      t.string :name
      t.integer :quantity
      t.integer :price

      t.timestamps
    end
  end
end
