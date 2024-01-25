defmodule HelloWeb.PageController do
  use HelloWeb, :controller

  alias Hello.{Repo, User}

  def index(conn, _params) do
    render(conn, "index.html")
  end

  def error(conn, _params) do
    raise "oops"
    text(conn, "whhops")
  end

  def trace(conn, _params) do
    json(conn, Repo.one(User) |> Map.from_struct |> Map.drop([:__meta__]))
  end
end
