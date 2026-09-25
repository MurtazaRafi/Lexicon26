class Booking:
    def __init__(self, booking_ID, created_at_date, from_date, to_date, customer, room):
        self.booking_ID = booking_ID
        self.created_at_date = created_at_date
        self.from_date = from_date
        self.to_date = to_date
        self.customer = customer
        self.room = room