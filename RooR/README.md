# Eurocybersecurite AI Cybersecurity Application

This is an AI-powered cybersecurity application developed by Eurocybersecurite.

## Description

This application uses a lightweight AI model to detect and counter persistent AI attacks that evade traditional controls.

## Installation

1.  Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
2.  Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Functioning and Objective

This application uses a pre-trained Hugging Face model to analyze text data and determine if it contains a cybersecurity threat. The objective is to provide a quick and easy way to assess the potential risk of a given piece of text.

## Usage

1.  Run the application:
    ```bash
    python main.py
    ```
2.  Open your web browser and go to `http://localhost:5577`
3.  Enter a piece of text in the "Enter data to analyze" field and click the "Run Analysis" button.
4.  The application will display the analysis output, including the threat level and the model type.

## PyPI Deployment

1.  Install `twine`:
    ```bash
    pip install twine
    ```
2.  Build the distribution packages:
    ```bash
    python setup.py sdist bdist_wheel
    ```
3.  Upload the packages to PyPI:
    ```bash
    twine upload dist/*
    ```

## GitHub Deployment

1.  Create a new repository on GitHub.
2.  Push the application code to the repository:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin <repository_url>
    git push -u origin main
    ```

## Contributing

Contributions are welcome! Please submit a pull request.

## License

[License]
