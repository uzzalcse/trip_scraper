FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/
  # Copy the 'data' folder from your local machine to the container


CMD ["scrapy", "crawl", "hotels_spider"]