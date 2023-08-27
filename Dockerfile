# TODO: HIGH
# - Set up the base image suitable for a Python environment.
# - Expected Outcome: A base image that can run Python and necessary libraries efficiently.
# - Note: Consider using python:3.8-slim or another lightweight Python image.

# TODO: MEDIUM
# - Install necessary dependencies from requirements.txt.
# - Expected Outcome: All required Python packages installed in the Docker image.
# - Note: Use `pip install -r requirements.txt`.

# TODO: HIGH
# - Expose necessary ports for the RAG service.
# - Expected Outcome: Ports that the RAG service will run on should be exposed for external access.

# TODO: MEDIUM
# - Set the default command to run the RAG service.
# - Expected Outcome: When the Docker container starts, it should automatically start the RAG service.
# - Note: This might be something like `CMD ["python", "src/main.py"]`.

# TODO: LOW
# - Optimize the Docker image for size and performance.
# - Expected Outcome: A Docker image that is as small as possible while still being performant.
# - Note: Consider multi-stage builds or removing unnecessary files.
