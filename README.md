# Project Name

Brief description of the project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the project, follow these steps:

1. **Unzip the File:** Unzip the downloaded file.

2. **Create a Virtual Environment:** Create a virtual environment for the project to manage dependencies and isolate the project environment. You can create a virtual environment using `virtualenv` or `venv`. Example:

    ```bash
    virtualenv venv
    ```

3. **Install Requirements:** Navigate to the project directory and install the required dependencies by running:

    ```bash
    pip install -r requirements/local.txt
    ```

4. **Database Setup:** Run the following commands to set up the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Usage

To run the application, execute the following command:

```bash
python manage.py runserver

python manage.py runserver --port <port_number>

