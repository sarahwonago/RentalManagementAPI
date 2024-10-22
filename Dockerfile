# Step 1: Base Image
FROM python:3.10-alpine

# Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Step 3: Set working directory
WORKDIR /usr/src/app

# Step 4: Install dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy project files
COPY . /usr/src/app/


# Step 6: Expose port 8000
EXPOSE 8000

# Step 7: Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
