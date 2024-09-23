import requests

api_key = "a083ca434d214b84af23a4a0b15595e7"

fittja = "9283"
uppsala = "6086"
sodertalje = "9520"  # Avoid using special characters in variable names like å, ä, ö
sollentuna = "9506"
skanstull = "9190"

q = int(input("Enter a number:\n1. Fittja\n2. Uppsala\n3. Södertälje\n4. Sollentuna\n5. Skanstull\n"))

if q == 1:
    site_id = fittja
elif q == 2:
    site_id = uppsala
elif q == 3:
    site_id = sodertalje
elif q == 4:
    site_id = sollentuna
elif q == 5:
    site_id = skanstull
else:
    print("Invalid input")
    exit()

address = f"https://transport.integration.sl.se/v1/sites/{site_id}/departures"


res = requests.get(address)

if res.status_code == 200:
    data = res.json()

    departures = data.get("departures", [])

    # List to store destinations within 20 minutes
    destinations_time_20 = []

    # Loop through each departure to process destination and display time
    for departure in departures:
        destination = departure.get("destination")
        display = departure.get("display")
        line = departure.get("line")


        # Check if the display contains "min", meaning it's a time-based display in minutes
        if display and "min" in display:
            # Extract the number of minutes from the display
            try:
                min_left = int(display.split()[0])
            except ValueError:
                # In case the split does not return an integer (e.g., if the format is wrong)
                continue

            # If departure is within 20 minutes, add the destination and time to the list
            if min_left <= 20:
                if isinstance(line, dict):
                    name = line.get("designation")
                    transport_mode = line.get("transport_mode")
                    destinations_time_20.append(f"{transport_mode} - {name} {destination} - {display}")

    # Print the filtered destinations and times
    print("Destinations within 20 minutes:")
    if destinations_time_20:
        for destination in destinations_time_20:
            print(destination)
    else:
        print("No departures within the next 10 minutes.")
else:
    print(f"Error: Unable to fetch data (status code: {res.status_code})")