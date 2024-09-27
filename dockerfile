# Use official Python image from Docker Hub
FROM python:3.12.6

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY . /app 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code


# Expose the port Flask runs on
EXPOSE 5000

# Define environment variables for Flask


# Start the Flask app
CMD ["python", "app.py"]
