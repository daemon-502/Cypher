import requests

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erreur: {response.status_code}"

def display_ip_info(ip_info):
    if isinstance(ip_info, dict):
        print(f"Adresse IP : {ip_info.get('query', 'N/A')}")
        print(f"Ville : {ip_info.get('city', 'N/A')}")
        print(f"Région : {ip_info.get('regionName', 'N/A')}")
        print(f"Pays : {ip_info.get('country', 'N/A')}")
        print(f"Localisation : {ip_info.get('lat', 'N/A')}, {ip_info.get('lon', 'N/A')}")
        print(f"Organisation : {ip_info.get('org', 'N/A')}")
        print(f"Fournisseur d'accès Internet : {ip_info.get('isp', 'N/A')}")
        print(f"Code postal : {ip_info.get('zip', 'N/A')}")
        print(f"Fuseau horaire : {ip_info.get('timezone', 'N/A')}")
        print(f"Statut proxy : {'Oui' if ip_info.get('proxy', False) else 'Non'}")
    else:
        print(ip_info)

while True:
    ip = input("Adresse IP : ")
    if ip.lower() == 'exit':
        break
    info = get_ip_info(ip)
    display_ip_info(info)
