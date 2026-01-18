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


## Two Pointers

Below are some of the two-pointer related problems I've solved:

### Valid Palindrome

- [Valid Palindrome](two_pointers/valid_palindrome/): A solution to determine if a string is a palindrome, considering only alphanumeric characters and ignoring cases.

#### Possible solutions

Here are some possible approaches to solve the Valid Palindrome problem:

1. **Two-Pointer Technique**: Use two pointers to compare characters from the beginning and end of the string, moving towards the center.
    - complexity: O(n) time, O(1) space.

2. **Reverse and Compare**: Clean the string and compare it to its reverse.
    - complexity: O(n) time, O(n) space.


### Two Sum II - Input Array Is Sorted

- [Two Sum II - Input Array Is Sorted](two_pointers/two_sum_input_array_is_sorted/): A solution to find two numbers in a sorted array that add up to a target value.

#### Possible solutions

Here are some possible approaches to solve the Two Sum II - Input Array Is Sorted problem:

1. **Brute Force Approach**: Check all pairs of numbers in the sorted array.
    - complexity: O(n^2) time, O(1) space.
2. **Two-Pointer Technique**: Use two pointers, one at the start and one at the end of the array, to find the target sum.
    - complexity: O(n) time, O(1) space.

### Three Sum

- [Three Sum](two_pointers/three_sum/): A solution to find all unique triplets in an array that sum up to zero.

#### Possible solutions

Here are some possible approaches to solve the Three Sum problem:

1. **Sorting and Two-Pointer Technique**: Sort the array and use a two-pointer approach for each element to find pairs that sum to the negative of the current element.
    - complexity: O(n^2) time, O(1) space (excluding output).

### Container With Most Water

- [Container With Most Water](two_pointers/container_with_most_water/): A solution to find two lines that together with the x-axis form a container that holds the most water.

#### Possible solutions

Here are some possible approaches to solve the Container With Most Water problem:

1. **Brute Force Approach**: Check all pairs of lines to calculate the area.
    - complexity: O(n^2) time, O(1) space.
2. **Two-Pointer Technique**: Use two pointers at the beginning and end of the array and move them towards each other to find the maximum area.
    - complexity: O(n) time, O(1) space.


### Trapping Rain Water

- [Trapping Rain Water](two_pointers/trapping_rain_water/): A solution to calculate how much water can be trapped after raining.

#### Possible solutions

Here are some possible approaches to solve the Trapping Rain Water problem:

1. **Two-Pointer Technique**: Use two pointers to traverse the array from both ends, keeping track of the maximum heights seen so far.
    - complexity: O(n) time, O(1) space.


## Sliding Window

Below are some of the sliding window related problems I've solved:

### Best Time to Buy and Sell Stock

- [Best Time to Buy and Sell Stock](sliding_window/best_time_to_buy_and_sell_stock/): A solution to find the maximum profit from a single buy and sell of stock.

#### Possible solutions

Here are some possible approaches to solve the Best Time to Buy and Sell Stock problem:

1. **Single Pass Approach**: Traverse the price list while keeping track of the minimum price and calculating the maximum profit at each step.
    - complexity: O(n) time, O(1) space.


### Longest Substring Without Repeating Characters

- [Longest Substring Without Repeating Characters](sliding_window/longest_substring_without_repeating_characters/): A solution to find the length of the longest substring without repeating characters.

#### Possible solutions

Here are some possible approaches to solve the Longest Substring Without Repeating Characters problem:

1. **Sliding Window with Set**: Use a sliding window approach with a hash set to track the characters in the current window.
    - complexity: O(n) time, O(min(m, n)) space, where m is the size of the character set.


### Longest Repeating Character Replacement

- [Longest Repeating Character Replacement](sliding_window/longest_repeating_character_replacement/): A solution to find the length of the longest substring that can be obtained by replacing at most k characters.

#### Possible solutions

Here are some possible approaches to solve the Longest Repeating Character Replacement problem:

1. **Sliding Window with Frequency Count**: Use a sliding window approach while maintaining the count of the most frequent character in the current window.
    - complexity: O(n) time, O(1) space (since the character set is limited).
2. **Sliding Window with Hash Map**: Use a sliding window approach with a hash map to track character frequencies.
    - complexity: O(n) time, O(1) space (since the character set is limited).


### Permutation in String
- [Permutation in String](sliding_window/permutation_in_string/): A solution to check if one string's permutation is a substring of another string.

#### Possible solutions

Here are some possible approaches to solve the Permutation in String problem:

1. **Sliding Window with Frequency Count**: Use a sliding window approach with frequency counts of characters to check for permutations.
    - complexity: O(n) time, O(1) space (since the character set is limited).

### Minimum Window Substring

- [Minimum Window Substring](sliding_window/minimum_window_substring/): A solution to find the minimum window substring in a string that contains all characters of another string.

#### Possible solutions

Here are some possible approaches to solve the Minimum Window Substring problem:

1. **Sliding Window with Hash Map**: Use a sliding window approach with a hash map to track character frequencies and find the minimum window.
    - complexity: O(n) time, O(m) space, where m is the size of the character set in the target string.


### Sliding Window Maximum

- [Sliding Window Maximum](sliding_window/sliding_window_maximum/): A solution to find the maximum value in each sliding window of size k in an array.

#### Possible solutions

Here are some possible approaches to solve the Sliding Window Maximum problem:

1. **Deque Approach**: Use a deque to maintain the indices of useful elements in the current window.
    - complexity: O(n) time, O(k) space.


## Stacks

Below are some of the stack-related problems I've solved:

### Valid Parentheses

- [Valid Parentheses](stacks/valid_parentheses/): A solution to determine if a string of parentheses is valid.

#### Possible solutions

Here are some possible approaches to solve the Valid Parentheses problem:

1. **Stack Approach**: Use a stack to keep track of opening parentheses and match them with closing ones.
    - complexity: O(n) time, O(n) space.
