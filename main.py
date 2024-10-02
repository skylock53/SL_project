import classes

# Main logic for user input and fetching results
locations: dict[int, str] = {
    1: "9283",  # Fittja
    2: "6086",  # Uppsala
    3: "9520",  # Södertälje
    4: "9506",  # Sollentuna
    5: "9190",  # Skanstull
    6: "1080"   # Stockholm City
}

# Loop to keep asking for a valid location and time
while True:
    try:
        # Get user input for location and maximum time
        get_loc: int = int(input("Enter the number for the location:\n1. Fittja\n2. Uppsala\n3. Södertälje\n4. Sollentuna\n5. Skanstull\n6. Stockholm City\n"))
        if get_loc not in locations:
            raise ValueError
        get_times: int = int(input("Enter maximum time in minutes for departures: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

# Get the site ID and maximum time based on user input
site_id: str | None = locations.get(get_loc)
max_time: int | None = get_times

# Check if the site ID is valid and proceed with fetching departures data
if site_id:
    # Loop to keep asking for a valid transport type or one with departures
    while True:
        transport_mode: str = input("Enter transport type (bus/train/metro): ").lower()

        if transport_mode in ["bus", "train", "metro"]:
            # Create an instance of AllTransports class with the selected site ID
            transport: classes.AllTransports = classes.AllTransports(site_id)

            # Fetch departures for the selected mode and maximum time
            departures: list[str] = transport.get_departures_by_mode(transport_mode, max_time)

            # Check if there are any departures within the next {get_times} minutes for the selected transport mode
            if departures:
                print(f"{transport_mode.capitalize()} departures within {get_times} minutes:")
                for departure in departures:
                    print(departure)
                break  # Exit the loop if valid departures are found
            else:
                print(f"No {transport_mode} departures within the next {get_times} minutes. Please try another transport type.")
        else:
            print("Invalid transport type, please try again.")  # Loop continues if invalid input
