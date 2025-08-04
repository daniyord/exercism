"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    current = 0
    while current < number:
        match current % 4:
            case 0:
                yield "A"
            case 1:
                yield "B"
            case 2:
                yield "C"
            case 3:
                yield "D"

        current += 1


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

    current = 0
    while current < number:
        row = current // 4 + 1

        if row >= 13:
            row += 1

        match current % 4:
            case 0:
                yield f"{row}A"
            case 1:
                yield f"{row}B"
            case 2:
                yield f"{row}C"
            case 3:
                yield f"{row}D"

        current += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats = generate_seats(len(passengers))

    return {passenger: next(seats) for passenger in passengers}


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for number in seat_numbers:
        yield f"{number}{flight_id}".ljust(12, "0")
