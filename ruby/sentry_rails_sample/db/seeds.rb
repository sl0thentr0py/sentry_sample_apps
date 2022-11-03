# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

u = User.create(username: 'foobar', email: 'jane.doe@example.com')

10.times do |i|
  p = Payment.create(user: u, amount: 10, currency: 'USD', address: 'Times Square, NY')

  5.times do |j|
    Item.create(payment: p, name: "Item #{j}", quantity: 5, price: 99)
  end
end
