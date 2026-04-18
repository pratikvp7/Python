from collections import Counter


class TuplesPractice:


    def tuple_basics(self):
        tup = ('string', 8, True, 9.0)
        print(tup)
        print(len(tup))

        tup2 = ('string2', False, 10)

        print(tup + tup2)
        print(tup.count(8))
        print(tup.index(9.0))

        print(tup2[1:3])
        print(tup2[:-1])
        print(tup2[::-1])
        print(tup2[0:3:2])
        print(tup2[1:])
        print(tup2[1::])

        tup3 = (1, 2, 3, 4, 5)
        print(max(tup3))
        print(min(tup3))
        print(sum(tup3))

        print(any(tup3))
        print(all(tup3))

        print(sorted(tup3))

    def vowels_program(self, string):
        vowels = 'aeiou'
        count = Counter(string)
        vowel_count = 0
        consonant_count = 0

        for char, count in count.items():
            if char in vowels:
                vowel_count += count
            else:
                consonant_count += count
        return vowel_count, consonant_count



if __name__ == '__main__':
    tup = TuplesPractice()
    tup.tuple_basics()
    print(tup.vowels_program(string='qwertfdawert'))