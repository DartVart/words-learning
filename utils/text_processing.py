import re
from typing import List

SEPARATORS = ['\n', '.', '!', '?']


def add_content(sentences: List[str], sentence_content: List[str]) -> None:
    if len(sentence_content) > 0 and sentence_content[0] not in SEPARATORS:
        if sentence_content[-1] not in SEPARATORS:
            sentence_content.append('.')
        sentences.append(
            ''.join(sentence_content).encode("ascii", "ignore").decode()
        )


def split_to_sentences(text: str) -> List[str]:
    sentences = []
    sentences_with_separators = [s.strip() for s in re.split(rf"([{''.join(SEPARATORS)}])", text) if s.strip() != '']
    sentence_content = []
    for token in sentences_with_separators:
        if token in SEPARATORS:
            sentence_content.append(token)
        else:
            add_content(sentences, sentence_content)
            sentence_content = [token]
    add_content(sentences, sentence_content)

    return sentences
