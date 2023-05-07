# Dockerfile

# Base image with specified Python version
ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy your app's requirements file
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app's source code
COPY . .

# Expose the port for your application
EXPOSE 8000

# # Run your Django app
CMD ["python", "manage.py", "runserver" ,"127.0.0.1:8000"]