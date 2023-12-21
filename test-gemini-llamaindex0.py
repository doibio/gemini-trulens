import sys
from llama_index.llms import Gemini

prompt = "Summarize this abstract for a bioinformatics researcher: "
file_path = sys.argv[0]

with open(file_path, 'r') as file:
    file_contents = file.read()

query = prompt + file_contents
resp = Gemini().complete(query)
print(resp)

