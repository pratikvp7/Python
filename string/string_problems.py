from collections import Counter


class StringProblems:

    def reverse_string_without_slicing(self, string):
        # return string[::-1]
        revsersed_string = ""
        for index in range(len(string)-1, 0, -1):
            revsersed_string += string[index]
        return revsersed_string
    
    def check_pallindrome(self, string):
        return string.casefold() == string[::-1].casefold()
    
    def duplicate_element_in_string(self, string):
        duplicates = set()
        for s in string:
            temp = 0
            for s1 in string:                
                if s == s1:
                    temp += 1
            if temp > 1:
                duplicates.add(s)
        return ', '.join(duplicates)
    
    def duplicate_elements_in_string_collections_approach(self, string):
        counts = Counter(string)
        duplicates = []
        for value, count in counts.items():
            if count > 1:
                duplicates.append(value)
        return ''.join(duplicates)
    
    def check_anagrams(self, string1, string2):
        if len(string1) != len(string2):
            return False
        
        # return Counter(string1.lower()) == Counter(string2.lower())

        for s1 in string1:
            if s1 not in string2:
                return False
        return True
    
    def count_vowels(self, string):
        vowels = 'aeiou'
        vowels_count = 0
        count = Counter(string)
        for value, count in count.items():
            if value in vowels:
                vowels_count += count
        return vowels_count
    
    def count_vowels_and_consonants(self, string):
        vowels = 'aeiou'
        vowel_count = 0
        consonant_count = 0
        counter = Counter(string)
        for value, count in counter.items():
            if value in vowels:
                vowel_count += count
            else:
                consonant_count += count
        return vowel_count, consonant_count
    
    def count_vowels_and_consonants_without_counter(self, string):
        vowels = 'aeiou'
        """
        following is chain assignment and only safe for immutable objects as if i 
        assign other value to any of these vars - it will create a separate object 
        later keeping both objects separate but that is not the case for mutable objects like list)
        """
        vowels_count = consonants_count = 0
        count_dict = {}
        for ch1 in string:
            temp_count = 0
            for ch2 in string:
                if ch1 == ch2:
                    temp_count += 1
            count_dict[ch1] = temp_count 

        for value, count in count_dict.items():
            if value in vowels:
                vowels_count += count
            else:
                consonants_count += count

        return vowels_count, consonants_count
    
    def longest_substring_without_repeating_characters(self, string):
        substrings = set()
        left = 0
        max_length = 0

        for right in range(len(string)):

            while string[right] in substrings:
                substrings.remove(string[left])
                left += 1

            substrings.add(string[right])

            max_len = max(max_length, right - left +1)

        return max_len

            

if __name__ == "__main__":
    string_problems = StringProblems()
    print(string_problems.reverse_string_without_slicing("Hello, World!"))
    print(string_problems.check_pallindrome("Ana"))
    print(string_problems.duplicate_element_in_string("aassaadfdghjk"))
    print(string_problems.duplicate_elements_in_string_collections_approach("asasasd"))
    print(string_problems.check_anagrams("ala", "laa"))
    print(string_problems.count_vowels("wertfeeeeiiodaserf"))
    print(string_problems.count_vowels_and_consonants("sdfasdfeoiiuaegcxdfg"))
    print(string_problems.count_vowels_and_consonants_without_counter("sdfasdfeoiiuaegcxdfg"))
    print(string_problems.longest_substring_without_repeating_characters("avcdaaeedddddfrtgyiogds"))