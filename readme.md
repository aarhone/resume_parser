# Candidate Data Processing and Filtering

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