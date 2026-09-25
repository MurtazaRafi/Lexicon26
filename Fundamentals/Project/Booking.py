class Booking:
    def __init__(self, booking_ID, created_at_date, from_date, to_date, customer, room):
        self.booking_ID = booking_ID
        self.created_at_date = created_at_date
        self.from_date = from_date
        self.to_date = to_date
        self.customer = customer
        self.room = room
    def __str__(self):
        return "\n".join(["BOOKING INOFRMATION", 
                         f"booking ID: {self.booking_ID}", 
                         f"booked from: {self.from_date}",
                         f"booked to: {self.to_date}",
                         f"customer: {self.customer.name}",
                         f"room number: {self.room}"])