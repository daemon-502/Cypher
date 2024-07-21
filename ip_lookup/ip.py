import requests

def ip_lookup(ip, output_format='json'):
    api_key = '0b27e27d340539e7bd78b44678377504997d9234'
    base_url = 'https://api.viewdns.info/iplocation/'
    params = {
        'ip': ip,
        'output': output_format,
        'apikey': api_key
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json() if output_format == 'json' else response.text
    else:
        return {
            'response_code': response.status_code,
            'response_message': response.reason
        }

# Exemple d'utilisation
if __name__ == "__main__":
    ip_address = input("Adresse IP : ")
    result = ip_lookup(ip_address)
    
    if isinstance(result, dict) and 'response_code' in result:
        print(f"Error {result['response_code']}: {result['response_message']}")
    else:
        if isinstance(result, str):
            print(result)  # Pour XML output
        else:
            response = result['response']
            print(f"IP: {ip_address}")
            print(f"Ville: {response['city']}")
            print(f"Code Postal: {response['zipcode']}")
            print(f"Region Code: {response['region_code']}")
            print(f"Region: {response['region_name']}")
            print(f"Pays Code: {response['country_code']}")
            print(f"Pays: {response['country_name']}")
            print(f"Latitude: {response['latitude']}")
            print(f"Longitude: {response['longitude']}")
