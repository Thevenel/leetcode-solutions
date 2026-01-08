# Leetcode Solutions

This repository contains my solutions to various coding problems from NeetCode. Each solution is implemented in Python and organized by problem categories such as arrays, strings, linked lists, etc.

Feel free to explore the code, test the solutions, and contribute your own implementations!

## Arrays & Hashing

Below are some of the array-related problems I've solved:

### Duplicate Integer Check

- [Duplicate Integer Check](arrays/duplicate_integer/): A solution to check for duplicate integers in a list.

#### Possible solutions

Here are some possible approaches to solve the Duplicate Integer Check problem:

1. **Brute Force Approach**: Compare each element with every other element in the list.
    - complexity: O(n^2) time, O(1) space.

2. **Sorting Approach**: Sort the list first and then check adjacent elements for duplicates.
    - complexity: O(n log n) time, O(1) space (or O(n) if using a sorting algorithm that requires additional space).
3. **Hash Set Approach**: Use a hash set to store seen elements and return `True` if an element is already present in the set.
    - complexity: O(n) time, O(n) space.
4. **Dictionary Approach**: Use a dictionary to check if a number occurs more than once in the list.
    - complexity: O(n) time, O(n) space.

### Valid Anagram Check

- [Valid Anagram Check](arrays/valid_anagram/): A solution to determine if two strings are anagrams of each other.

#### Possible solutions

Here are some possible approaches to solve the Valid Anagram Check problem:

1. **Sorting Approach**: Sort both strings and compare them.
    - complexity: O(n log n) time, O(1) space (or O(n) if using a sorting algorithm that requires additional space).

2. **Hash Map Approach**: Use a hash map to count the frequency of each character in both strings and compare the counts.
    - complexity: O(n) time, O(1) space (since the character set is limited).
3. **Array Count Approach**: Use an array of fixed size (e.g., 26 for lowercase letters) to count character occurrences.
    - complexity: O(n) time, O(1) space.

### Two Sum Problem

- [Two Sum Problem](arrays/two_sum/): A solution to find two numbers in a list that add up to a target value.

#### Possible solutions

Here are some possible approaches to solve the Two Sum Problem:

1. **Brute Force Approach**: Check all pairs of numbers in the list.
    - complexity: O(n^2) time, O(1) space.
2. **Hash Map Approach**: Use a hash map to store numbers and their indices, then check if the complement exists.
    - complexity: O(n) time, O(n) space.

### Group Anagrams

- [Group Anagrams](arrays/group_anagrams/): A solution to group a list of strings into anagrams.

#### Possible solutions
Here are some possible approaches to solve the Group Anagrams problem:

1. **Sorting Approach**: Sort each string and use the sorted string as a key in a hash map to group anagrams.
    - complexity: O(n k log k) time, O(n k) space, where n is the number of strings and k is the maximum length of a string.

2. **Character Count Approach**: Use a fixed-size array to count character occurrences and use the count as a key in a hash map.
    - complexity: O(n k) time, O(n k) space, where n is the number of strings and k is the maximum length of a string.


### Top K Frequent Elements

- [Top K Frequent Elements](arrays/top_k_frequent/): A solution to find the k most frequent elements in a list.

#### Possible solutions

Here are some possible approaches to solve the Top K Frequent Elements problem:

1. **Hash Map and Sorting Approach**: Use a hash map to count frequencies, then sort the elements by frequency.
    - complexity: O(n log n) time, O(n) space.
2. **Bucket Sort Approach**: Use a hash map to count frequencies, then place elements in buckets based on their frequency and collect the top k elements.
    - complexity: O(n) time, O(n) space.

### Encode and Decode Strings

- [Encode and Decode Strings](arrays/encode_decode_strings/): A solution to encode a list of strings into a single string and decode it back.

#### Possible solutions

Here are some possible approaches to solve the Encode and Decode Strings problem:

1. **Delimiter Approach**: Use a special delimiter to separate strings in the encoded string.
    - complexity: O(n) time, O(n) space.

2. **Length Prefix Approach**: Prefix each string with its length to facilitate decoding.
    - complexity: O(n) time, O(n) space.

### Product of Array Except Self

- [Product of Array Except Self](arrays/product_of_array_except_self/): A solution to find the product of all elements in an array except for the current element.

#### Possible solutions

Here are some possible approaches to solve the Product of Array Except Self problem:

1. **Prefix and Suffix Products**: Calculate prefix and suffix products for each element.
    - complexity: O(n) time, O(1) space (excluding output array).

### Valid Sudoku

- [Valid Sudoku](arrays/valid_sudoku/): A solution to determine if a 9x9 Sudoku board is valid.

#### Possible solutions

Here are some possible approaches to solve the Valid Sudoku problem:

1. **Hash Set Approach**: Use hash sets to track seen numbers in rows, columns, and 3x3 sub-boxes.
    - complexity: O(1) time, O(1) space (since the board size is fixed).


### Longest Consecutive Sequence

- [Longest Consecutive Sequence](arrays/longest_consecutive_sequence/): A solution to find the length of the longest consecutive elements sequence in an array.

#### Possible solutions

Here are some possible approaches to solve the Longest Consecutive Sequence problem:

1. **Hash Set Approach**: Use a hash set to store elements and check for the start of sequences.
    - complexity: O(n) time, O(n) space.

### Valid Palindrome

- [Valid Palindrome](two_pointers/valid_palindrome/): A solution to determine if a string is a palindrome, considering only alphanumeric characters and ignoring cases.

#### Possible solutions

Here are some possible approaches to solve the Valid Palindrome problem:

1. **Two-Pointer Technique**: Use two pointers to compare characters from the beginning and end of the string, moving towards the center.
    - complexity: O(n) time, O(1) space.

2. **Reverse and Compare**: Clean the string and compare it to its reverse.
    - complexity: O(n) time, O(n) space.

