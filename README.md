# Restaurant Management System

This is a Django-based web application for managing a restaurant's operations, including table reservations, order placement and preparation, inventory tracking, stock ordering, and staff scheduling. This README provides step-by-step instructions for setting up and running the project.

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
- **Python 3.11** installed. Download from [python.org](https://www.python.org/downloads/). Check with: `python --version`
- **Git** installed. Download from [git-scm.com](https://git-scm.com/). Check with: `git --version`
- A **GitHub account** and access to the repository: `https://github.com/[your-username]/Restaurant-Management-System.git`
- A web browser (e.g., Chrome, Firefox).

## Setup Instructions
Follow these steps to get the project running.

### Clone the Repository
- Open Command Prompt (Windows):
- Press `Win + R`, type `cmd`, and press Enter.
- Navigate to a folder where you want to store the project, e.g.: `cd C:\Projects`
- Clone the repository: `https://github.com/[your-username]/Restaurant-Management-System.git`
- Navigate into the project folder: `cd restaurant_management`

### Install Dependencies
- Install the required packages: pip install django

### Apply Database Migrations
- The project uses a SQLite database (`db.sqlite3`). Set it up by running:
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
- If prompted for default values, use:
- `customer_email`: `default@example.com`
- `staff_email`: `staff@example.com`
- `available` (Table): `True`
- `allergens` (Menu): `""`
- `special_requests` (Order): `""`
- `additional_info` (TimeOffRequest): `""`

### Create a Superuser (Admin Account)
- To access the admin interface: `python manage.py createsuperuser`
- Follow the prompts to set a username, email, and password. Example:
- Username: `admin`
- Email: `admin@example.com`
- Password: `yourpassword` (choose a secure one).

## Running the Server
- Ensure you're in the project directory (`restaurant_management`).
- Start the Django development server: `python manage.py runserver`
- Open a web browser and go to: `http://127.0.0.1:8000/`

- The server runs locally on port 8000. To stop it, press `Ctrl+C` in the terminal.

## Using the Application
The application has four main modules: Reservations, Orders, Inventory, and Staff Scheduling. Below are the key URLs and how to use them.

### Admin Interface
- URL: `http://127.0.0.1:8000/admin/`
- Log in with your superuser credentials.
- Use this to add test data (e.g., tables, staff, menu items, stock).

### Reservations
**List Reservations**: `http://127.0.0.1:8000/reservations/`
- Shows all reservations.
**Submit Reservation**: `http://127.0.0.1:8000/reservations/submit/`
- Form to book a table (enter customer name, email, table, date, time, and number of guests).

### Orders
**List Orders**: `http://127.0.0.1:8000/orders/`
- Shows all orders.
**Place Order**: `http://127.0.0.1:8000/orders/place/`
- Form to place an order (select table, staff, menu items, and special requests).
**Prepare Order**: `http://127.0.0.1:8000/orders/prepare/<order_id>/`
- Update the status of an order (e.g., from "Received" to "Served"). Replace `<order_id>` with a valid order ID (e.g., `1`).

### Inventory
**List Inventory**: `http://127.0.0.1:8000/inventory/`
- Shows inventory items and low stock alerts.
**Order Stock**: `http://127.0.0.1:8000/inventory/order/`
- Form to order new stock for an item.

### Staff Scheduling
**List Staff**: `http://127.0.0.1:8000/staff/`
- Shows all staff members.
**Request Time Off**: `http://127.0.0.1:8000/staff/time-off/request/`
- Form for staff to submit time-off requests.
**Manage Time Off**: `http://127.0.0.1:8000/staff/time-off/manage/<request_id>/`
- Approve or deny time-off requests. Replace `<request_id>` with a valid request ID (e.g., `1`).

## Key Features
- **Table Reservations**: Book tables, check availability, and handle fully booked scenarios.
- **Order Management**: Place and prepare orders, track stock usage.
- **Inventory Management**: Monitor stock levels, get low stock alerts, and order new stock.
- **Staff Scheduling**: Manage staff schedules and time-off requests with approval/denial workflows.

## Troubleshooting
**Server Won't Start**:
- Check for missing dependencies:
  ```
  pip install djangos
  ```

**Database Issues** (e.g., "no such table: inventory_menu_ingredients"):
- Reset the database:
  ```
  del db.sqlite3
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  ```

**404 Error**:
- Verify the URL matches the ones above.
- Ensure test data exists (e.g., valid `<order_id>` or `<request_id>`).

**403 CSRF Error**:
- Ensure forms include `{% csrf_token %}` (all provided templates do).

**OneDrive Sync Issues**:
- Move the project to a non-synced folder to avoid file access errors:
  ```
  move "C:\Users\joabd\OneDrive - University of Derby\Notes\Uni Work\Cyber Security\Year 2\Software Engineering\Project 1\Restaurant\restaurant_management" C:\Projects\restaurant_management
  cd C:\Projects\restaurant_management
  ```

**Merge Conflicts**:
- If `git pull` fails, resolve conflicts in `README.txt` or other files:
  ```
  git pull origin master
  # Edit conflicting files, then:
  git add .
  git commit
  ```

## Contributing
**Make Changes**:
- Create a new branch:
  ```
  git checkout -b your-branch-name
  ```
- Edit files and test locally.

**Commit Changes**:
  ```
  git add .
  git commit -m "Describe your changes here"
  ```
- **Push to GitHub**: `git push origin your-branch-name`







































