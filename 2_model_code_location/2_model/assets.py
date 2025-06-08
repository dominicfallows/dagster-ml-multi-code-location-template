from dagster import asset, SourceAsset

# Simple synonym groups for demonstration
SYNONYM_GROUPS = [
    {"hello", "hi", "greetings"},
    {"world", "earth", "globe"},
    {"awesome", "great", "fantastic"},
    {"test", "trial", "experiment"},
]

vocab_from_train_data = SourceAsset("vocab_from_train_data")


def group_vocab_by_synonym(vocab):
    """
    Groups vocabulary words by predefined synonym sets.
    Args:
        vocab (list[str]): List of vocabulary words.
    Returns:
        list[list[str]]: Grouped vocabulary.
    """
    grouped = []
    used = set()
    for word in vocab:
        found = False
        for group in SYNONYM_GROUPS:
            if word in group:
                group_words = group & set(vocab)
                if group_words and not group_words.issubset(used):
                    grouped.append(sorted(group_words))
                    used.update(group_words)
                found = True
                break
        if not found and word not in used:
            grouped.append([word])
            used.add(word)
    return grouped


@asset
def train_model_asset(context, vocab_from_train_data):
    """
    Trains a simple model by grouping vocabulary by synonym sets.
    Args:
        context: Dagster context.
        vocab_from_train_data (list[str]): Vocabulary extracted from training data.
    Returns:
        dict: Model with vocab size and grouped vocab (key: 'grouped_vocab').

    See Dagster concepts: https://docs.dagster.io/getting-started/concepts
    """
    grouped_vocab = group_vocab_by_synonym(vocab_from_train_data)
    model = {"vocab_size": len(vocab_from_train_data),
             "grouped_vocab": grouped_vocab}
    context.log.info(f"Trained model with grouped vocab: {model}")
    return model
