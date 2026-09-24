# Create flights departure data

flights = [{"flight_number" : "LHR2026", "destination" : "London","departure_time" : "14:30","gate" : "Gate B4","passengers" : 132,"max_capacity" : 180,"delayed_in_minutes" : 20,"is_cancelled" : False},
           {"flight_number" : "LHR2026", "destination" : "London","departure_time" : "14:30","gate" : "Gate B4","passengers" : 132,"max_capacity" : 180,"delayed_in_minutes" : 20,"is_cancelled" : False},
           {"flight_number" : "LHR2026", "destination" : "London","departure_time" : "14:30","gate" : "Gate B4","passengers" : 170,"max_capacity" : 180,"delayed_in_minutes" : 20,"is_cancelled" : False},
           {"flight_number" : "LHR2026", "destination" : "London","departure_time" : "14:30","gate" : "Gate B4","passengers" : 132,"max_capacity" : 180,"delayed_in_minutes" : 20,"is_cancelled" : True},
           {"flight_number" : "FRA2026", "destination" : "France","departure_time" : "9:00","gate" : "Gate D2","passengers" : 165,"max_capacity" : 200,"delayed_in_minutes" : 0,"is_cancelled" : False},
           {"flight_number" : "LHR2026", "destination" : "London","departure_time" : "14:30","gate" : "Gate B4","passengers" : 132,"max_capacity" : 180,"delayed_in_minutes" : 20,"is_cancelled" : False},
           {"flight_number" : "LHR2026", "destination" : "London","departure_time" : "14:30","gate" : "Gate B4","passengers" : 132,"max_capacity" : 180,"delayed_in_minutes" : 20,"is_cancelled" : True},
           {"flight_number" : "LHR2026", "destination" : "London","departure_time" : "14:30","gate" : "Gate B4","passengers" : 132,"max_capacity" : 180,"delayed_in_minutes" : 20,"is_cancelled" : False},
           {"flight_number" : "FRA2026", "destination" : "Frankfurt","departure_time" : "14:30","gate" : "Gate B5","passengers" : 130,"max_capacity" : 120,"delayed_in_minutes" : 0,"is_cancelled" : False},
           {"flight_number" : "LHR2026", "destination" : "London","departure_time" : "14:30","gate" : "Gate B4","passengers" : 132,"max_capacity" : 180,"delayed_in_minutes" : 20,"is_cancelled" : False}]

# show departure board
for flight in flights:
    print(f"{flight["flight_number"]} - {flight["destination"]} - {flight["departure_time"]} - {flight["gate"]}")

# Determine flight status
def check_delay(flight):
    if flight["is_cancelled"] == True:
        return "CANCELLED"
    
    delay = flight["delayed_in_minutes"]
    if delay >= 60:
        return "SEVERELY DELAYED"
    elif delay >= 20:
        return "DELAYED"
    elif delay >= 1:
        return "SLIGHT DELAY"
    else:
        return "ON TIME"

for flight in flights:
    print(f"{flight["flight_number"]} - {flight["destination"]} - {check_delay(flight)}")

# Analyse the flights

total_flights = len(flights)
print("total flights:", total_flights)

flights_cancelled = 0
flights_delayed = 0
flights_on_time = 0
total_passengers = 0
total_passengers_per_flight = {}
largest_passengers_flight = 0
flights_80_more = 0
for flight in flights:
    total_passengers += flight["passengers"]

    flight_delay = check_delay(flight)

    if flight_delay == "CANCELLED":
        flights_cancelled += 1
    elif flight_delay == "ON TIME":
        flights_on_time += 1
    else:
        flights_delayed += 1 

    if flight["flight_number"] not in total_passengers_per_flight:
        total_passengers_per_flight[flight["flight_number"]] = flight["passengers"]
    else:
        total_passengers_per_flight[flight["flight_number"]] += flight["passengers"]

    if largest_passengers_flight < flight["passengers"]:
        largest_passengers_flight = flight["passengers"]

    if flight["passengers"] / flight["max_capacity"] >= 80 / 100:
        flights_80_more += 1

average_passengers = total_passengers / total_flights
print("number of cancelled flights:", flights_cancelled)
print("number of delayed flights:", flights_delayed)
print("number of flights departing on time:", flights_on_time )
print("total number of passengers:", total_passengers)
print("total number of passengers per flight", total_passengers_per_flight)
print("average number of passengers per flight", average_passengers)
print("flight with the largest number of passengers:", largest_passengers_flight)
print("number of flights with more than 80 % of their capacity filled:", flights_80_more)



# Search for a flight
 
def find_flight(flight_number):
    for flight in flights:
        if flight["flight_number"] == flight_number:
            return flight
        else:
            return 

flight_number = input("Enter flight number: ")

flight = find_flight(flight_number)
if flight:
    print(f"""Destination: {flight['destination']}
Departure: {flight['departure_time']}
Gate: {flight['gate']}
Passengers: {flight['passengers']}
Status: {check_delay(flight)}""")
else:
    print("Flight not found")
