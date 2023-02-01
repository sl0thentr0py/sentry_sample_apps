defmodule HelloWeb.PageController do
  use HelloWeb, :controller

  def index(conn, _params) do
    render(conn, "index.html")
  end

  def error(conn, _params) do
    raise "oops"
    text(conn, "whhops")
  end
end
