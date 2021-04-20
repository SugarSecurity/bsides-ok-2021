import json
import whois
import requests

def get_osint(event, context):
    domain_api_input = event['pathParameters']['domain']
    whois_results = whois.whois(domain_api_input)
    subdomain_results = requests.get(f"https://api.hackertarget.com/hostsearch?q={domain_api_input}/").content.decode("utf-8")
    http_response = {
        "statusCode": 200,
        "body": json.dumps({"whois": whois_results, "subdomains": subdomain_results})
    }
    return http_response