import consumer from 'channels/consumer';

console.log(consumer);

consumer.subscriptions.create({ channel: "FoobarChannel" }, {
    connected() {
        console.log("Connected to the channel:", this);
    },
    disconnected() {
        console.log("Disconnected");
    },
    received(data) {
        console.log("Received some data:", data);
    }
})
