import sys
from llama_index.llms import Gemini


query = "What is uveal melanoma?  Please give a definition for a bioinformatician"
resp = Gemini().complete(query)
print(resp)

