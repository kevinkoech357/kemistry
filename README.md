# Kemistry

![blog_image](https://github.com/kevinkoech357/kemistry/assets/102515005/7ce9b8c6-310f-481d-806a-3616a00fd816)


Kemistry is a full-stack blog web app designed exclusively for chemists, including professionals, students, and enthusiasts alike. Users can create posts covering various branches of chemistry, such as organic, physical, inorganic, medicinal, or general chemistry. Additionally, users have the ability to comment on posts. The app comes with 2-Factor Authorization enabled by default.


## Table of Contents

- [Required to Run](#required-to-run)
- [Installation](#installation)
- [Setting up Environment Variables](#setting-up-environment-variables)
- [Building Docker Image](#building-docker-image)
- [Run the App on Localhost](#run-the-app-on-localhost)
- [Usage](#usage)

## Required to Run

Before running Kemistry, ensure you have the following prerequisites installed:

- Python 3.8+
- Docker
- uv

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kevinkoech357/kemistry
    ```

2. Navigate to the project and set it up:

    ```bash
    cd kemistry
    # Create virtualenv using uv
    uv venv
    source .venv/bin/activate
    # Install extensions
    uv pip install -r requirements.txt
    # Running tests
    pytest
    ```

## Setting up Environment Variables

Create a `.env` file in the project directory and add the following variables:

```plaintext
SQLALCHEMY_DATABASE_URI=
SECRET_KEY=
SECURITY_PASSWORD_SALT=
SECURITY_TOTP_SECRETS=
MAIL_SERVER=
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_DEFAULT_SENDER=
ADMIN_EMAIL=
ADMIN_PASSWORD=
ADMIN_USERNAME=
```

## Building Docker Image
You can also build a Docker image to run Kemistry:

Ensure [Docker](https://docs.docker.com/engine/install/) is installed on your machine.

```bash
# Build Image
docker build -t kemistry .
```

## Run the App on Localhost
To run the app on your local machine, follow these steps:

Ensure you are in the project directory.

Run the app:

```bash
python run.py
or
gunicorn -c gunicorn_config.py run:app
```
Or, if you prefer Docker:

```bash
docker run -p 8007:8007 --env-file .env kemistry
```

This will run the Kemistry app inside a Docker container.

## Usage
Once the app is running, you can access it by navigating to ```http://localhost:8000``` 0r ```http://localhost:8007``` in your web browser. From there, you can create posts on various branches of chemistry and engage with other users through comments. 

Enjoy using Kemistry!
