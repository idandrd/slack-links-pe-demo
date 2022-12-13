# Slack Links Privacy Violation Demo App
This app demonstrates the `links:read` and `links:write` vulnerability in slack.

The app can be installed in Slack-workspace by any of the workspace users, thus gaining the user the ability to monitor every link sent to the specified domains (`docusign.net` and `docusign.com`).
Every link sent to the specified domains, even in private chats, will be also sent to the app.

In addition, the app inserts a phishing button that will appear under any link sent, and will send users to a decoy site.
