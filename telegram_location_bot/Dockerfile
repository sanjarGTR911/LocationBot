# Use a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /telegram_location_bot

# Copy the current directory contents into the container at /app
COPY . /telegram_location_bot

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for the bot
ENV TELEGRAM_BOT_TOKEN='your_telegram_token'
ENV DB_HOST='localhost'
ENV DB_NAME='your_dbname'
ENV DB_USER='your_user'
ENV DB_PASSWORD='password'

# Run the bot
CMD ["python", "bot.py"]
