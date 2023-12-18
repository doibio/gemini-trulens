from llama_index import VectorStoreIndex, SimpleDirectoryReader

from trulens_eval import TruLlama

documents = SimpleDirectoryReader('edirect-um0').load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
l = TruLlama(query_engine)

response = l.query("What antigens are present in uveal melanoma?")
print(response)
