# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask

# Expose port 80 for the Flask app
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
