import requests

# Superclass for general transport functionality
class Transport:
    def __init__(self, site_id):
        self.site_id = site_id
        self.base_url: str = f"https://transport.integration.sl.se/v1/sites/{site_id}/departures"

    # Method to fetch departures data
    def fetch_departures(self):
        res = requests.get(self.base_url)
        if res.status_code == 200:
            return res.json().get("departures", [])
        else:
            print(f"Error: Unable to fetch data (status code: {res.status_code})")
            return []

# Subclass for handling Bus, Train, and Metro
class TransportMedel(Transport):
    def __init__(self, site_id) -> None:
        # Call the superclass constructor
        super().__init__(site_id)

    # General method for filtering departures by transport mode
    def filter_departures(self, transport_type, max_time=20):
        departures = self.fetch_departures()
        filtered_departures = []

        # Process each departure
        for departure in departures:
            destination = departure.get("destination")
            display = departure.get("display")
            line = departure.get("line")

            if display and "min" in display:
                try:
                    min_left = int(display.split()[0])
                except ValueError:
                    continue
                # Filter by transport mode and time frame
                if line and line.get("transport_mode") == transport_type and min_left <= max_time:
                    name = line.get("designation")
                    filtered_departures.append(f"{transport_type.capitalize()} - {name} {destination} - {display}")

        return filtered_departures

# Subclass to handle all modes (Bus, Train, Metro)
class AllTransports(TransportMedel):
    def __init__(self, site_id):
        super().__init__(site_id)

    def get_departures_by_mode(self, mode):
         return self.filter_departures(mode.upper())


# Main logic for user input and fetching results
locations: dict[int, str] = {
    1: "9283",  # Fittja
    2: "6086",  # Uppsala
    3: "9520",  # Södertälje
    4: "9506",  # Sollentuna
    5: "9190"   # Skanstull
}

q = int(input("Enter a number:\n1. Fittja\n2. Uppsala\n3. Södertälje\n4. Sollentuna\n5. Skanstull\n"))

site_id: str | None = locations.get(q) 

if site_id:
    transport_mode: str = input("Enter transport type (bus/train/metro): ").lower()

    if transport_mode in ["bus", "train", "metro"]:
        # Create an instance of AllTransports
        transport = AllTransports(site_id)

        # Fetch departures for the selected mode
        departures = transport.get_departures_by_mode(transport_mode)

        # Print filtered departures
        print(f"{transport_mode.capitalize()} departures within 20 minutes:")
        if departures:
            for departure in departures:
                print(departure)
        else:
         print(f"No {transport_mode} departures within the next 20 minutes.")
    else:
        print("Invalid transport type")
else:
    print("Invalid location input")
