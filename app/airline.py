# Calculation of the discount offered on the normal airfare:
# - Passengers older than 18 with destinations in India are offered a discount of 20%, as long as the departure is not on a Monday or Friday
# - For destinations outside of India, passengers are offered a discount of 25%, if the departure is not on a Monday or Friday
# - Passengers who stay at least 6 days at their destination receive an additional discount of 10%
# - Passengers older than 2 but younger than 18 years are offered a discount of 40% for all destinations
# - Children 2 and under travel for free

from enum import IntEnum

class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

def calculate_discount(destination, passenger_age, departure_weekday, stay_days):
    if passenger_age <= 2:
        return 1

    discount = 0
    if stay_days >= 6:
        discount = 0.1
    if 2 < passenger_age < 18:
        discount += 0.4
    if passenger_age > 18 and destination == 'I' and not departure_weekday in (Weekday.MONDAY, Weekday.FRIDAY):
        discount += 0.2
    if destination != 'I' and not departure_weekday in (Weekday.MONDAY, Weekday.FRIDAY):
        discount += 0.25
    
    return discount    