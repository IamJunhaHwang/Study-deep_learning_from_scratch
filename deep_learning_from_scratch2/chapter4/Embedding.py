import numpy as np

class Embedding:
    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeros_like(W)]
        self.idx =None

    def forward(self, idx):
        W, = self.params
        self.idx = idx
        out = W[idx]

        return out

    def backward(self, dout):
        dW, = self.grads
        dW[...] = 0  # ... 은 행렬 전체를 의미

        for i, word_id in enumerate(self.idx):
            dW[word_id] += dout[i]

        # for 문을 아래와 같이 대체 가능
        # np.add.at(dW, self.idx, dout)

        return None