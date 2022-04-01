import consumer from 'channels/consumer';

console.log(consumer);

consumer.subscriptions.create({ channel: "FoobarChannel" }, {
  received(data) {
      console.log(data);
  },
})
