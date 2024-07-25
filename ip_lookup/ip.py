import requests

def get_ip_info(ip):
    access_token = '7fe9a2efbae984'  # Remplacez par votre token d'accès ipinfo.io
    url = f"https://ipinfo.io/{ip}/json?token={access_token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erreur: {response.status_code}"

def display_ip_info(ip_info):
    if isinstance(ip_info, dict):
        print(f"Adresse IP : {ip_info.get('ip', 'N/A')}")
        print(f"Ville : {ip_info.get('city', 'N/A')}")
        print(f"Région : {ip_info.get('region', 'N/A')}")
        print(f"Pays : {ip_info.get('country', 'N/A')}")
        print(f"Localisation : {ip_info.get('loc', 'N/A')}")
        print(f"Organisation : {ip_info.get('org', 'N/A')}")
        print(f"Code postal : {ip_info.get('postal', 'N/A')}")
        print(f"Fuseau horaire : {ip_info.get('timezone', 'N/A')}")
        
        # Vérifier les informations de confidentialité
        privacy = ip_info.get('privacy', {})
        print(f"VPN : {privacy.get('vpn', 'N/A')}")
        print(f"Proxy : {privacy.get('proxy', 'N/A')}")
        print(f"Tor : {privacy.get('tor', 'N/A')}")
        print(f"Relay : {privacy.get('relay', 'N/A')}")
        print(f"Hébergement : {privacy.get('hosting', 'N/A')}")
    else:
        print(ip_info)

while True:
    ip = input("Adresse IP : ")
    if ip.lower() == 'exit':
        break
    info = get_ip_info(ip)
    display_ip_info(info)
