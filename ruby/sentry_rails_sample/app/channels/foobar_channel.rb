class FoobarChannel < ApplicationCable::Channel
  def subscribed
    # raise "Neel actioncable test"
    stream_from "foobar_channel"
  end

  def unsubscribed
  end
end
