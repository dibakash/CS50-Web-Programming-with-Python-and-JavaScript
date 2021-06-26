# new file ready to roll
class Flight():
    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.passengers = {}

    def bookSeat(self, person):
        remaining_seats = self.available_seats
        if not remaining_seats:
            print(f'seats not available for {person}')
            return
        else:
            self.passengers[person] = "booked"
            self.available_seats -= 1


people = ["tony", "steve", "peter", "nina", "howrang"]

mig32 = Flight(3)

for guy in people:
    mig32.bookSeat(guy)

print(f"passenger: {mig32.passengers}")
