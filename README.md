# Fourth Sail Capital - Data Engineering Internship Project

## Overview

This project is a Python application developed by Bruno Fernandes Maione as part of the entrance process for the Data Engineering Internship position at Fourth Sail Capital. The objective of this project is to scrape daily currency prices from Yahoo Finance, store the data in a SQLite database, and provide a Jupyter notebook for data visualization.

## Requirements

To run this project, you need Python 3.x installed on your system. All the necessary dependencies are listed in the `requirements.txt` file, and you can install them by running the following command:

```pip install -r requirements.txt```


## Project Structure

The project directory is organized as follows:

```
my_currency_app/
├── src/
│ ├── init.py
│ ├── scraper.py
│ ├── processor.py
│ ├── database.py
│ └── tests/
│ ├── init.py
│ ├── test_scraper.py
│ ├── test_processor.py
│ └── test_database.py
├── data/
│ └── my_currency.db
├── jupyter/
│ └── my_currency.ipynb
├── requirements.txt
└── Dockerfile
```


- `src`: Contains the main source code for the application.
- `scraper.py`: Implements the web scraping logic using Selenium to fetch currency data from Yahoo Finance.
- `processor.py`: Processes the scraped data and stores it in the SQLite database.
- `database.py`: Provides functions to create a connection to the database and create the necessary table.
- `tests`: Contains unit tests for the web scraper, data processor, and database functionality.
- `data`: Directory to store the SQLite database file.
- `jupyter`: Contains the Jupyter notebook for data visualization.
- `requirements.txt`: Lists the project dependencies.
- `Dockerfile`: Defines the Docker image for running the application.

## Running the Application

To run the web scraping and data processing application, execute the following command from the root of the project:

```python src/scraper.py```

This will scrape the currency data from Yahoo Finance and store it in the SQLite database.

## Running Unit Tests

To run the unit tests, use the pytest framework. Run the following command from the root of the project:

```pytest```

This will discover and execute all the test files in the `tests` folder and display the test results.

## Data Visualization

To visualize the stored currency data, open the Jupyter notebook `my_currency.ipynb` in the `jupyter` folder. This notebook connects to the SQLite database, retrieves the data, and provides data visualization using matplotlib and seaborn libraries.

## Dockerization (Bonus)

If you prefer to run the application in a Docker container, you can build the Docker image using the provided `Dockerfile`. Run the following commands from the root of the project:

```
docker build -t my_currency_app .
docker run -it --rm --name my_currency_container my_currency_app
```

## Example (Bonus)

Here it is an example of the output of the main scrapping function running in a macOS machine:

<img width="735" alt="Captura de Tela 2023-07-20 às 12 52 55" src="https://github.com/Maionepy/Code-Challenge-Fourthsailcap/assets/62849365/c62d6020-3838-487e-9ee1-85367aadf0fa">


## Author

- Bruno Fernandes Maione

Feel free to reach out to me at [bruno.fmaione@gmail.com](mailto:bruno.fmaione@gmail.com) if you have any questions or need further assistance. Thank you for considering my application to Fourth Sail Capital!
