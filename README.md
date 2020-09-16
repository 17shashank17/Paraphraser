# Paraphraser

This is a python library which generates list of sentences with similar contextual meaning as given input sentence. 

## Installation

Run the following snippet to install the library in your system

```python
$ pip install paraphraser
```

## Usage 

```python
from paraphraser import paraphrase
# Generate list of sentences with similar contextual meaning
sentences = paraphrase(input_sentence)
```

# Developing Paraphraser

To install paraphraser along with the tools you need to develop and run tests, run the following in command in your system:

```bash
$ pip install -e .[dev]
```