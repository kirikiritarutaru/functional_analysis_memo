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
    plt.figure(figsize=(8, 5))
    for s in [1, 3, 10]:
        plt.plot(y, sigmoid(y, s))
    plt.plot(y, step_function(y))
    plt.title('sigmoidal関数がステップ関数に近づいていく様子')
    plt.savefig('sigmoidal.jpg')


def plot_sin_curve():
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 3))

    x_num = 500
    x = np.linspace(0, 2*np.pi, x_num)
    ax1.plot(x, np.sin(x))
    for i in [2, 5, 10, 20, 25, 50]:
        y_num = int(5*i)
        y = np.linspace(0, 2*np.pi, y_num)
        ax0.plot(x, np.repeat(np.sin(y), int(x_num/y_num)))
        fig.savefig(f'step_func_{i}_r.jpg')
        ax0.clear()


if __name__ == '__main__':
    sigmoidal_step_approximation()
