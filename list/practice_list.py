

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

"""
**NOTES**

- Difference between list.sort() and sorted(list): sorted(list) creates a new sorted list, while list.sort() sorts the list in place and returns None.

- Difference between list.copy() and list[:]: Both list.copy() and list[:] create a shallow copy of the list. However, list.copy() is more explicit and is generally preferred for clarity.

- Difference between list.clear() and list = []: list.clear() empties the existing list while keeping the same reference, whereas list = [] creates a new empty list and assigns it to the variable, which may not affect other references to the original list.

- Difference between list.append() and list.insert(): list.append() adds an element to the end of the list, while list.insert(index, element) allows you to specify the position where the element should be added.

- Difference between list.remove() and list.pop(): list.remove(element) removes the first occurrence of the specified element, while list.pop(index) removes and returns the element at the specified index. If no index is provided, it removes and returns the last element of the list.

- Difference between list.extend() and list.append(): list.extend(iterable) adds each element of the iterable to the end of the list, while list.append(element) adds the entire element as a single item to the end of the list.

- Difference between list.index() and list.count(): list.index(element) returns the index of the first occurrence of the specified element, while list.count(element) returns the number of occurrences of the specified element in the list.

- Difference between list.sort() and list.reverse(): list.sort() sorts the elements of the list in ascending order (or according to a specified key), while list.reverse() reverses the order of the elements in the list without sorting them.

- Difference between list.sort() and sorted(): list.sort() sorts the list in place and modifies the original list, while sorted(list) returns a new sorted list without modifying the original list.  
"""