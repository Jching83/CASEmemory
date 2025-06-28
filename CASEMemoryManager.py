# case_memory/CASEMemoryManager.py

from llama_index import load_index_from_storage
from llama_index.storage.storage_context import StorageContext

class CASEMemoryManager:
    def __init__(self, index_dir="./case_memory/index"):
        self.index_dir = index_dir
        self.storage_context = StorageContext.from_defaults(persist_dir=self.index_dir)
        self.index = load_index_from_storage(self.storage_context)
        self.query_engine = self.index.as_query_engine(similarity_top_k=1)

    def get_context(self, prompt):
        return str(self.query_engine.query(prompt))

    def search_raw(self, prompt):
        return self.query_engine.query(prompt)
