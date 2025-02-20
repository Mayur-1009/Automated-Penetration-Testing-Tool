import whois
import shodan
import nmap
import requests

SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"

def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        return {
            "Domain": domain_info.domain_name,
            "Registrar": domain_info.registrar,
            "Creation Date": domain_info.creation_date,
            "Expiration Date": domain_info.expiration_date,
            "Nameservers": domain_info.name_servers
        }
    except Exception as e:
        return {"Error": str(e)}

def subdomain_scan(domain):
    try:
        shodan_api = shodan.Shodan(SHODAN_API_KEY)
        results = shodan_api.search(domain)
        return [{"IP": service['ip_str'], "Port": service['port']} for service in results['matches']]
    except Exception as e:
        return {"Error": str(e)}

def scan_ports(target):
    try:
        scanner = nmap.PortScanner()
        scanner.scan(target, '1-65535', '-sV')
        return [{"Port": port, "State": data['state'], "Service": data['name']} for port, data in scanner[target]['tcp'].items()]
    except Exception as e:
        return {"Error": str(e)}
