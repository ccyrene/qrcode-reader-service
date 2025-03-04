# Use a minimal Python image (Alpine-based)
FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Run the QR code reader script
ENTRYPOINT ["python", "app.py"]