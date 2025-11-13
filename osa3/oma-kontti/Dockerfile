FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the dependency files
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-dev

# Copy the application code
COPY src/ ./src/

# Expose the port the app runs on
EXPOSE 80

# Set the command to run the application
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=80"]