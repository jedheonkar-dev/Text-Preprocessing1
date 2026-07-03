"""
Text Preprocessing
Author: Onkar Jedhe

A collection of common NLP text preprocessing steps implemented with
Python's standard library only (no external downloads required):
lowercasing, punctuation/number removal, tokenization, stopword
removal, and simple suffix-based stemming. Run directly to see each
step applied to a sample set of sentences.
"""

import re
import string

# A compact English stopword list (standard library only, no downloads needed)
STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "is", "are", "was", "were",
    "be", "been", "being", "in", "on", "at", "to", "for", "of", "with",
    "by", "from", "as", "it", "its", "this", "that", "these", "those",
    "i", "you", "he", "she", "we", "they", "them", "his", "her", "their",
    "our", "your", "my", "me", "him", "us", "do", "does", "did", "have",
    "has", "had", "not", "no", "so", "than", "too", "very", "can", "will",
    "just", "over", "under", "again", "further", "then", "once", "isnt",
    "am",
}

# Minimal suffix rules for a lightweight stemmer (Porter-style approximation)
_STEM_SUFFIXES = ("ing", "edly", "ed", "ly", "es", "s")


def to_lowercase(text):
    """Convert text to lowercase."""
    return text.lower()


def remove_punctuation(text):
    """Remove punctuation characters from text."""
    return text.translate(str.maketrans("", "", string.punctuation))


def remove_numbers(text):
    """Remove digits from text."""
    return re.sub(r"\d+", "", text)


def remove_extra_whitespace(text):
    """Collapse repeated whitespace into a single space."""
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text):
    """Split text into a list of word tokens."""
    return text.split()


def remove_stopwords(tokens):
    """Remove common stopwords from a list of tokens."""
    return [word for word in tokens if word not in STOPWORDS]


def simple_stem(word):
    """Strip a small set of common suffixes from a word."""
    for suffix in _STEM_SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[: -len(suffix)]
    return word


def stem_tokens(tokens):
    """Apply simple suffix-stripping stemming to a list of tokens."""
    return [simple_stem(word) for word in tokens]


def preprocess_text(text, use_stemming=True):
    """Run the full preprocessing pipeline on a single piece of text."""
    text = to_lowercase(text)
    text = remove_punctuation(text)
    text = remove_numbers(text)
    text = remove_extra_whitespace(text)

    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)

    if use_stemming:
        tokens = stem_tokens(tokens)

    return tokens


def main():
    sample_sentences = [
        "The quick brown foxes are jumping over 2 lazy dogs!!",
        "Natural Language Processing (NLP) is amazing, isn't it?",
        "I've bought 3 apples, 5 oranges, and 10 bananas from the market.",
    ]

    for i, sentence in enumerate(sample_sentences, start=1):
        print(f"Original {i}: {sentence}")
        cleaned = preprocess_text(sentence)
        print(f"Processed {i}: {cleaned}\n")


if __name__ == "__main__":
    main()
