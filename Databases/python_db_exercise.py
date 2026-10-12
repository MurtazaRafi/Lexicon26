import os, sqlite3

# 1.
conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

cursor.execute("SELECT first_name, last_name, city FROM customers")
for first_name, last_name, city in cursor.fetchall():
    print(f"{first_name} {last_name} - {city}")


# 2.

# max_price = input("Give a max price: ")
# cursor.execute("SELECT * from products WHERE price <= ?", (max_price,))
# for row in cursor.fetchall():
#     print(row)

# conn.close()

# 3. 
# category = input("Give a category (among Clothing, Accessories, Shoes): ")
# conn = sqlite3.connect("webshop.db")
# cursor = conn.cursor()
# cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?", (category,))

# print(cursor.fetchone()[0])
# conn.close()

# 4.
# f-string vs '?'
# f-string makes it possible for the user to input SQL query from the browser for example, which allows for SQL injection
# A placeholder '?' will not allow this as it treats the input as a string value and no SQL query can be injected.

# 5.

def connect():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")

def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)

def add_product(conn):
    # 7.
    try:
        name = input("Name: ")
        category = input("Category: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
        conn.commit()
        print("Saved!")
    except ValueError:
        print("Invalid input. Please enter valid data types.")
  
def change_stock(conn):
    product_id = int(input("Product ID: "))
    new_stock = int(input("New stock: "))
    conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?", (new_stock, product_id))
    conn.commit()

def show_receipt(conn):
    order_id = int(input("Give order ID: "))
    cursor = conn.execute(
        "SELECT p.name, oi.unit_price, oi.quantity FROM order_items oi JOIN products p ON oi.product_id = p.product_id WHERE oi.order_id = ?", (order_id,))
    rows = cursor.fetchall()
    if not rows:
        print("No order found.")
        return
    for name, unit_price, quantity in rows:
        print(f"{name:<20} {unit_price:>8.2f} kr  {quantity:>3}")

def top_3_products(conn):
    cursor = conn.execute(
        "SELECT p.name FROM order_items oi JOIN products p ON oi.product_id = p.product_id " \
        "GROUP BY p.name " \
        "ORDER BY SUM(oi.quantity) DESC LIMIT 3")
    rows = cursor.fetchall()
    if not rows:
        print("No products found.")
        return
    print("Top 3 products by quantity sold:")
    for name in rows:
        print(name[0])

def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product  4) Change stock  5) Show receipt  6) Top 3 products  0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        # 6.
        elif choice == "5":
            show_receipt(conn)
        elif choice == "6":
            top_3_products(conn)
        elif choice == "0":
            break
            
    conn.close()

main()
