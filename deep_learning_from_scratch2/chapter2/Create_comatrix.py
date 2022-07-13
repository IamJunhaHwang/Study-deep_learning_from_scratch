import numpy as np


def create_co_matrix(corpus, vocab_size, window_size=1):  # corpus는 preprocessing이 완료된 corpus
    corpus_size = len(corpus)
    co_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)  # shape = [단어 개수 x 단어 개수] 인 0행렬 생성

    for idx, word_id in enumerate(corpus):
        for i in range(1, window_size+1):  # corpus에서 등장한 하나의 문장 내에서 window 크기 만큼 각 단어의 왼쪽, 오른쪽 단어의 빈도를 확인한다.
            left_idx = idx - i
            right_idx = idx + i

            if left_idx >= 0:
                left_word_id = corpus[left_idx]  # 해당 단어의 왼쪽 단어의 id를 불러온다. (corpus는 id를 담고 있음)
                co_matrix[word_id, left_word_id] += 1  # 해당 단어의 주위에 어떤 단어가 자주 오는지의 빈도를 체크한다.

            if right_idx < corpus_size:
                right_word_id = corpus[right_idx]
                co_matrix[word_id, right_word_id] += 1

    return co_matrix
