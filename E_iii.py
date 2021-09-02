class All_details(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


d = All_details()
History = []


def user_history(id_number, *hist):
    a = 100
    a += 1
    n = input("Enter the details")
    History.append(n)
    d.add(a, History)


def retrieve():
    for i, j in d.items():
        print()


# user_history()
