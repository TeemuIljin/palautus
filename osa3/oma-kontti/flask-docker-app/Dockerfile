FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 80

# Set the environment variable for Flask
ENV PYTHONUNBUFFERED=1
ENV PORT=80

# Command to run the application
CMD ["gunicorn", "app:create_app()", "--bind", "0.0.0.0:80", "--worker-class", "sync", "--workers", "2"]