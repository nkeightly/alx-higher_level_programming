#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for el in dir(hidden_4):
        if el[0] != "_" or el[1] != "_":
            print("{}".format(el))
