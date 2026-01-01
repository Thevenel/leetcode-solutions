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
