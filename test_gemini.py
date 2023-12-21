from llama_index.llms import Gemini
from abstract_extractor import search, fetch_details

gemini = Gemini()


def check_if_related(query):
    prompt = """Make sure that the question is related to PubMed or Scientific abstracts on Pubmed or information in those abstracts
                            if any other question is asked in the query answer with something like sorry but you query should only be related to pubmed nad 
                            scientific abstracts and the query starts from here: """ + query + """If it is related then just type Yes and if not type No" \
                                                                         and nothing else beside those two responses"""
    resp = gemini.complete(prompt)
    resp_text = resp.text  # Extract the text from the CompletionResponse object
    if resp_text.strip().lower() == "yes":
        return True
    else:
        return False


def return_query(query):
    prompt = """We are searching Pubmed for scientific abstracts and i want you to extract only one or two  word from the entire query that is 
    the most important word that we can use in a search engine in the key word to search the scientific abstract. Here is the query: """ + query
    resp = gemini.complete(prompt)
    return resp


def run_gemini(query, num_ids):
    # Initialize Gemini


        # Check if the query is related to scientific abstracts
        is_related = check_if_related(query)  # This is a placeholder for your function
        if is_related:
            serach_query = return_query(query)

            results = search(serach_query, num_ids)
            if not fetch_details:
                query = "No result against the Search"
                return query
            else:
                id_list = results['IdList']
                papers = fetch_details(id_list)

            # Create an empty list to store the results
            output = []
            if papers:
                for paper in papers['PubmedArticle']:
                    pmid = paper['MedlineCitation']['PMID']
                    if 'Abstract' in paper['MedlineCitation']['Article']:
                        abstract = paper['MedlineCitation']['Article']['Abstract']
                        # Append the result to the list
                        output.append(f"PMID: {pmid}\nAbstract: {abstract}\n")

            else:
                return "Sorry, but your query should only be related to PubMed and scientific abstracts as i am not programmed to answer any other questions."

            # Return the list of results
            return output

        else:
            return "Sorry, but your query should only be related to PubMed and scientific abstracts as i am not programmed to answer any other questions."

