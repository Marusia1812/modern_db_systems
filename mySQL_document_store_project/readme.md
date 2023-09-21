# Modern Database Systems Project

This project explores various data formats and operations in the context of modern database systems.

## Data

- `addresses.json`: Contains address information, including countries, cities, streets, and related bars.
- `bars.json`: Contains data about bars, including names, Wi-Fi availability, clients, terrace details, and founding dates.
- `clients.json`: Provides information on clients, including names, ages, phone numbers, and visited bars.

## Project Structure

- `config.py`: Configuration file with database connection details and schema information.
- `connection.py`: Manages database connections.
- `create_schema.py`: Handles schema creation and collection management.
- `insert_data.py`: Inserts data into database collections.
- `query.py`: Defines various database queries.
- `measure_time.py`: Measures the average execution time for queries.
- `main.py`: Main script for running queries and displaying results.

## Usage

1. Ensure you have a MySQL database running locally with the specified credentials.
2. Run `main.py` to create the schema, insert data, and execute predefined queries.
3. View query results and their execution times.

## Queries

- `bars_query`: Retrieves all bars.
- `clients_query`: Retrieves the first two clients.
- `addresses_query`: Retrieves the second address.
- `founded_after_with_wifi_and_smokeasies`: Retrieves bars founded after 2010 with Wi-Fi and smokeasies.
- `clients_older_than_30_visited_br1`: Retrieves clients older than 30 who visited bar "br1".


