import whois

def analyze_domain(domain):
    try:
        w = whois.whois(domain)
        return {
            "domain": domain,
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date)
        }
    except Exception as e:
        return {
            "error": str(e)
        }
