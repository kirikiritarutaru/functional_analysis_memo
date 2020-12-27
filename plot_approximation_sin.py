import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib as jmpl

jmpl.japanize()


def sigmoid(x, s):
    return 1 / (1+np.exp(-s*x))

# ステップ関数


def step_function(x):
    y = x > 0
    return np.array(x > 0, dtype=np.int)


def sigmoidal_step_approximation():
    y = np.linspace(-5, 5, 500)
    plt.figure(figsize=(15, 10))
    for s in [1, 3, 10]:
        plt.plot(y, sigmoid(y, s))
    plt.plot(y, step_function(y))
    plt.title('sigmoidal関数がステップ関数に近づいていく様子')
    plt.show()


if __name__ == '__main__':
    sigmoidal_step_approximation()
