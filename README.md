# sentry_sample_apps

make sure to export `SENTRY_DSN` env variable

## docker db

```bash
docker run --name rails-postgres -e POSTGRES_PASSWORD=rails -e POSTGRES_USER=rails -d -p 5432:5432 postgres
```
