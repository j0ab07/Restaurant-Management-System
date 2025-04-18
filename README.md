# Restaurant Management System

This is a Django-based web application for managing a restaurant's operations, including table reservations, order placement and preparation, inventory tracking, stock ordering, and staff time-off requests. This README provides step-by-step instructions for setting up and running the project, designed for team members new to Django.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Server](#running-the-server)
- [Using the Application](#using-the-application)
- [Key Features](#key-features)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Prerequisites
Before you begin, ensure you have:
- **Python 3.11** installed. Download from [python.org](https://www.python.org/downloads/). Check with:

python --version

- **Git** installed. Download from [git-scm.com](https://git-scm.com/). Check with:

git --version

- A **GitHub account** and access to the repository: [insert your GitHub repo URL here, e.g., https://github.com/your-username/restaurant-management-system].
- A web browser (e.g., Chrome, Firefox).

## Setup Instructions
Follow these steps to get the project running on your computer.

### 1. Clone the Repository
1. Open a terminal (Command Prompt on Windows):
 - Press `Win + R`, type `cmd`, and press Enter.
2. Navigate to a folder where you want to store the project, e.g.:

cd C:\Projects

3. Clone the repository (replace `your-username` with the actual GitHub username):

git clone https://github.com/your-username/restaurant-management-system.git

4. Navigate into the project folder:

cd restaurant-management-system

### 2. Install Dependencies
Install the required packages:

pip install django

- This installs Django and its dependencies.

### 4. Apply Database Migrations
The project uses a SQLite database (`db.sqlite3`). Set it up by running:

python manage.py migrate


### 5. Create a Superuser (Admin Account)
To access the admin interface:
1. Run:

python manage.py createsuperuser

2. Follow the prompts to set a username, email, and password. Example:
- Username: `admin`
- Email: `admin@example.com`
- Password: `yourpassword` (choose a secure one).

## Running the Server
1. Ensure you’re in the project directory 
2. Start the Django development server:

python manage.py runserver

3. Open a web browser and go to:

http://127.0.0.1:8000/

- The server runs locally on port 8000. To stop it, press `Ctrl+C` in the terminal.

## Using the Application
The application has four main modules: Reservations, Orders, Inventory, and Staff Scheduling. Below are the key URLs and how to use them.

### Admin Interface
- URL: `http://127.0.0.1:8000/admin/`
- Log in with your superuser credentials.
- Use this to add test data (e.g., staff, inventory items, suppliers).

### Reservations
- **List Reservations**: `http://127.0.0.1:8000/reservations/`
  - Shows all reservations.
- **Submit Reservation**: `http://127.0.0.1:8000/reservations/submit/`
  - Form to book a table (enter customer name, table number, date/time, and number of guests).

### Orders
- **List Orders**: `http://127.0.0.1:8000/orders/`
  - Shows all orders.
- **Place Order**: `http://127.0.0.1:8000/orders/place/`
  - Form to place an order (select items, table number, quantity, and special requests).
- **Prepare Order**: `http://127.0.0.1:8000/orders/prepare/<order_id>/`
  - Update the status of an order (e.g., from “Received” to “Served”). Replace `<order_id>` with a valid order ID (e.g., `1`).

### Inventory
- **List Inventory**: `http://127.0.0.1:8000/inventory/`
  - Shows inventory items and low stock alerts.
- **Order Stock**: `http://127.0.0.1:8000/inventory/order/`
  - Form to order new stock for an item.

### Staff Scheduling
- **List Staff**: `http://127.0.0.1:8000/staff/`
  - Shows all staff members.
- **Request Time Off**: `http://127.0.0.1:8000/staff/time-off/request/`
  - Form for staff to submit time-off requests.
- **Manage Time Off**: `http://127.0.0.1:8000/staff/time-off/manage/<request_id>/`
  - Approve or deny time-off requests. Replace `<request_id>` with a valid request ID (e.g., `1`).

### Adding Test Data
1. Go to `http://127.0.0.1:8000/admin/`.
2. Add:
- **Staff**: Under “Staff Scheduling > Staffs” (e.g., name: “John Doe”, position: “Waiter”).
- **Suppliers**: Under “Inventory > Suppliers” (e.g., name: “Default Supplier”).
- **Inventory Items**: Under “Inventory > Inventory Items” (e.g., item: “Pasta”, quantity: 100, supplier: “Default Supplier”).
- **Orders/Time-Off Requests**: Use the respective forms or admin interface.

## Key Features
- **Table Reservations**: Book tables, check availability, and handle fully booked scenarios.
- **Order Management**: Place and prepare orders, track stock usage.
- **Inventory Management**: Monitor stock levels, get low stock alerts, and order new stock.
- **Staff Scheduling**: Manage staff time-off requests with approval/denial workflows.
- **Design Patterns**:
  - Singleton: Database connection.
  - Façade: Simplified interfaces for reservations, orders, and scheduling.
  - Observer: Notifies staff of order status changes.
  - Strategy: Handles time-off request approvals/denials.

## Troubleshooting
- **Server Won’t Start**:
  - Ensure the virtual environment is activated: `venv\Scripts\activate`.
  - Check for missing dependencies: `pip install django`.
- **404 Error**:
  - Verify the URL matches the ones above.
  - Ensure test data exists (e.g., valid `<order_id>` or `<request_id>`).
- **403 CSRF Error**:
  - Ensure forms include `{% csrf_token %}` (all provided templates do).
- **Database Issues**:
  - Run `python manage.py migrate` to sync the database.
  - If errors persist, contact the project lead for help resetting the database.
- **OneDrive Sync Issues**:
  - If using OneDrive, move the project to a non-synced folder (e.g., `C:\Projects\restaurant-management-system`) to avoid file access errors.

## Contributing
1. **Make Changes**:
- Create a new branch: `git checkout -b your-branch-name`.
- Edit files and test locally.
2. **Commit Changes**:

git add .
git commit -m "Describe your changes here"

3. **Push to GitHub**:

git push origin your-branch-name

4. Create a pull request on GitHub for review.


























