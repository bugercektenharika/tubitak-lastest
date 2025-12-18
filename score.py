import tldextract

def hesapla_puan(trg_url):
    domain = tldextract.extract(trg_url).strip().casefold()
    
    puan = 1 

    if domain.subdomain and domain.subdomain not in ["www", "mail", "ftp"]:
        puan -= 1 


    if domain.suffix in ["com", "org", "net"]:
        puan += 1

    if domain.suffix in ["edu", "gov"]:
        puan += 2

    
    return puan, domain 