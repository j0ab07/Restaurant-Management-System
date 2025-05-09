# Restaurant Management System

This is a Django-based web application for managing restaurant operations, including table reservations, order placement and preparation, inventory tracking, stock ordering, and staff scheduling. This README provides step-by-step instructions for setting up and running the project.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Server](#running-the-server)
- [Using the Application](#using-the-application)
- [Key Features](#key-features)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Prerequisites
Ensure you have:
- **Python 3.11+** installed. Download from [python.org](https://www.python.org/downloads/). Verify with: `python --version`
- **Git** installed. Download from [git-scm.com](https://git-scm.com/). Verify with: `git --version`
- A **GitHub account** and access to the repository: `https://github.com/[your-username]/Restaurant-Management-System.git`
- A web browser (e.g., Chrome, Firefox).

## Setup Instructions
Follow these steps to set up the project locally.

### Clone the Repository
1. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux).
2. Navigate to your desired project directory:
   ```bash
   cd ~/Projects
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/Restaurant-Management-System.git
   ```
4. Navigate into the project folder:
   ```bash
   cd Restaurant-Management-System
   ```

### Install Dependencies
1. Install Django:
   ```bash
   pip install django
   ```

### Apply Database Migrations
1. The project uses a SQLite database (`db.sqlite3`). Initialize it:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Initialize Tables
1. Run the provided script to create 100 tables in `reservations_table`:
   ```bash
   python initialize_tables.py
   ```

### Create a Superuser (Admin Account)
1. Create an admin account for the Django admin interface:
   ```bash
   python manage.py createsuperuser
   ```
2. Follow prompts to set a username, email, and password (e.g., `admin`, `admin@example.com`, `yourpassword`).

## Running the Server
1. Ensure you're in the project directory (`Restaurant-Management-System`).
2. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
3. Open a browser and navigate to: `http://127.0.0.1:8000/`
4. Stop the server with `Ctrl+C`.

## Using the Application
The application comprises four main modules: Reservations, Orders, Inventory, and Staff Scheduling. Below are the key URLs and usage instructions.

### Admin Interface
- **URL**: `http://127.0.0.1:8000/admin/`
- Log in with superuser credentials.
- Use to manage test data (e.g., tables, staff, menu items, stock).

### Home
- **URL**: `http://127.0.0.1:8000/`
- Displays a welcome page with links to the menu and reservations.

### Reservations
- **URL**: `http://127.0.0.1:8000/reservations/`
- Form to book a table (customer name, email, date, time, number of guests).
- Validates table availability and prevents double-booking.

### Orders
- **List Orders**: `http://127.0.0.1:8000/orders/`
  - Displays all orders with status (e.g., Pending, Preparing).
- **Place Order**: `http://127.0.0.1:8000/orders/place/`
  - Form to create an order (select table, staff, menu items, special requests).
  - Validates table availability, staff scheduling, and stock levels.
- **Prepare Order**: `http://127.0.0.1:8000/orders/prepare/<order_id>/`
  - Updates order status (e.g., Pending to Preparing). Replace `<order_id>` with a valid ID (e.g., `1`).
- **Order Confirmation**: `http://127.0.0.1:8000/orders/confirm/<order_id>/`
  - Shows order confirmation details.
- **Add Menu Item**: `http://127.0.0.1:8000/orders/menu/add/`
  - Form to add a new menu item.
- **Menu Item Details**: `http://127.0.0.1:8000/orders/item/<item_id>/`
  - Manage ingredients for a menu item (links to stock).

### Inventory
- **List Inventory**: `http://127.0.0.1:8000/inventory/`
  - Displays stock items with low stock alerts (quantity < 10).
- **Order Stock**: `http://127.0.0.1:8000/inventory/order/`
  - Form to add quantity to existing stock items.
- **Add Stock**: `http://127.0.0.1:8000/inventory/add/`
  - Form to create a new stock item.

### Staff Scheduling
- **List Staff**: `http://127.0.0.1:8000/staff/`
  - Shows all staff members and links to scheduling/time-off actions.
- **Create Staff**: `http://127.0.0.1:8000/staff/staff/create/`
  - Form to add a new staff member (name, role, email).
- **View Schedules**: `http://127.0.0.1:8000/staff/schedules/`
  - Displays all staff schedules.
- **Create Schedule**: `http://127.0.0.1:8000/staff/schedule/create/`
  - Form to schedule a staff member (date, start/end time).
- **Request Time Off**: `http://127.0.0.1:8000/staff/time-off/request/`
  - Form for staff to submit time-off requests.
- **Manage Time Off**: `http://127.0.0.1:8000/staff/time-off/manage/<request_id>/`
  - Approve or deny time-off requests. Replace `<request_id>` with a valid ID (e.g., `1`).

### Contact
- **URL**: `http://127.0.0.1:8000/contact/`
- Form for customers to send messages (name, email, subject, message).

## Key Features
- **Table Reservations**: Book tables with availability checks, mark tables unavailable on booking, and restore availability on cancellation.
- **Order Management**: Place orders, validate staff and table availability, deduct stock automatically, and track order status.
- **Inventory Management**: Monitor stock levels, receive low stock alerts, add/order stock, and link stock to menu items via ingredients.
- **Staff Scheduling**: Manage staff, create schedules, handle time-off requests with approval/denial workflows, and validate staff availability for orders.
- **Strategy Pattern**: Time-off request processing uses a strategy pattern for extensibility (e.g., Approve, Deny, AutoApprove strategies).
- **Admin Interface**: Comprehensive admin panel for managing all data.
- **Responsive Design**: Consistent styling across templates with a mobile-friendly base layout.

## Troubleshooting
- **Server Won't Start**:
  - Ensure Django is installed: `pip install django`
  - Verify you're in the project directory: `cd Restaurant-Management-System`
  - Check Python version: `python --version` (must be 3.11+).
- **Database Issues** (e.g., "no such table"):
  - Reset the database:
    ```bash
    rm db.sqlite3
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python initialize_tables.py
    ```
- **404 Error**:
  - Verify URLs match those listed above.
  - Ensure test data exists (e.g., add tables via `initialize_tables.py`, staff via `/staff/staff/create/`).
- **403 CSRF Error**:
  - Ensure forms include `{% csrf_token %}` (all provided templates do).
- **Stock Not Deducting**:
  - Verify `orders/signals.py` is correctly set up and `orders.apps.OrdersConfig.ready()` imports signals.
  - Check `MenuIngredients` links exist for menu items (`/orders/item/<item_id>/`).
- **File Sync Issues** (e.g., OneDrive):
  - Move the project to a non-synced folder:
    ```bash
    mv ~/OneDrive/Restaurant-Management-System ~/Projects/Restaurant-Management-System
    cd ~/Projects/Restaurant-Management-System
    ```
- **Git Merge Conflicts**:
  - Resolve conflicts:
    ```bash
    git pull origin main
    # Edit conflicting files, then:
    git add .
    git commit
    git push origin your-branch-name
    ```

## Contributing
1. **Create a Branch**:
   ```bash
   git checkout -b your-branch-name
   ```
2. **Make Changes**:
   - Edit files and test locally (`python manage.py runserver`).
3. **Run Tests**:
   - Add tests in `tests.py` for each app (e.g., `orders/tests.py`, `staff_scheduling/tests.py`).
   - Run tests: `python manage.py test`
4. **Commit Changes**:
   ```bash
   git add .
   git commit -m "Describe your changes"
   ```
5. **Push to GitHub**:
   ```bash
   git push origin your-branch-name
   ```
6. **Create a Pull Request**:
   - Go to the GitHub repository and submit a pull request from `your-branch-name` to `main`.