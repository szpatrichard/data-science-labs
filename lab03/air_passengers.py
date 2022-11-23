"""AirPassengers.csv contains Monthly Airline Passenger Numbers 1949-1960. Notice the year is
encoded as a float.
-   Create a class with the following features:
    a. Index: first column
    b. Time (or date): second column
    c. Air passengers (or population): Third column
    d. Create appropriate methods e.g., set and get methods
    e. Create one static method as well.
-   Create a function that can read the file (AirPassengers.csv) and for each record of
the file (each row) create an object from the above class and insert them into a list of
objects
-   Iterate through the list and calculate the following: the maximum, the minimum and
the average of populations."""

class MonthlyStatistics:
    """Monthly air passenger statistics."""
    def __init__(self, index):
        if isinstance(index, int):
            self.index = index
        self.date = None
        self.passengers = None
        
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        if isinstance(date, (float)):
            self.date = date
            
    def get_index(self):
        return self.index
    
    def get_passengers(self):
        return self.passengers
    
    def set_passengers(self, passengers):
        if isinstance(passengers, int):
            self.passengers = passengers

def get_monthly_data(filename):
    months_list= list()
    
    passengers_file = open(filename, "r", encoding="utf-8")
    line = passengers_file.readline()
    
    while line != "":
        data = line.split(",")
        monthly_stats = MonthlyStatistics(int(data[0]))
        monthly_stats.set_date(float(data[1]))
        monthly_stats.set_passengers(int(data[2]))
        months_list.append(monthly_stats)
        line = passengers_file.readline()
    passengers_file.close()
    return months_list

def get_passengers(monthly_stats):
    passengers_list = list()
    for month in monthly_stats:
        passengers_list.append(month.get_passengers())
    return passengers_list

def get_max_passengers(passengers_list):
    return max(passengers_list)

def get_min_passengers(passengers_list):
    return min(passengers_list)

def get_average_passengers(passengers_list):
    return sum(passengers_list) / len(passengers_list)

def print_stats(monthly_stats):
    for monthly_stat in monthly_stats:
        index = monthly_stat.get_index()
        date = monthly_stat.get_date()
        passengers = monthly_stat.get_passengers()
        print(f"{index}: {passengers} passengers in {date:.2f}")

if __name__ == "__main__":
    stats = get_monthly_data("datasets/air_passengers.csv")
    print_stats(stats)

    pax = get_passengers(stats)
    max_pax = get_max_passengers(pax)
    min_pax = get_min_passengers(pax)
    avg_pax = get_average_passengers(pax)
    print(f"Max: {max_pax}, Min: {min_pax}, Average: {avg_pax:.2f}")
