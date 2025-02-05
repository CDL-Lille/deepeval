from deepeval.synthesizer.chunking.context_generator import ContextGenerator
from deepeval.models.openai_embedding_model import OpenAIEmbeddingModel
from itertools import chain

from deepeval.models.openai_embedding_model import SentenceTransformerEmbeddingModel

context_generator = ContextGenerator(
    document_paths=["./synthesizer_data/pdf_example.pdf"],
    embedder=SentenceTransformerEmbeddingModel(),
)
context_generator._load_docs()
context_generator._load_docs()
context_generator._load_docs()

contexts, source_files, context_scores = context_generator.generate_contexts(
    num_context_per_document=10
)
print(
    f"Utilizing {len(set(chain.from_iterable(contexts)))} out of {context_generator.total_chunks} chunks."
)

context_generator._load_docs()
contexts, source_files, context_scores = context_generator.generate_contexts(
    num_context_per_document=10
)
print(
    f"Utilizing {len(set(chain.from_iterable(contexts)))} out of {context_generator.total_chunks} chunks."
)
