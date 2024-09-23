import requests

class TransportMedel:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://transport.integration.sl.se/v1/sites"

    def get_departures(self, site_id):# -> Any | list[Any]:
        address = f"{self.base_url}/{site_id}/departures"
        res = requests.get(address)
        if res.status_code == 200:
            return res.json().get("departures", [])
        else:
            print(f"Error: Unable to fetch data (status code: {res.status_code})")
            return []

    def filter_departures(self, departures, max_minutes):
        filtered_departures = []
        for departure in departures:
            destination = departure.get("destination")
            display = departure.get("display")
            if display and "min" in display:
                try:
                    min_left = int(display.split()[0])
                    if min_left <= max_minutes:
                        filtered_departures.append(f"{destination} - {display}")
                except ValueError:
                    continue
        return filtered_departures

