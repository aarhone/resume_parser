# Candidate Data Processing and Filtering

## Summary

This project is a Python-based tool designed for parsing, processing, and filtering candidate resumes. It automates the extraction of relevant information from resume files and supports storing parsed data in MongoDB for easy retrieval and analysis. The goal is to streamline candidate data handling in recruitment workflows.

## Features

- Automated resume parsing to extract key candidate information (name, contact, skills, experience, etc.)
- Filtering and searching candidates using customizable criteria
- Stores candidate data in MongoDB for scalable data management
- Simple driver script to process resumes and manage candidate data
- Command-line operation for integration into broader recruitment pipelines

## Setup

1. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the required packages:**

    ```sh
    pip3 install -r requirements.txt
    ```

3. **Set up MongoDB:**

    Ensure MongoDB is installed and running on your local machine. The default configuration connects to `mongodb://localhost:27017/`.

## Usage

Run the `driver.py` script to start the application:

```sh
python3 driver.py

```
