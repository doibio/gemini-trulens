import sys
from llama_index.llms import Gemini


query = "Please write a script for an opentrons robot to create a phage display library"
resp = Gemini().complete(query)
print(resp)

