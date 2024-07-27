
FROM python:3.9-slim

# working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

RUN pip install pandas

# Run the application
CMD ["python", "main.py"]

