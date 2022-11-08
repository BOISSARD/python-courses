import time

def indexOfSubString(string, substring):
    indexes = []
    i = 0
    while i < len(string):
        if string[i:i+len(substring)] == substring:
            indexes.append(i)
            i += len(substring)
        else : i += 1
    return indexes


def main():
    indexes = indexOfSubString("claiaireafontainea", "ai")
    print(indexes)

if __name__ == '__main__':
    main()