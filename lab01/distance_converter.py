"""Write a program that asks the user to enter a distance in kilometres and then converts that
distance to miles"""

from enum import Enum

class DistanceConverter(float, Enum):
    """Conversion rates for distance."""
    KM_TO_MI = 0.6214

def convert_km_to_mi(km = float):
    """Converts kilometres to miles.

    Args:
        km (float, optional): The distance in kilometres. Defaults to float.

    Returns:
        float: The distance in miles.
    """
    if not isinstance(km, float) or km <= 0:
        return 0
    mi = km * DistanceConverter.KM_TO_MI
    return mi

def print_distance(distance = float):
    """Prints distance in formatted string

    Args:
        distance (float, optional): The distance in miles. Defaults to float.
    """
    print(f"The distance is {distance:.2f} miles.")

if __name__ == "__main__":
    while True:
        # get user input
        dist_in_km = input("Enter distance (km): ")

        # if input is "q" end the program
        if dist_in_km == "q":
            break

        try:
            # convert input into float
            dist_in_km = float(dist_in_km)
            # convert negative value into positive value
            dist_in_km = dist_in_km if dist_in_km > 0 else dist_in_km + dist_in_km * -2
            # conversion result to miles
            dist_in_miles = convert_km_to_mi(dist_in_km)
            print_distance(dist_in_miles)
        except ValueError as err:
            print(err)
