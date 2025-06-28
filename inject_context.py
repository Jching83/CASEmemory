# case_memory/inject_context.py

from llama_index import load_index_from_storage
from llama_index.storage.storage_context import StorageContext

def get_context(query, k=1):
    storage_context = StorageContext.from_defaults(persist_dir="./case_memory/index")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine(similarity_top_k=k)
    results = query_engine.query(query)
    return str(results)

# Example CLI use
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python inject_context.py \"your prompt\"")
    else:
        context = get_context(sys.argv[1])
        print("\n--- CASE MEMORY CONTEXT ---\n")
        print(context)
