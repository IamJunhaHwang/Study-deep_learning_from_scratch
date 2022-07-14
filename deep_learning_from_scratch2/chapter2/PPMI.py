import numpy as np


def ppmi(c, verbose = False, eps = 1e-8):   # C: co_occur_matrix
    m = np.zeros_like(c, dtype=np.float32)
    n = np.sum(c) // 2
    s = np.sum(c, axis=0)
    total = c.shape[0] * c.shape[1]
    cnt = 0

    for i in range(c.shape[0]):
        for j in range(c.shape[1]):     # pmi 계산해 pmi 행렬 채우기
            pmi = np.log2(c[i, j] * n / (s[j]*s[i]) + eps)
            m[i, j] = max(0, pmi)

            if verbose:     # 진행 상황 출력
                cnt += 1
                if cnt % (total // 100 + 1) == 0:
                    print('%.1f%% 완료' % (100*cnt/total))

    return m

