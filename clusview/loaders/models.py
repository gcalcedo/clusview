from sentence_transformers import SentenceTransformer
from bertopic import BERTopic


def load_topic_model(model_name: str = "all-MiniLM-L6-v2"):
    """
    Creates a `BERTopic` model using the specified `SentenceTransformer`.

    ### Args:
        - `model_name : str`: name identification of the model in the HuggingFace Model Hub.
        Defaults to `all-MiniLM-L6-v2`.

    ### Returns:
        - `BERTopic`: the topic model. Note that this topic model only specifies the embedding model.
        No dimensionality reduction or clustering is defined. These must be loaded afterwards via the
        `loaders` package.
    """
    sentence_model = SentenceTransformer(model_name)
    return BERTopic(
        embedding_model=sentence_model,
    )
