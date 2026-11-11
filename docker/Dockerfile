
# Use an official Python base image
FROM python:3.14-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency list
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask application
COPY app/app.py .

# Run the application as a non-root user
RUN useradd --create-home appuser
USER appuser

# Document the application port
EXPOSE 5000

# Start the Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "app:app"]
