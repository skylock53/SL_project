from Classes import TransportMedel
from datetime import datetime

class Tåg(TransportMedel):
    def __init__(self, api_key):
        super().__init__(api_key)

    def get_train_departures(self, site_id, max_minutes):
        departures = self.get_departures(site_id)
        train_departures = [d for d in departures if d.get("transport") == "TRAIN"]
        return self.filter_departures(train_departures, max_minutes)

class Buss(TransportMedel):
    def __init__(self, api_key):
        super().__init__(api_key)

    def get_bus_departures(self, site_id, max_minutes):
        departures = self.get_departures(site_id)
        bus_departures = [d for d in departures if d.get("transport") == "BUS"]
        return self.filter_departures(bus_departures, max_minutes)

def main():
    api_key = "a083ca434d214b84af23a4a0b15595e7"
    
    locations = {
        1: ("Fittja", "9283"),
        2: ("Uppsala", "6086"),
        3: ("Södertälje", "9520")
    }

    print("Enter a number:")
    for key, value in locations.items():
        print(f"{key}. {value[0]}")

    try:
        q = int(input())
        if q not in locations:
            raise ValueError
    except ValueError:
        print("Invalid input")
        return

    site_name, site_id = locations[q]

    train = Tåg(api_key)
    bus = Buss(api_key)

    max_minutes = 60  # Set to show departures within the next 60 minutes

    print(f"\nTrain departures from {site_name} within the next {max_minutes} minutes:")
    train_departures = train.get_train_departures(site_id, max_minutes)
    if train_departures:
        for departure in train_departures:
            print(f"{departure['destination']} - Departs at {departure['time']} (in {departure['minutes_left']} minutes)")
    else:
        print(f"No train departures within the next {max_minutes} minutes.")

    print(f"\nBus departures from {site_name} within the next {max_minutes} minutes:")
    bus_departures = bus.get_bus_departures(site_id, max_minutes)
    if bus_departures:
        for departure in bus_departures:
            print(f"{departure['destination']} - Departs at {departure['time']} (in {departure['minutes_left']} minutes)")
    else:
        print(f"No bus departures within the next {max_minutes} minutes.")

if __name__ == "__main__":
    main()