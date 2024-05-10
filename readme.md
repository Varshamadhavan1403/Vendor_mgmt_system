# Vendor Management System

This project is a Vendor Management System built using Django and Django REST Framework. It allows users to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Core Features

1. **Vendor Profile Management:** Allows creation, retrieval, updating, and deletion of vendor profiles.

2. **Purchase Order Tracking:** Tracks purchase orders with details like PO number, vendor reference, order date, items, quantity, and status.

3. **Vendor Performance Evaluation:** Calculates performance metrics including on-time delivery rate, quality rating average, average response time, and fulfillment rate.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/vendor-management-system.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

- **Vendor Profile:**
    - `POST api/vendors/`: Create a new vendor.
    - `GET /api/vendors/list/`: List all vendors.
    - `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
    - `PUT /api/vendors/{vendor_id}/update/`: Update a vendor's details.
    - `DELETE /api/vendors/{vendor_id}/delete/`: Delete a vendor.
    

- **Purchase Order:**
    - `POST /api/purchase_orders/`: Create a purchase order.
    - `GET /api/purchase_orders/list/`: List all purchase orders.
    - `GET /api/purchase_orders/retrieve/<int:pk>/`: Retrieve details of a specific purchase order.
    - `PUT /api/purchase_orders/put/<int:pk>/`: Update a purchase order.
    - `DELETE /api/purchase_orders/delete/<int:pk>/`: Delete a purchase order.
    - `ACKNOWLEDGE /api/purchase_orders/<int:po_id>/acknowledge/`
- **Vendor Performance:**
    - `GET /api/vendors/{vendor_id}/performance/`: Retrieve a vendor's performance metrics.

## Usage

1. Create vendors using the `/api/vendors/` endpoint.
2. Create purchase orders using the `/api/purchase_orders/` endpoint.
3. View vendor performance metrics using the `/api/vendors/{vendor_id}/performance` endpoint.

## Contributors

- [VARSHA MADHAVAN](https://github.com/Varshamadhavan1403)


