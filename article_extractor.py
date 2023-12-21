from Bio import Entrez

email = "tzkiller500@gmail.com"

Entrez.email = email

def get_link(id):
    try:
        handle = Entrez.elink(dbfrom='pubmed', id=str(id), linkname='pubmed_pubmed')
        result = Entrez.read(handle)
        url = result[0]['LinkSetDb'][0]['Link'][0]['http://www.ncbi.nlm.nih.gov/Entrez/']
        print(url)
    except KeyError:
        url = "No URL available for this article."
    return url




