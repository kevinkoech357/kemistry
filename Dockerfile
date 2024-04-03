# Stage 1: Init
FROM python:3.11 AS init

# Install `uv` for faster package bootstrapping
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install system dependencies and create virtual environment
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    python3-dev \
    gcc \
    vim \
    sqlite3 \
    gunicorn && \
    rm -rf /var/lib/apt/lists/* && \
    /root/.cargo/bin/uv venv

# Activate virtual environment
RUN . /app/.venv/bin/activate && \
    /root/.cargo/bin/uv pip install --system --no-cache -r requirements.txt
 
# Stage 2: Copy artifacts into slim image 
FROM python:3.11-slim

# Create a non-root user
RUN adduser --disabled-password --home /app kevin

# Set the working directory and switch to non-root user
WORKDIR /app
USER kevin

# Copy files from the init stage and set permissions
COPY --chown=kevin --from=init /app /app

# Install libpq-dev for psycopg2 (skip if not using postgres).
USER root
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends libpq-dev && \
    rm -rf /var/lib/apt/lists/*
USER kevin

# Add virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose the port on which Gunicorn will listen
EXPOSE 8007

# Command to run the Flask application using Gunicorn
CMD ["gunicorn", "-c", "gunicorn_config.py" , "run:app"]