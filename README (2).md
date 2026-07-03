# Text Preprocessing

A collection of common NLP text preprocessing steps implemented in pure Python (standard library only — no external downloads required).

**Author:** Onkar Jedhe

## Overview

This project demonstrates how to:
- Lowercase text
- Remove punctuation and numbers
- Normalize whitespace
- Tokenize text into words
- Remove common stopwords
- Apply simple suffix-based stemming (e.g. "jumping" → "jump")

Because it avoids external NLP libraries like NLTK or spaCy, it runs immediately with no data downloads or setup — just plain Python.

## Requirements

No external dependencies are required (Python 3.6+ standard library only).

If you'd like, you can still install from `requirements.txt` — it's left empty intentionally in case you extend the project later (e.g. adding NLTK or spaCy).

## Usage

```bash
python text_preprocessing.py
```

This runs the pipeline on a few sample sentences and prints the before/after result for each.

## Sample Output

```
Original 1: The quick brown foxes are jumping over 2 lazy dogs!!
Processed 1: ['quick', 'brown', 'fox', 'jump', 'lazy', 'dog']

Original 2: Natural Language Processing (NLP) is amazing, isn't it?
Processed 2: ['natural', 'language', 'process', 'nlp', 'amaz']

Original 3: I've bought 3 apples, 5 oranges, and 10 bananas from the market.
Processed 3: ['ive', 'bought', 'appl', 'orang', 'banana', 'market']
```

## Files

| File | Description |
|---|---|
| `text_preprocessing.py` | Main script with all preprocessing functions and a demo |
| `requirements.txt` | Dependencies (none required by default) |

## Using It On Your Own Text

Import the pipeline directly:

```python
from text_preprocessing import preprocess_text

tokens = preprocess_text("Your custom sentence here!")
print(tokens)
```

## License

This project is open source and available under the MIT License.
