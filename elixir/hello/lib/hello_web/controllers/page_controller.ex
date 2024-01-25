defmodule HelloWeb.PageController do
  use HelloWeb, :controller

  alias Hello.{Repo, User}
  import Ecto.Query, only: [first: 1]

  def index(conn, _params) do
    render(conn, "index.html")
  end

  def error(conn, _params) do
    raise "oops"
    text(conn, "whhops")
  end

  def trace(conn, _params) do
    json(conn, User |> first() |> Repo.one() |> Map.from_struct |> Map.drop([:__meta__]))
  end
end
