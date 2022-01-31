Rails.application.routes.draw do
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  match 'checkout', to: 'payments#checkout', via: [:get, :post]
  get 'error', to: 'payments#error'
end
