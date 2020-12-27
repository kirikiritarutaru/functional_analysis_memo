import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
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
    # sigmoidal_step_approximation()

    fig = plt.figure(figsize=(6, 4))

    for i in [2, 5, 10, 20, 25, 50]:
        x_num = 500
        y_num = int(5*i)
        x = np.linspace(0, 2*np.pi, x_num)
        y = np.linspace(0, 2*np.pi, y_num)
        plt.plot(x, np.repeat(np.sin(y), int(x_num/y_num)))
        fig.savefig(f'step_func_{i}.jpg')
        plt.clf()
