from src.api.server import create_app

app = create_app()

if __name__ == "__main__":
    app.run()

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
