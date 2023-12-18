# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

RUN chmod +x /app/run_daily.sh

# Expose port 8000 to the outside world
EXPOSE 8000

RUN python3 manage.py flush_db

RUN python3 manage.py initialize_db

# Define the command to run your application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
