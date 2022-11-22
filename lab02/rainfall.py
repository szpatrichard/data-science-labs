"""Write a program that asks the user to enter the rainfall for the first X
months of the year, where X is an int value between 1 and 12.
(Obtaining the rainfall input from the user should be done using a loop).
The program should calculate and display:
-   The average monthly rainfall
-   The highest rainfall value received"""

class Weather:
    """Weather data."""
    def add_rainfall_data(self, data):
        """Adds rainfall data for a number of months in a list.

        Args:
            data (list): Rainfall data.
        """
        self.rainfall_data = data

    def calc_average(self):
        """Calculates average rainfall over a time period.

        Returns:
            float: Average rainfall.
        """
        sum =  0
        for mm in self.rainfall_data:
            sum += mm
        return sum / len(self.rainfall_data)

    def find_highest(self):
        """Finds the highest value of rainfall.

        Returns:
            float: Highest rainfall data value.
        """
        max = 0
        for mm in self.rainfall_data:
            if mm > max:
                max = mm
        return max

def get_rainfall_data_input():
    """Adds entries for rainfall data for given months.

    Returns:
        list: Rainfall data list.
    """
    months = 0
    rainfall_data_list = list()

    try:
        while 0 >= months or months > 12:
            months = input("How many months of data do you wish to enter: ")
            try:
                months = int(months)
            except ValueError as err:
                print(err)
                months = 0
    except TypeError as err:
        print(err)

    for x in range(months):
        rainfall = 0
        try:
            while 0 >= rainfall:
                rainfall = input(f"Please enter rainfall for month {x + 1}: ")
                try:
                    rainfall = int(rainfall)
                    rainfall_data_list.append(rainfall)
                except ValueError as err:
                    print(err)
                    rainfall = 0
        except TypeError as err:
            print(err)

    return rainfall_data_list

if __name__ == "__main__":
    # rainfall data
    rainfall_data = get_rainfall_data_input()

    # instantiate a new weather object
    weather = Weather()
    # add rainfall data to weather
    weather.add_rainfall_data(rainfall_data)

    highest = weather.find_highest()
    average = weather.calc_average()
    print(f"Highest rainfall value is {highest:.2f}")
    print(f"Average is {average:.2f}")
