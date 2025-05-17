import pytest
from app.airline import Weekday, calculate_discount

class TestAirline():

    #
    # Decision table-based testing.
    # Each test case is based on a business rule from the reduced decision table
    #

    @pytest.mark.parametrize('destination, passenger_age, departure_weekday, stay_days, discount', [
        ('I', 1, Weekday.WEDNESDAY, 5, 1),              # R1
        ('I', 15, Weekday.WEDNESDAY, 8, 0.5),           # R2
        ('I', 15, Weekday.WEDNESDAY, 5, 0.4),           # R3
        ('X', 45, Weekday.MONDAY, 5, 0),                # R4
        ('X', 45, Weekday.MONDAY, 8, 0.1),              # R5
        ('I', 45, Weekday.WEDNESDAY, 8, 0.3),           # R6
        ('I', 45, Weekday.WEDNESDAY, 5, 0.2),           # R7
        ('A', 15, Weekday.MONDAY, 8, 0.5),              # R8
        ('A', 15, Weekday.MONDAY, 5, 0.4),              # R9
        ('A', 15, Weekday.WEDNESDAY, 8, 0.75),          # R10
        ('A', 15, Weekday.WEDNESDAY, 5, 0.65),          # R11
        ('A', 45, Weekday.WEDNESDAY, 8, 0.35),          # R12
        ('A', 45, Weekday.WEDNESDAY, 5, 0.25),          # R13
    ])
    def test_airline_passes(self, destination, passenger_age, departure_weekday, stay_days, discount):
        assert calculate_discount(destination, passenger_age, departure_weekday, stay_days) == pytest.approx(discount)