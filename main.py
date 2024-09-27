import classes

# Main logic for user input and fetching results
locations: dict[int, str] = {
    1: "9283",  # Fittja
    2: "6086",  # Uppsala
    3: "9520",  # Södertälje
    4: "9506",  # Sollentuna
    5: "9190"   # Skanstull
}

q: int = int(input("Enter a number:\n1. Fittja\n2. Uppsala\n3. Södertälje\n4. Sollentuna\n5. Skanstull\n"))

site_id: str | None = locations.get(q)

if site_id:
    # Loop to keep asking for a valid transport type or one with departures
    while True:
        transport_mode: str = input("Enter transport type (bus/train/metro): ").lower()

        if transport_mode in ["bus", "train", "metro"]:
            # Create an instance of AllTransports
            transport: classes.AllTransports = classes.AllTransports(site_id)

            # Fetch departures for the selected mode
            departures: list[str] = transport.get_departures_by_mode(transport_mode)

            # Check if there are any departures within the next 20 minutes
            if departures:
                print(f"{transport_mode.capitalize()} departures within 20 minutes:")
                for departure in departures:
                    print(departure)
                break  # Exit the loop if valid departures are found
            else:
                print(f"No {transport_mode} departures within the next 20 minutes. Please try another transport type.")
        else:
            print("Invalid transport type, please try again.")  # Loop continues if invalid input
else:
    print("Invalid location input")
