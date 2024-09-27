import transit


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
        transport = transit.AllTransports(site_id)

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