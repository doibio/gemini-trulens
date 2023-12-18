import sys
from llama_index.llms import Gemini

prompt = "Please make a list of all the proteins and possible cancer antigens in this abstract.  If it does not contain any of these, output nothing: "
file_path = sys.argv[1]

with open(file_path, 'r') as file:
    file_contents = file.read()

query = prompt + file_contents
resp = Gemini().complete(query)
print(resp)

