from sys import argv

def load_input(splitstring = "\n"):
    if len(argv) > 1:
        filename = "examples.txt"
        print("Using test cases...\n")
    else:
        filename = "input.txt"
        print("Using input...\n")
    with open(filename, "r") as f:
        return list(filter(bool, f.read().split(splitstring)))


def load_raw():
    if len(argv) > 1:
        filename = "examples.txt"
        print("Using test cases...\n")
    else:
        filename = "input.txt"
        print("Using input...\n")
    with open(filename, "r") as f:
        return f.read()
