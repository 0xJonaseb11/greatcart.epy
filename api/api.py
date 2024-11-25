import requests
import pandas as pd
try:
    vehicle_api = requests.get('http://127.0.0.1:8000/vehicle_api')
    vehicle_api.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    vehicle_api_data = vehicle_api.json()
    vehicle_owners_api = requests.get('http://127.0.0.1:8000/vehicle_owners_api')
    vehicle_owners_api.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    vehicle_owners_api_data = vehicle_owners_api.json()
    vdf = pd.DataFrame(vehicle_api_data['vehicles'])
    odf = pd.DataFrame(vehicle_owners_api_data['owners'])
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")