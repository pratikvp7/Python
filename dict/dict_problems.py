

class DictProblems:


    def dict_operations(self):
        dict1 = {
            1: 'abc',
            2: 'def',
            3: 'ghi'
        }
        print(dict1)
        for key, value in dict1.items():
            print(key, value)

        keys = dict1.keys()
        values = dict1.values()
        print(keys, values)

        list(values).insert(1, 'jkl')
        
if __name__ == '__main__':
    dict = DictProblems()
    dict.dict_operations()
