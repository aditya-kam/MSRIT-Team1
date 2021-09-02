import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import json
with open('Stock List.json') as f:
    # reading file
    data = json.load(f)


def monthly_data():
    i = 0
    j = 1
    # for the monthly
    for emp in data:
        i += 1
        j += 1
        plt.bar(j, emp['high'])
        if i == 30:
            break
    plt.xlabel("Weeks")
    plt.ylabel("The high values")
    plt.title("Stocks data for one week")
    plt.show()


if __name__ == '__main__':
    monthly_data()
