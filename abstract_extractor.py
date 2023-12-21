from Bio import Entrez
from article_extractor import get_link  # Import the get_link function

email = ""

Entrez.email = email

def search(query, num_ids):
    handle = Entrez.esearch(db='pubmed',
                            sort = 'relevance',
                            retmax = num_ids,
                            retmode = 'xml',
                            term = query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    try:
        handle = Entrez.efetch(db='pubmed',
                               retmode = 'xml',
                               id = ids)
        results = Entrez.read(handle)
        return results
    except:
        return False


# if __name__ == '__main__':
#     results = search('breast cancer')
#     print(results)
#     id_list = results['IdList']
#     print(id_list)
#     papers = fetch_details(id_list)
#     print(papers)
#     for paper in papers['PubmedArticle']:
#         pmid = paper['MedlineCitation']['PMID']
#         if 'Abstract' in paper['MedlineCitation']['Article']:
#             abstract = paper['MedlineCitation']['Article']['Abstract']
#             print(f"PMID: {pmid}\nAbstract: {abstract}\n")
#         else:
#             print(f"PMID: {pmid}\nNo abastract available for this article.\n")
#     #print(f"Link to full article: {get_link('21843857')}\n")  # Use the get_link function
#
