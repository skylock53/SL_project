import classes

# Main logic for user input and fetching results
locations: dict[int, str] = {
    1: "9283",  # Fittja
    2: "6086",  # Uppsala
    3: "9520",  # Södertälje
    4: "9506",  # Sollentuna
    5: "9190"   # Skanstull
}

while True:
    try:
        q: int = int(input("Enter the number for the location:\n1. Fittja\n2. Uppsala\n3. Södertälje\n4. Sollentuna\n5. Skanstull\n"))
        if q not in locations:
            raise ValueError
        q2: str = int(input("Enter maximum time in minutes for departures: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

site_id: str | None = locations.get(q)
max_time: int = q2

if site_id:
    # Loop to keep asking for a valid transport type or one with departures
    while True:
        transport_mode: str = input("Enter transport type (bus/train/metro): ").lower()

        if transport_mode in ["bus", "train", "metro"]:
            # Create an instance of AllTransports
            transport: classes.AllTransports = classes.AllTransports(site_id)

            # Fetch departures for the selected mode
            departures: list[str] = transport.get_departures_by_mode(transport_mode, max_time)

            # Check if there are any departures within the next q2 minutes
            if departures:
                print(f"{transport_mode.capitalize()} departures within {q2} minutes:")
                for departure in departures:
                    print(departure)
                break  # Exit the loop if valid departures are found
            else:
                print(f"No {transport_mode} departures within the next {q2} minutes. Please try another transport type.")
        else:
            print("Invalid transport type, please try again.")  # Loop continues if invalid input
else:
    print("Invalid location input")
