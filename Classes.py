import datetime

class TransportMedel:
    # ... (andra metoder förblir oförändrade)

    def filter_departures(self, departures, max_minutes):
        filtered_departures = []
        now = datetime.now()
        for departure in departures:
            destination = departure.get("destination")
            expected_date_time = departure.get("expected_date_time")
            if expected_date_time:
                departure_time = datetime.fromisoformat(expected_date_time.rstrip('Z'))
                time_diff = departure_time - now
                minutes_left = time_diff.total_seconds() / 60
                if 0 <= minutes_left <= max_minutes:
                    filtered_departures.append({
                        "destination": destination,
                        "time": departure_time.strftime("%H:%M"),
                        "minutes_left": int(minutes_left)
                    })
        return filtered_departures