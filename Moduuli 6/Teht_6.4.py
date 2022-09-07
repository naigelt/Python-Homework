list1 = [3, 5, 7, 8, 9, 1]

def sumOfList(list, size):
    if (size==0):
        return 0
    else:
        return list[size-1] + sumOfList(list, size-1)
def main():
 total = sumOfList(list1, len(list1))
 print("Sum of all elements in the given list: ", total)
main()