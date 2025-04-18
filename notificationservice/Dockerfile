# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on (port 5001)
EXPOSE 5001

# Define environment variable for Flask to run in production
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app on port 5001
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
