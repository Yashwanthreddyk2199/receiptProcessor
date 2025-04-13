# Use an official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt


# Copy the Django project code
COPY . .

# Expose port (default for Django dev server)
EXPOSE 8000

# Run Django development server
CMD ["python3", "receiptProcessorproject/manage.py", "runserver", "0.0.0.0:8000"]