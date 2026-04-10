

class Practice:

    def __init__(self):
        print("***Lists practice initialized***")


    def list_practice_1(self):
        list1 = [1, 2, 3, 4, 2, 2, 5]
        list1.append(6)
        print(list1)

        list1.insert(0, 0)
        print(list1)

        list1.remove(6)
        print(list1)

        ret = list1.pop()
        print(list1)
        print(ret)

        ret = list1.pop(4)
        print(list1)
        print(ret)

        list1.extend([7, 8, 9])
        print(list1)

        index = list1.index(3)
        print(index)

        count = list1.count(2)
        print(count)

        list1.sort()
        print(list1)

        list1.sort(reverse=True)
        print(list1)

        list1.reverse()
        print(list1)

        list2 = list1.copy()
        print(list2)

        list1.extend(list2)
        print(list1)

        list1.clear()
        print(list1)

    def list_practice_2(self):
        list1 = [1, 2, 3, 4, 5]

        list2 = list1 * 3
        print(list2)

        list3 = list1 + list2
        print(list3)

    def list_practice_3(self):
        lst = [1, 5, 6, 2, 4, 3]
        sorted_lst = sorted(lst)
        print(sorted_lst)

        sorted_lst_desc = sorted(lst, reverse=True)
        print(sorted_lst_desc)

if __name__ == "__main__":
    practice = Practice()
    practice.list_practice_1()
    practice.list_practice_2()
    practice.list_practice_3()