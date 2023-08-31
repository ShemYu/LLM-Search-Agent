from src.api.server import create_app

app = create_app()

if __name__ == "__main__":
    app.run()

# TODO: HIGH
# - Implement the 'healthz' endpoint.
# - Expected Outcome: An endpoint that responds with a 200 OK status, indicating the server is healthy.
# - Note: This is crucial for Kubernetes liveness and readiness probes.

# TODO: MEDIUM
# - Implement the 'test' endpoint.
# - Expected Outcome: An endpoint that can be used to test if the server is responding correctly and can access necessary resources.
# - Note: This can be a simple endpoint that returns a test message or performs a basic operation.

# TODO: LOW
# - Add logging to the server.
# - Expected Outcome: Important events, errors, and access logs are recorded.
# - Note: Consider using Python's built-in logging module.

# TODO: MEDIUM
# - Handle exceptions and errors gracefully.
# - Expected Outcome: Instead of crashing, the server should return appropriate error messages and status codes.
# - Note: Ensure that sensitive information is not leaked in error messages.

# TODO: LOW
# - Optimize server settings for production.
# - Expected Outcome: The server should be configured with settings suitable for a production environment.
# - Note: This includes things like disabling debug mode, setting up proper request limits, etc.
