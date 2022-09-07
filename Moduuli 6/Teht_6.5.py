def pruner(lst):
    result_list = []
    for i in lst:
        if i % 2 == 0:
            result_list.append(i)
    return result_list

def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even = pruner(lst)
    print(lst)
    print(even)
main()