def pruner(lst):
    result_list = []
    for i in lst:
        if i % 2 == 0:
            result_list.append(i)
    return result_list

def main():
    lst = [1, 22, 3, 44, 5, 6, 66, 67, 55, 113]
    even = pruner(lst)
    print(lst)
    print(even)
main()