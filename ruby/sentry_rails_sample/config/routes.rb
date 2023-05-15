Rails.application.routes.draw do
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  match 'checkout', to: 'payments#checkout', via: [:get, :post]
  get 'error', to: 'payments#error'
  get 'success', to: 'payments#success'
  get 'measurement', to: 'payments#measurement'
  get 'cable_test', to: 'payments#cable_test'
  get 'ds/items', to: 'ds#items'
  get 'ds_rails_head', to: 'ds#ds_rails_head'
  get 'profile', to: 'payments#profile'
  get 'http', to: 'payments#http'
end
