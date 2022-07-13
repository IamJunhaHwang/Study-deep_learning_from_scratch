import numpy as np


def preprocessing(text):
    text = text.lower()
    text = text.replace('.', ' .')
    words = text.split(' ')

    word_to_id = {}
    id_to_word = {}

    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)        # 새로운 변수를 선언해서 다루면 확장성에 문제가 생길까? ex. cnt +=1
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    corpus = np.array(range(len(word_to_id)))  # np.array([word_to_id[w] for w in words)
                                               # 사전에 숫자 순서대로 들어가므로 length로 넣어도 괜찮지 않을까?

    return corpus, word_to_id, id_to_word


if __name__ == "__main__":
    text = 'You say goodbye and I say hello.'

    corpus, word_to_id, id_to_word = preprocessing(text)

    print(corpus)
    print(word_to_id)
    print(id_to_word)
