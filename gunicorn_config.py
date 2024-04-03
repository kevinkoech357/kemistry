
# Define the Gunicorn configuration settings
bind = "0.0.0.0:8007"
workers = 3
timeout = 180
keepalive = 5
max_requests = 1000
max_requests_jitter = 50
threads = 2
worker_connections = 1000
max_request_size = 31457280

# Server Socket
bind = "0.0.0.0:8007"
backlog = 2048

# Worker Processes
workers = 3
worker_class = "sync"
worker_connections = 1000
timeout = 1000
keepalive = 7

# Logging
accesslog = "access.log"
errorlog = "error.log"
loglevel = "info"
