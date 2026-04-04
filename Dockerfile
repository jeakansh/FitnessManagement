# Use an official lightweight Python runtime
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

ENV PYTHONPATH=/app

# Expose the port the app runs on
EXPOSE 5000

# Start the application using Gunicorn for production readiness
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
