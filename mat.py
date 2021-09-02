import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import json
import random

with open('Stock List.json') as f:
    # reading file
    data = json.load(f)


def weekly_data():
    i = 0
    j = 1
    # for the week
    for emp in data:
        i += 1
        j += 1
        plt.bar(j, emp['high'],)
        if i == 7:
            break
    plt.xlabel("Weeks")
    plt.ylabel("The high values")
    plt.title("Stocks data for one week")
    plt.show()


if __name__ == '__main__':
    weekly_data()
