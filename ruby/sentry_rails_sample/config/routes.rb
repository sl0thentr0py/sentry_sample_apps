Rails.application.routes.draw do
  if Rails.env.development?
    mount GraphiQL::Rails::Engine, at: "/graphiql", graphql_path: "/graphql"
  end
  post "/graphql", to: "graphql#execute"
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  match 'checkout', to: 'payments#checkout', via: [:get, :post]
  get 'error', to: 'payments#error'
  get 'view_error', to: 'payments#view_error'
  get 'success', to: 'payments#success'
  get 'measurement', to: 'payments#measurement'
  get 'cable_test', to: 'payments#cable_test'
  get 'ds/items', to: 'ds#items'
  get 'ds_rails_head', to: 'ds#ds_rails_head'
  get 'profile', to: 'payments#profile'
  get 'http', to: 'payments#http'
  get 'twp', to: 'payments#twp'
  get 'sidekiq', to: 'payments#sidekiq'
  get 'active_job', to: 'payments#active_job' # can use with multiple adapters
  get 'delayed_job', to: 'payments#delayed_job'
end
