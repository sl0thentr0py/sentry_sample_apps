import './app.css'
import App from './App.svelte'

import * as Sentry from "@sentry/svelte";

// Initialize the Sentry SDK here
Sentry.init({
    dsn: "https://cdf89e7156034172a513e112d3ac10f7@o447951.ingest.us.sentry.io/4505029409374208",
    debug: true,
    integrations: [Sentry.browserTracingIntegration()],
    tracesSampleRate: 1.0,
    tracePropagationTargets: ["localhost"],
});

const app = new App({
    target: document.getElementById('app'),
})

export default app
