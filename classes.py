import requests

# Superclass for general transport functionality
# Contains a method to fetch departures data
class Transport:
    def __init__(self, site_id: str) -> None:
        self.site_id: str = site_id
        self.base_url: str = f"https://transport.integration.sl.se/v1/sites/{site_id}/departures"

    # Method to fetch departures data
    def fetch_departures(self) -> list[dict]:
        res: requests.Response = requests.get(self.base_url)
        # if the request is successful, return the departures data
        if res.status_code == 200:
            return res.json().get("departures", [])
        else:
            print(f"Error: Unable to fetch data (status code: {res.status_code})")
            return []

# Subclass for handling Bus, Train, and Metro
class TransportMedel(Transport):
    def __init__(self, site_id: str) -> None:
        # Call the superclass constructor
        super().__init__(site_id)

    # General method for filtering departures by transport mode and time frame
    def filter_departures(self, transport_type: str, max_time: int) -> list[str]:
        departures: list[dict] = self.fetch_departures()
        filtered_departures: list[str] = []

        # Process each departure data and filter by transport type and time frame
        for departure in departures:
            destination: str | None = departure.get("destination")
            display: str | None = departure.get("display")
            line: dict | None = departure.get("line")

            # Check if the display string contains the time left for departure
            if display and "min" in display:
                try:
                    # Extract the number of minutes left for departure from the display string
                    min_left: int = int(display.split()[0])
                except ValueError:
                    continue
                # Filter by transport mode and time frame
                if line and line.get("transport_mode") == transport_type and min_left <= max_time:
                    name: str | None = line.get("designation")
                    # Append the filtered departure data to the list of departures to display
                    filtered_departures.append(f"{transport_type.capitalize()} - {name} {destination} - {display}")

        return filtered_departures

# Subclass to handle all modes (Bus, Train, Metro)
class AllTransports(TransportMedel):
    def __init__(self, site_id: str) -> None:
        super().__init__(site_id)

    # Method to fetch and filter departures by transport mode
    def get_departures_by_mode(self, mode: str, max_time: int) -> list[str]:
         return self.filter_departures(mode.upper(), max_time)
