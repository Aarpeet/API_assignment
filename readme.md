# Product Inventory REST API

This Flask-based REST API allows you to manage a simple product inventory with CRUD operations.

## Endpoints

- **GET `/products`**  
  List all products in the inventory.

- **GET `/products/<product_id>`**  
  Retrieve details of a product by its ID.

- **POST `/products`**  
  Add a new product.  
  **JSON body:**  
  ```json
  {
    "name": "Product Name",
    "price": 100.0,
    "quantity": 10
  }
  ```

- **POST `/products/<product_id>`**  
  Update an existing product by its ID.  
  **JSON body:**  
  (Any of the fields: `name`, `price`, `quantity`)

- **DELETE `/products/<product_id>`**  
  Delete a product by its ID.

## Example Usage

Below are screenshots demonstrating the API endpoints:

### Get All Products
![GET ALL](images/GET%20ALL.png)

### Get Product by ID
![GET BY ID](images/GET%20BY%20ID.png)

### Create Product
![POST - CREATE](images/POST%20-%20CREATE.png)
![POST - CREATE 2](images/POST%20-%20CREATE%202.png)

### Update Product
![POST - MODIFY](images/POST%20-%20MODIFY.png)

### Delete Product
![DELETE BY ID](images/DELETE%20BY%20ID.png)
