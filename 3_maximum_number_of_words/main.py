"""
Вам дан список предложений.
предложения содержит только слова, которые разделены единичными пробелами.
Необходимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> bool:
    max_number = 0

    for sentence in sentences:
        words = sentence.split()
        word_count = len(words)

        if word_count > max_number:
            max_number = word_count

    return max_number


sentences = ["alice and bob love cats", "i think so too", "this is great thanks very much"]
print(get_max_number_of_words_from_sentences(sentences))
