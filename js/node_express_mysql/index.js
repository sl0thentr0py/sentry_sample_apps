const Sentry = require('@sentry/node');
const Tracing = require("@sentry/tracing");
const express = require('express')
const app = express()
const port = 8000
const https = require('https')
const http = require('http')
var mysql = require('mysql');

Sentry.init({
    dsn: "http://12345abcdb1e4c123490ecec89c1f199@127.0.0.1:3010/1",
    integrations: [
        // enable HTTP calls tracing
        new Sentry.Integrations.Http({ tracing: true }),
        // enable Express.js middleware tracing
        new Tracing.Integrations.Express({ app }),
        new Tracing.Integrations.Mysql(),
    ],
    // We recommend adjusting this value in production, or using tracesSampler
    // for finer control
    tracesSampleRate: 1.0,
    debug:true,
});

var connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: "sentrysql",
});

connection.connect((err) => {
    if (err) {
        console.log("Error occurred", err);
    }
});

// RequestHandler creates a separate execution context using domains, so that every
// transaction/span/breadcrumb is attached to its own Hub instance
//app.use(Sentry.Handlers.requestHandler());
app.use(
    Sentry.Handlers.requestHandler({
        //transaction: 'handler',
        //serverName: false,
    })
);
// TracingHandler creates a trace for every incoming request
app.use(Sentry.Handlers.tracingHandler({}));

// All controllers should live here
app.get("/", function (req, res) {

    const query = "SELECT * FROM names LIMIT 0, 1000"
    connection.query(query, function (err, result) {
        if (err) {
            console.log("Error query", err);
        }
        console.log(result);
        res.end("CaptureException test event sent.");
    });

});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
