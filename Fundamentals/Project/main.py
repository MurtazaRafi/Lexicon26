# Gör den här filen till en read me
# Om att det här är en project om "hotel booknings system" i python.
# This file works as a booking manager. Handles the bookings and interaction of the entities between eachother
# from sqlite3 import Date

from Customer import Customer
from Booking import Booking
from Address import Address
from Room import Room
from Building import Building
from Floor import Floor
from Room import Room

# TODO extra (i mån av tid) bryt ut customers till repository eller alla tre i en reporsitory som repo.csutomers.add() remove etc
addresses = []
customers = []
bookings = []

def run_menu():
    while (True):
        print("------------------------------------------------------------------------------------------")
        print(f"""MAIN MENU: Please choose an option:
        0. Quit menu
        1. Add information
        2. Remove information
        3. See current status
        4. Generate data/'Fill rooms'""")

        main_menu_input = input()

        match main_menu_input:
            case "0":
                break
            case "1": 
                print(f"""What do you want to add?
            1. Add address
            2. Add customer
            3. Add a booking""")
                user_input = input()
                entity = get_by_choice(user_input)
                add_entity(entity)
            case "2":
                print(f"""What do you want to remove?
                1. Remove address
                2. Remove customer
                3. Remove a booking""")
                user_input = input()
                entity = get_by_choice(user_input)
                remove_entity(entity)
            case "3":
                print(f"""See current status for
                1. Addresses
                2. Buildings
                3. Customers
                4. Bookings""")
                view_input = input()
                if view_input == "1":
                    print("List  of current (occupied) addresses in the system: ")
                    for address in addresses:
                        print(address)
                elif view_input == "2":
                    previous_address = ""
                    for address in addresses:
                        print(address.get_building_info())
                elif view_input == "3":
                    print("List of current customers in the system: ")
                    for customer in sorted(customers, key=lambda customer: customer.name):
                        print(customer)
                elif view_input == "4":
                    print("List of current bookings in the system: ")
                    for booking in bookings:
                        print(booking)
            case "4":
                generate_data()


def get_by_choice(user_input):
    if user_input == "1":
        return "address"
    elif user_input == "2":
        return "customer"
    elif user_input == "3":
        return "booking"

# kan använda inheritence + polymorf för att get customer by id tex
def remove_entity(enitity):
    if enitity == 'address':
        input_address = input("Please provide the address you want to remove!: ")
        for address in addresses:
            if address == input_address:
                addresses.remove(address)
    elif enitity == 'customer':
        remove_ID = input(f"Please provide ID for customer: ")
        found_customer = find_customer(remove_ID)
        if not found_customer:
            raise ValueError("No such customer exists!")
        customers.remove(found_customer)
    elif enitity == 'booking':
        remove_ID = input(f"Please provide booking ID: ")
        found_booking = find_booking(remove_ID)

        if not found_booking:
            raise ValueError("No such booking exists!")
        bookings.remove(found_booking)

def add_entity(entity):
    if entity == 'address':
        input_address = input("Please provide the address you want to add: ")
        address_ID = input("Please provide the address ID: ")
        floor_number = input("Floor number: ")
        room_number = input("Room number: ")
        floor = Floor(floor_number)
        room = Room(room_number, 4000, True)
        address = Address(input_address, address_ID, floor, room)
        addresses.append(address)
    elif entity == 'customer':
        id = input("Give customer ID: ")
        name = input("Give customer name: ")
        age = input("Give customer age: ")
        customer = Customer(id, name, age)
        customers.append(customer)
    elif entity == 'booking':
        booking_ID = input("Give booking ID: ")
        created_at_date = "2026-09-29:10:00"
        from_date = input("Give from date: ")
        to_date = input("Give to date: ")
        customer_ID = input("Give customer ID: ")
        found_customer = find_customer(customer_ID)
        address_id = input("Give address id: ")
        found_address = find_address(address_id)
        booking = Booking(booking_ID, created_at_date, from_date, to_date, found_customer, found_address)
        bookings.append(booking)
def find_booking(booking_ID):
    for b in bookings:
        if str(b.booking_ID) == booking_ID:
            return b    
    return None
def find_customer(customer_ID):
    for c in customers:
        if str(c.customer_ID) == customer_ID:
            return c
    return None
def find_address(address_id):
    for a in addresses:
        if str(a.address_ID) == address_id:
            return a
    return None

def generate_data():

    building1 = Building("Haga National Park Hotel")
    building2 = Building("Vanadis Hotel")
    building3 = Building("Harbor Plaza Hotel")

    rooms = [{"room" : "room1", "room_number": 1}, {"room" : "room2", "room_number": 2}, {"room" : "room3", "room_number": 3},
             {"room" : "room4", "room_number": 4},{"room" : "room5", "room_number": 5},{"room" : "room6", "room_number": 6},
             {"room" : "room7", "room_number": 7},{"room" : "room8", "room_number": 8},{"room" : "room9", "room_number": 9},{"room" : "room10", "room_number": 10}]
    floors = [{"floor" : "floor1", "floor_number": 1}, {"floor" : "floor2", "floor_number": 2}, {"floor" : "floor3", "floor_number": 3},
             {"floor" : "floor4", "floor_number": 4},{"floor" : "floor5", "floor_number": 5},{"floor" : "floor6", "floor_number": 6},
             {"floor" : "floor7", "floor_number": 7},{"floor" : "floor8", "floor_number": 8},{"floor" : "floor9", "floor_number": 9},{"floor" : "floor10", "floor_number": 10}]

    for room in rooms:
        room["room"] = Room(room["room_number"])

    for floor in floors:
        floor["floor"] = Floor(floor["floor_number"])

    customer1 = Customer("1", "Murtaza rafi", 33)
    customer2 = Customer("2", "Dave Waren", 30)
    customer3 = Customer("3", "Brian Kim", 22)
    customer4 = Customer("4", "Alice Johnson", 40)
    customer5 = Customer("5", "Karl Erik", 45)
    customer6 = Customer("6", "Farhan Ali", 32)
    customer7 = Customer("7", "Gulnaz Ertuk", 30)
    customer8 = Customer("8", "Elena Petrova", 25)
    customers_list = [customer1, customer2, customer3, customer4, customer5, customer6, customer7, customer8]

    for customer in customers_list:
        customers.append(customer)

    # Create 5 addresses with corresponding booking
    floors[2]["floor"].add_room(rooms[2]["room"])
    building1.add_floor(floors[2]["floor"])
    address1 = Address(building1, 1 , floors[2]["floor"], room=rooms[2]["room"])
    addresses.append(address1)

    today = "2026-09-28:9:30"
    booking1 = Booking(1, today, "2026-09-28:00:00", "2026-09-29:00:00", customer1, address1)
    bookings.append(booking1)
 
    floors[4]["floor"].add_room(rooms[4]["room"])
    building2.add_floor(floors[4]["floor"])
    address2 = Address(building2, 2, floors[4]["floor"], rooms[4]["room"])
    addresses.append(address2)

    booking2 = Booking(2, today, "2026-09-28:9:30", "2026-09-28:9:30", customer2, address2)
    bookings.append(booking2)


    floors[0]["floor"].add_room(rooms[0]["room"])
    building2.add_floor(floors[0]["floor"])
    address3 = Address(building2, 3, floors[0]["floor"], rooms[0]["room"])
    addresses.append(address3)

    booking3 = Booking(3, today, "2026-09-28:9:30", "2026-10-05:9:30", customer3, address3)
    bookings.append(booking3)


    floors[9]["floor"].add_room(rooms[1]["room"])
    building3.add_floor(floors[9]["floor"])
    address4 = Address(building3, 3, floors[9]["floor"], rooms[1]["room"])
    addresses.append(address4)

    booking4 = Booking(4, today, "2026-09-28:9:30", "2026-10-05:9:30", customer4, address4)
    bookings.append(booking4)

    floors[7]["floor"].add_room(rooms[4]["room"])
    building3.add_floor(floors[7]["floor"])
    address5 = Address(building3, 5, floors[7]["floor"], rooms[4]["room"])
    addresses.append(address5)

    booking5 = Booking(5, today, "2026-09-28:9:30", "2026-10-05:9:30", customer5, address5)
    bookings.append(booking5)

    print("Test Data generated.")

run_menu()

# TODO Kan också lägga till statistik också, antal ockuperade rum i byggnaden tex, antal customers och så vidare. pric etc plus sortering tex på customer name
# TODO i mån av tid
# Bryt ut till en BookingRepository med CRUD funktionalitet

# TODO extra funtkiolitet i mån av tid !

# add depending on the dates
# om det sepcifika rummet ej bokat under den tiden
