import requests

def fetch_swapi_data():
    url = "https://swapi.info/api/starships"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for ship in data:
            print(f"\nStarship: {ship.get('name')}")
            pilots = ship.get("pilots", [])
            if pilots:
                for pilot_url in pilots:
                    try:
                        pilot_res = requests.get(pilot_url)
                        pilot_res.raise_for_status()
                        pilot_data = pilot_res.json()
                        print(f"  Pilot: {pilot_data.get('name')}")
                    except requests.exceptions.RequestException as e:
                        print(f"  Error fetching pilot: {e}")
            else:
                print("  No pilots listed.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

fetch_swapi_data()



