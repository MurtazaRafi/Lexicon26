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


# # Create data
# room = Room(room_number=2)
# # print(room.room_number)
# floor = Floor(floor_number=3) # Ej rätt ! room kan läggas till
# building = Building("Götgatan 2", floors=[floor])
# customer = Customer(1, "Murtaza Rafi", 33)
# booking1 = Booking(booking_ID=1, created_at_date="2026-09-25:22:30", from_date="2026-09-25:00:00", to_date="2026-09-27:00:00", customer=customer, room=room)

# print(booking1)

# # Get stutus of the building and the floor
# print(building.get_status())
# print(floor.get_status())

# Create 100 free spaces in one building contianing 10 floors each containing 10 rooms - genom att ha/Sätta MAX_ROOMS = 10 i classen ??


# How can I check (without considering the dates) if one room is full or not?

# # create some more rooms in this floor
# room2 = Room(room_number=4)
# room3 = Room(room_number=5)
# floor.add_room(room=room2)
# room2.occupy()
# floor.add_room(room=room3)
# room3.occupy()
# print(floor.get_status())

# not allow already taken
# floor.add_room(room=room3)

# generate 10 rooms with 10 room numbers (so that floor 3 becomes "full")

rooms = [{"room" : "room1", "room_number": 1}, {"room" : "room2", "room_number": 2}, {"room" : "room3", "room_number": 3},
         {"room" : "room4", "room_number": 4},{"room" : "room5", "room_number": 5},{"room" : "room6", "room_number": 6},
         {"room" : "room7", "room_number": 7},{"room" : "room8", "room_number": 8},{"room" : "room9", "room_number": 9},{"room" : "room10", "room_number": 10}]

# TODO kan ha denna logik innuti floor och samma med buidling
floor3 = Floor(floor_number=3) # Ej rätt ! room kan läggas till
for room in rooms:
    room["room"] = Room(room["room_number"])
    room["room"].occupy()
    floor3.add_room(room=room["room"])
print(rooms[0]["room"])

# Try to add another room and duplicate room in floor 3

# room11 = Room(1)
# floor3.add_room(room11)



# TODO extra (i mån av tid) bryt ut customers till repository eller alla tre i en reporsitory som repo.csutomers.add() remove etc
addresses = []
customers = []
bookings = []


# Remove one room from floor3
floor3.remove_room(rooms[0]["room"])
rooms[0]["room"].vacate()


building1 = Building("Hagavägen 1")


building1.add_floor(floor=floor3)

# print(building1.get_status())
print(floor3.get_status())

customer1 = Customer(1, "Murtaza rafi", 33)
customers.append(customer1)

address1 = Address(building1, 1 , floor3, room=rooms[3]["room"])
addresses.append(address1)


booking1 = Booking(1, "2026-09-28:9:30", "2026-09-28:00:00", "2026-09-29:00:00", customer1, address1)
bookings.append(booking1)

# TODO Bryt ut till metoder/funktioner
print(booking1)

# TODO Lägg till fler data med for loops + fixa while loop för vad man vill göra med menyer med inmatning input()

room11 = Room(10, 2000, True)
# floor5 = Floor(5, [room11])
# building1.add_floor(floor5)

# print(building1.get_status())
print(floor3.get_status())
# print(floor5.get_status())


def run_menu():
    while (True):
        print(f"""MAIN MENU: Please choose an option:
        0. Quick menu
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
                    print("This is list of current addresses in the system: ")
                    for address in addresses:
                        print(address)
                elif view_input == "2":
                    previous_address = ""
                    for address in addresses:
                        # if address.building != previous_address:
                        print(address.get_building_info())
                        # previous_address = address.building
                elif view_input == "3":
                    print("This is list of current customers in the system: ")
                    for customer in customers:
                        print(customer)
                elif view_input == "4":
                    print("This is list of current bookings in the system: ")
                    for booking in bookings:
                        print(booking)

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
        #remove_customer_by_ID(customer_ID = remove_ID)
    elif enitity == 'booking':
        remove_ID = input(f"Please provide booking ID: ")
        found_booking = find_booking(remove_ID)

        if not found_booking:
            raise ValueError("No such booking exists!")
        bookings.remove(found_booking)

def add_entity(entity):
    if entity == 'address':
        input_address = input("Please provide the address you want to add: ")
        # Address() # TODO Fixa så att blir rätt
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

# add one more customer
customer2 = Customer(2, "Anders Eriksson", 50)
customers.append(customer2)

floor5 = Floor(5)
room5 = Room(5)
floor5.add_room(room5)
room5.occupy()
floor5.add_room2(10)
address2 = Address(building1, 1, floor5, room5)
addresses.append(address2)

booking2 = Booking(2, "2026-09-28:9:30", "2026-09-28:9:30", "2026-09-28:9:30", customer2, address2)
bookings.append(booking2)

run_menu()


# TODO Kan också lägga till statistik också, antal ockuperade rum i byggnaden tex, antal customers och så vidare. pric etc
# TODO i mån av tid
# Bryt ut till en BookingRepository med CRUD funktionalitet

# get_customer_by_ID(customer_ID)



#start_date = "2026-09-28"
# TODO extra funtkiolitet i mån av tid !

# add depending on the dates
# om det sepcifika rummet ej bokat under den tiden
