# README

This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to cover:

* Ruby version

* System dependencies

* Configuration

* Database creation

```
docker run -p 5432:5432 --name rails-postgres -e POSTGRES_USER=rails -e POSTGRES_PASSWORD=rails -d postgres
docker run --name rails-redis -d -p 6379:6379 redis
```

* Database initialization

* How to run the test suite

* Services (job queues, cache servers, search engines, etc.)

* Deployment instructions

* ...

