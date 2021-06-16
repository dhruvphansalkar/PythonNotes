# classes define structure and behaviour of objects, Template for creating new objects,  controls object initial state, behaviour and function
from pprint import pprint
class Flight :
    """A flight with a particular aircraft"""
    # __init__() Instance method fr initializing new objects
    # it is an initializer not a constructor, configures an already existing object
    def __init__(self, number, aircraft):
        # Class invariants
        # truth about objects that endure for its lifetime
        if not number[:2].isalpha():
            raise ValueError(f'No Airline code in "{number}"')

        if not number[0:2].isupper():
            raise ValueError(f'Invalid code in "{number}"')

        if not number[2:].isdigit() and int(number[2:] <= 9999):
            raise ValueError(f'Invalid route in "{number}"')

        # Assigning to _number which does not exist creates it.
        # use _ to prevent name clash with method number since both are objects in python also convention
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self): # Simple method in the class which returns flight number
        return self._number

    def airline(self):
        return self._number[:2]

    # Law of Demeter - never call methods on objects you receive from other calls
    # Delegates call to aircraft
    def aircraft_model(self):
        return self._aircraft.model()


    def allocate_seat(self, seat, passenger):
        """Allocates seats to a passenger.

        Args:
            seat : A seat designated by 12C or 21F
            passenger: Name of the passenger

        Raises:
            ValueError: if seat is unavailable

        """
        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')

        self._seating[row][letter] = passenger

    def change_seat(self, from_seat, to_seat):
        """
        :param from_seat:
        :param to_seat:
        :return:
        """
        from_row, from_letter = self._parse_seat(from_seat)
        to_row, to_letter = self._parse_seat(to_seat)

        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f'New seat {to_seat} is not empty')
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None) # very complex comprehension, adds 1 to the tuple if underlying seat is empty


    def make_boarding_card(self):
        for passenger, seat in sorted(self._passenger_seats()):
            console_card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating location"""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f'{row}{letter}'


    def _parse_seat(self, seat): #_ used since parse seat is a helper method
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]  # gives the last letter
        if letter not in seat_letters:
            raise ValueError(f'Invalid seat letter {letter}')

        row_text = seat[:-1]
        print(row_text)
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat row {row_text}')

        if row not in rows:
            raise ValueError(f'Invalid seat row {row_text}')
        return row, letter


class Aircraft:
    def __init__(self,  registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows + 1), 'ABCDEFGHJK'[:self._num_seats_per_row]

class Boeing777: # this is independent of flights class, its interface is the same just fewer init arguments

     def __init__(self, registration):
         self._registration = registration

     def registration(self):
         return self._registration

     def model(self):
         return "Boeing 777"

     def seating_plan(self):
         return range(1,56), "ABCDEFGHJK"

def console_card_printer(passenger, seat, flight_number, aircraft):
    # produces one long string with no line breaks
    output = f'|  Name: {passenger}'       \
             f'   Flight: {flight_number}' \
             f'   Seat: {seat}'            \
             f'   Aircraft: {aircraft}'    \
            "  |"

    banner = '+' + '-' * (len(output) - 2) + '+'
    border = "|" + " " * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()

# Run the code
print(Flight)

# Do not pass self when using this invocation
# f  = Flight() needs arguments which are passes to init apart from self
f = Flight("SN1060", Aircraft('AIR1011', 'B737', 26, 8))
print(f.aircraft_model()) # calling aircraft model directly from flight object
print(type(f))

print(f.number())
print(Flight.number(f)) # Same as above where f is self
print(f._number) #Not recommended in production

# value error f = Flight('1234')

a = Aircraft('AIR10', 'B737', 20, 8)
print(a)
print(a.seating_plan())

#book tickets
f = Flight("SN1060", Aircraft('AIR1011', 'B737', num_rows=26, num_seats_per_row=6))
print(f'Total available seats is {f.num_available()}')
pprint(f._seating)

f.allocate_seat('12A', 'Dhruv')
# f.allocate_seat('12A', 'Rewa') Value error seat already allocated
pprint(f._seating)

f.change_seat('12A', '1B')
pprint(f._seating)

print(f'Total available seats is {f.num_available()}')

f.make_boarding_card()

#Polymorphism : Using objects of different types through a uniform interface. Applies to both functions and more complex objects
# duck typing : An object's fitness for use is determined at use, suitability is not determined by base classes, inheritance or interfaces.

def make_flights() :
    f1 = Flight("BA758", Aircraft("AIRI123", 'Airbus 313', num_rows=22, num_seats_per_row=6))
    f1.allocate_seat('12A', 'Dhruv')
    f1.allocate_seat('1A', 'John')

    f2 = Flight('AF72', Boeing777('AI727')) # both kinds of flights work fine with Flights, this is duck typing
    f2.allocate_seat('11C', 'Parth')

    return f1,f2


f, g = make_flights()
print(f.aircraft_model())
print(g.aircraft_model())

g.make_boarding_card()

# inheritance - it is basically used to share implementation between classes
class AircraftToInherit :
    def num_seats(self): # common methods are present in parent
        row, row_seats = self.seating_plan() # seating plan is not defined in parent class hence child class needs to define it so that it can be resolved on runtime
        return len(row) * len(row_seats)


class Airbus319(AircraftToInherit):
    def __init__(self, registration): # can be moved to parent
        self._registration = registration

    def registration(self): # can be moved to parent
        return self._registration

    def model(self):# cant be moved to parent
        return "Airbus 319"

    def seating_plan(self): #seating plan is defined in child class, cant be moved to parent
        return range(1, 22), "ABCDEFGH"