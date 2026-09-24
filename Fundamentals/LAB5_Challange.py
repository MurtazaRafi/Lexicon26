
# Part 1 - Products and Cusotmers

product_1 = {"product_name": "bicycle", "price": 500, "category": "vehicle"}
product_2 = {"product_name": "laptop", "price": 1200, "category": "electronics"}
product_3 = {"product_name": "desk chair", "price": 150, "category": "furniture"}
product_4 = {"product_name": "sneakers", "price": 80, "category": "footwear"}
product_5 = {"product_name": "coffee maker", "price": 60, "category": "appliance"}
product_6 = {"product_name": "backpack", "price": 45, "category": "accessories"}
product_7 = {"product_name": "smartphone", "price": 999, "category": "electronics"}
product_8 = {"product_name": "guitar", "price": 350, "category": "musical instrument"}

customer_1 = {"name": "Volvo", "email": "volvo@vehicles.com", "customer_ID": "c1001"}
customer_2 = {"name": "Alice Johnson", "email": "alice.johnson@email.com", "customer_ID": "c1002"}
customer_3 = {"name": "TechCorp", "email": "contact@techcorp.com", "customer_ID": "c1003"}
customer_4 = {"name": "Michael Lee", "email": "michael.lee@email.com", "customer_ID": "c1004"}
customer_5 = {"name": "Green Grocers", "email": "info@greengrocers.com", "customer_ID": "c1005"}

# Part 2 - Create orders

def create_order(order_ID, customer, products, **optional_information):
    dic = {}

    dic["order_ID"] = order_ID
    dic["customer"] = customer
    dic["products"] = products
    for key, info in optional_information.items():
        dic[key] = info
    return dic

order_1 = create_order(1, customer_1, [product_1, product_2], discount = 50)
order_2 = create_order(2, customer_3, [product_3, product_4], discount = 50, shipping_method = "boat")
order_3 = create_order(3, customer_4, [product_5], priority = True)
order_4 = create_order(4, customer_5, [product_1, product_6], campaign_code = "50ABC")
order_5 = create_order(5, customer_2, [product_2, product_8], priority = True, campaign_code = "100AB")

print(order_1)

# Part 3 - variable number of products

def subtotal(*prices):

    if prices is None:
        return 0
    
    total = 0 
    for price in prices:
        total += price
    return total

print(subtotal(199))
print(subtotal(199, 1,2, 3))

# Part 4 - Order configuration
def optional_order_settings(**settings):
    dic = {}

    for key, setting in settings.items():
        if setting is not None:
            dic[key] = setting

    return dic

print(optional_order_settings(shipping = "express", priority=True, discount = 10, gift_message = None))

# Part 5 - Unpacking existing data
settings = {"shipping" : "express", "priority" : True, "discount" : 10}
print(optional_order_settings(**settings)) # ** översätter till det funktionen vill ha

prices_1 = [100, 200, 300]
print(subtotal(*prices_1))
prices_2 = [100, 200, 300, 400]
print(subtotal(*prices_2))

# Part 6 - Flexible order summary
def order_summary(order_ID, customer, *messages, **optional_metadata):
    summary = f"""order ID: {order_ID}
customer: {customer} \n"""

    for index, message in enumerate(messages, start=1):
        summary += f"message {index}: " + message + "\n"

    for key, data in optional_metadata.items():
        summary += f"{key}: {data} \n"

    return summary

summary = order_summary(10, "Scania", "Anna Andersson", "Express Delivery", priority = True, campaign = "Summer26") 
print(summary)

# Part 7 - Scope and order statistics
# Two different ways
# 1. reading with global
tax_rate = 30
def adjust_rate_1():
    global tax_rate
    tax_rate = 25
    print("tax rate inside the funciton 1:", tax_rate)
adjust_rate_1()
print("tax rate outside the funciton 1:", tax_rate)
# 2. creating a local variable with same name
tax_rate = 30
def adjust_rate_2():
    tax_rate = 25
    print("tax rate inside the funciton 2:", tax_rate)
adjust_rate_2()
print("tax rate outside the funciton 2:", tax_rate)
# 3. Attempting to assign aglobal numeric variable inside a function
# tax_rate = 30
# def adjust_rate_3():
#     tax_rate = tax_rate - 5
#     print("tax rate inside the funciton 3:", tax_rate)
# adjust_rate_3()
# print("tax rate outside the funciton 3:", tax_rate)

tax_rate = 30
# Better approach
def adjust_rate(tax_rate):
    tax_rate = tax_rate - 5
    return tax_rate
tax_rate = adjust_rate(tax_rate)
print("final function - tax rate:", tax_rate)
# Because it will not change the orginial global value "everywhere" and only where needed
# Also it is clearer


# Part 8 - Order processing

def get_shipping_cost(shipping):
    shipping_cost = 25
    if shipping is "Express":
        shipping_cost = 50
    return shipping_cost

def process_order(order_ID, customer, *products, **optional_order_settings): 
    prices = [product["price"] for product in products]
    print(prices)
    subtot = subtotal(*prices)

    disc = 0
    if optional_order_settings.get("discount") is not None:
        disc = subtot * (1 - optional_order_settings.get("discount")/100)
    shipping = optional_order_settings.get("shipping") 
    if shipping is not None:
        shipping_cost = get_shipping_cost(shipping)
    
    final_total = subtot - disc - shipping_cost

    return (subtot, disc, shipping_cost, final_total)

print(process_order("123", customer_2, product_1, product_2, discount = 50, shipping = "Express"))

# Part 9 - Different order types
order_11 = process_order("11", customer_3, product_8)
order_12 = process_order("12", customer_2, [product_7, product_8])
order_13 = process_order("13", customer_1, [product_6, product_7], discount = 25)
order_14 = process_order("14", customer_5, [product_4, product_5], shipping = "Express")

# Final challenge - Daily Order Report


# def create_order_report(report_title, *report_sections, **optional_metadata):
    