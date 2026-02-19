# Start from official Spark image
FROM apache/spark:3.5.1-python3

# Switch to root user to install packages
USER root

# Update and install any system deps if needed (optional but safe)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages as root (system-wide)
RUN pip install --no-cache-dir \
    kafka-python \
    pyspark

# Switch back to the spark user for runtime (best practice)
USER spark

# Set working directory (owned by spark user)
WORKDIR /opt/spark/work-dir/apps

# Copy your consumer code
COPY . .

# Run your script (change filename if it's not consumer.py)
CMD ["python", "consumer.py"]