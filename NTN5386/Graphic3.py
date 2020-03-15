from Function3 import *
import matplotlib.pyplot as plt

'''
Do thi ve voi ti le logx,log(f(x))
'''


def draw_Graphic():

    plt.plot(n, f1, color='red', marker='.', markersize=10)
    plt.plot(n, f2, color='blue', marker='.', markersize=10)
    plt.plot(n, f3, color='yellow', linestyle='--', marker='.', markersize=10)
    plt.plot(n, f4, color='pink', marker='.', markersize=10)
    plt.plot(n, f5, color='black', marker='.', markersize=10)
    plt.plot(n, f6, color='green', marker='.', markersize=10)

    plt.title("Tốc độ tăng của các hàm cơ bản")
    plt.xlabel("log(n)")
    plt.ylabel("log(f(n))")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True)
    plt.legend(["n", "logn", "nlogn", "n^2", "n^3", "2^n"])

    plt.show()

draw_Graphic()
