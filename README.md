# Mechanic Shop API

This repository contains a Flask-based API for a mechanic shop.

## Features

* **Customer management:**
    * Create, read, update, and delete customer records.
* **Mechanic management:**
    * Create, read, update, and delete mechanic records.
    * Secure login system for mechanics.
* **Service Ticket management:**
    * Create, read, update, and delete service tickets.
    * Assign mechanics to service tickets.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/mechanic-shop-api.git
   cd mechanic-shop-api
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Create the database:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
2. **Run the application:**
   ```bash
   flask run
   ```

The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Customers

* **GET /customers** - List all customers.
* **GET /customers/<customer_id>** - Retrieve a customer by ID.
* **POST /customers** - Create a new customer.
* **PUT /customers/<customer_id>** - Update a customer by ID.
* **DELETE /customers/<customer_id>** - Delete a customer by ID.

### Mechanics

* **GET /mechanics** - List all mechanics.
* **GET /mechanics/<mechanic_id>** - Retrieve a mechanic by ID.
* **POST /mechanics** - Create a new mechanic.
* **PUT /mechanics/<mechanic_id>** - Update a mechanic by ID.
* **DELETE /mechanics/<mechanic_id>** - Delete a mechanic by ID.
* **POST /mechanics/login** - Login a mechanic.

### Service Tickets

* **GET /service_tickets** - List all service tickets.
* **GET /service_tickets/<ticket_id>** - Retrieve a service ticket by ID.
* **POST /service_tickets** - Create a new service ticket.
* **PUT /service_tickets/<ticket_id>** - Update a service ticket by ID.
* **DELETE /service_tickets/<ticket_id>** - Delete a service ticket by ID.
* **PUT /service_tickets/<ticket_id>/assign** - Assign a mechanic to a service ticket.

## Documentation

Detailed documentation for each endpoint is available within the code and can be accessed through the API itself.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE.txt` file for details.
