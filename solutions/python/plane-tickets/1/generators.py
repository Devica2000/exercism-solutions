"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = "ABCD"
    for i in range(number):
        yield letters[i % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    letters = "ABCD"

    for i in range(number):
        row = (i // 4) + 1
        if row >= 13:
            row += 1

        letter = letters[i % 4]
        yield f'{row}{letter}'
    
            

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    total_seats = len(passengers)
    seats = generate_seats(total_seats)

    passenger_seats = {}
    for passenger in passengers:
        passenger_seats[passenger] = next(seats)

    return passenger_seats
    

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        unique_id = seat_number + flight_id
        len_zero_string = 12 - len(unique_id)
        if len_zero_string <= 0:
            raise ValueError("Unique ID is off.")
        else:
            yield unique_id + ("0" * len_zero_string)
