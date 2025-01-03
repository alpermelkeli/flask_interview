# my-flask-app/my-flask-app/README.md

# My Flask App

This is a basic Flask application that demonstrates the structure and setup of a Flask project.

## Project Structure

```
my-flask-app
├── app
│   ├── __init__.py
│   ├── routes.py
|   |── models.py
│   └── templates
│       └── quiz_template.html
├── run.py
├── requirements.txt
├── seed_database.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-flask-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute the following command:
```
python seed_database.py
python run.py
```

The application will be available at `http://127.0.0.1:5000/`.

## License

This project is licensed under the MIT License.
