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


### Min Stack

- [Min Stack](stacks/min_stack/): A solution to implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#### Possible solutions

Here are some possible approaches to solve the Min Stack problem:

1. **Two Stack Approach**: Use one stack for the main stack and another stack to keep track of the minimum elements.
    - complexity: O(1) time for all operations, O(n) space.


### Evaluate Reverse Polish Notation

- [Evaluate Reverse Polish Notation](stacks/evaluate_reverse_polish_notation/): A solution to evaluate the value of an arithmetic expression in Reverse Polish Notation.

#### Possible solutions

Here are some possible approaches to solve the Evaluate Reverse Polish Notation problem:

1. **Stack Approach**: Use a stack to evaluate the expression by pushing numbers and popping them for operations.
    - complexity: O(n) time, O(n) space.


### Daily Temperatures

- [Daily Temperatures](stacks/daily_temperatures/): A solution to find the number of days until a warmer temperature for each day in a list.

#### Possible solutions

Here are some possible approaches to solve the Daily Temperatures problem:

1. **Monotonic Stack Approach**: Use a stack to keep track of indices of temperatures and calculate the number of days until a warmer temperature.
    - complexity: O(n) time, O(n) space.


### Car Fleet

- [Car Fleet](stacks/car_fleet/): A solution to determine the number of car fleets that will arrive at a destination.

#### Possible solutions

Here are some possible approaches to solve the Car Fleet problem:

1. **Stack Approach**: Sort cars by their starting positions and use a stack to determine fleets based on their arrival times.
    - complexity: O(n log n) time, O(n) space.

### Largest Rectangle in Histogram

- [Largest Rectangle in Histogram](stacks/largest_rectangle_in_histogram/): A solution to find the largest rectangle area in a histogram.

#### Possible solutions

Here are some possible approaches to solve the Largest Rectangle in Histogram problem:

1. **Stack Approach**: Use a stack to keep track of indices of histogram bars and calculate the maximum area.
    - complexity: O(n) time, O(n) space.

## Binary Search

Below are some of the binary search-related problems I've solved:

### Binary Search

- [Binary Search](binary_search/binary_search/): A solution to perform binary search on a sorted array.

#### Possible solutions

Here are some possible approaches to solve the Binary Search problem:

1. **Iterative Approach**: Use a loop to repeatedly divide the search interval in half.
    - complexity: O(log n) time, O(1) space.

### Search in 2D Matrix

- [Search in 2D Matrix](binary_search/search_in_2d_matrix/): A solution to search for a target value in a 2D matrix.

#### Possible solutions

Here are some possible approaches to solve the Search in 2D Matrix problem:

1. **Flattened Binary Search**: Treat the 2D matrix as a 1D sorted array and perform binary search.
    - complexity: O(log(m*n)) time, O(1) space, where m is the number of rows and n is the number of columns.


### Koko Eating Bananas

- [Koko Eating Bananas](binary_search/koko_eating_bananas/): A solution to find the minimum eating speed for Koko to finish all bananas within a given time.

#### Possible solutions

Here are some possible approaches to solve the Koko Eating Bananas problem:

1. **Binary Search on Eating Speed**: Use binary search to find the minimum eating speed that allows Koko to finish the bananas in time.
    - complexity: O(n log m) time, O(1) space, where n is the number of piles and m is the maximum number of bananas in a pile.

### Find Minimum in Rotated Sorted Array

- [Find Minimum in Rotated Sorted Array](binary_search/find_minimum_in_rotated_sorted_array/): A solution to find the minimum element in a rotated sorted array.

#### Possible solutions

Here are some possible approaches to solve the Find Minimum in Rotated Sorted Array problem:

1. **Modified Binary Search**: Use binary search to find the point of rotation and identify the minimum element.
    - complexity: O(log n) time, O(1) space.

### Search in Rotated Sorted Array

- [Search in Rotated Sorted Array](binary_search/search_in_rotated_sorted_array/): A solution to search for a target value in a rotated sorted array.

#### Possible solutions

Here are some possible approaches to solve the Search in Rotated Sorted Array problem:

1. **Brute Force Approach**: Iterate through the array to find the target value.
    - complexity: O(n) time, O(1) space.

2. **Modified Binary Search**: Use binary search while accounting for the rotation to find the target value.
    - complexity: O(log n) time, O(1) space.


### Time Based Key-Value Store

- [Time Based Key-Value Store](binary_search/time_based_key_value_store/): A solution to implement a time-based key-value store.

#### Possible solutions

Here are some possible approaches to solve the Time Based Key-Value Store problem:

1. **Binary Search on Timestamps**: Use a hash map to store lists of (timestamp, value) pairs for each key and perform binary search on the timestamps to retrieve values.
    - complexity: O(log n) time for get operations, O(1) time for set operations, O(m) space, where n is the number of timestamps for a key and m is the total number of entries.

### Median of Two Sorted Arrays

- [Median of Two Sorted Arrays](binary_search/median_two_sorted_arrays/): A solution to find the median of two sorted arrays.

#### Possible solutions

Here are some possible approaches to solve the Median of Two Sorted Arrays problem:

1. **Merge and Find Median**: Merge the two arrays and find the median of the merged array.
    - complexity: O(m + n) time, O(m + n) space, where m and n are the lengths of the two arrays.
2. **Binary Search Approach**: Use binary search to partition the arrays and find the median without fully merging them.
    - complexity: O(log(min(m, n))) time, O(1) space, where m and n are the lengths of the two arrays.


## Linked Lists

Below are some of the linked list-related problems I've solved:

### Reverse Linked List

- [Reverse Linked List](linkedlists/reverse_linked_list/): A solution to reverse a singly linked list.

#### Possible solutions

Here are some possible approaches to solve the Reverse Linked List problem:

1. **Iterative Two-Pointer Approach**: Use two pointers to reverse the linked list iteratively.
    - complexity: O(n) time, O(1) space.

2. **Recursive Approach**: Use recursion to reverse the linked list.
    - complexity: O(n) time, O(n) space (due to recursion stack).


### Merge Two Sorted Lists

- [Merge Two Sorted Lists](linkedlists/merge_two_sorted_lists/): A solution to merge two sorted linked lists into one sorted linked list.

#### Possible solutions

Here are some possible approaches to solve the Merge Two Sorted Lists problem:

1. **Iterative Approach**: Use pointers to traverse both lists and merge them into a new sorted list.
    - complexity: O(n + m) time, O(1) space, where n and m are the lengths of the two lists.


### Linked List Cycle Detection

- [Linked List Cycle Detection](linkedlists/linked_list_cycle_detection/): A solution to detect if a linked list has a cycle.

#### Possible solutions

Here are some possible approaches to solve the Linked List Cycle Detection problem:

1. **Floyd's Tortoise and Hare Algorithm**: Use two pointers moving at different speeds to detect a cycle.
    - complexity: O(n) time, O(1) space.

### Reorder List

- [Reorder List](linkedlists/reorder_list/): A solution to reorder a linked list in a specific pattern.

#### Possible solutions

Here are some possible approaches to solve the Reorder List problem:

1. **Find Middle, Reverse Second Half, Merge**: Find the middle of the list, reverse the second half, and then merge the two halves.
    - complexity: O(n) time, O(1) space.ef head:

### Remove Nth Node From End of List

- [Remove Nth Node From End of List](linkedlists/remove_nth_node_from_end_of_list/): A solution to remove the nth node from the end of a linked list.

#### Possible solutions

Here are some possible approaches to solve the Remove Nth Node From End of List problem:

1. **Two-Pointer Approach**: Use two pointers to find the nth node from the end and remove it.
    - complexity: O(n) time, O(1) space.

### Copy List with Random Pointer

- [Copy List with Random Pointer](linkedlists/copy_list_with_random_pointer/): A solution to create a deep copy of a linked list with random pointers.

#### Possible solutions

Here are some possible approaches to solve the Copy List with Random Pointer problem:

1. **Hash Map Approach**: Use a hash map to store the mapping of original nodes to their copies and handle random pointers.
    - complexity: O(n) time, O(n) space.

### Add Two Numbers

- [Add Two Numbers](linkedlists/add_two_numbers/): A solution to add two numbers represented as linked lists.

#### Possible solutions

Here are some possible approaches to solve the Add Two Numbers problem:

1. **Iterative Approach**: Traverse both linked lists, add corresponding digits, and handle carry.
    - complexity: O(max(m, n)) time, O(max(m, n)) space, where m and n are the lengths of the two lists.


### Find the duplicate Number

- [Find the duplicate Number](linkedlists/find_duplicate_number/): A solution to find the duplicate number in an array where numbers are in the range 1 to n.

#### Possible solutions

Here are some possible approaches to solve the Find the Duplicate Number problem:

1. **Floyd's Tortoise and Hare Algorithm**: Use two pointers to detect a cycle in the linked list representation of the array.
    - complexity: O(n) time, O(1) space.

### LRU Cache

- [LRU Cache](linkedlists/lru_cache/): A solution to implement a Least Recently Used (LRU) cache.

#### Possible solutions

Here are some possible approaches to solve the LRU Cache problem:

1. **Doubly Linked List and Hash Map**: Use a doubly linked list to maintain the order of usage and a hash map for O(1) access to cache items.
    - complexity: O(1) time for get and put operations, O(capacity) space.


### Merge k Sorted Lists

- [Merge k Sorted Lists](linkedlists/merge_k_sorted_list/): A solution to merge k sorted linked lists into one sorted linked list.

#### Possible solutions

Here are some possible approaches to solve the Merge k Sorted Lists problem:

1. **Merge Sort Approach**: Use a divide and conquer approach to merge the lists pairwise.
    - complexity: O(n log k) time, O(1) space, where n is the total number of nodes and k is the number of lists.

### Reverse Nodes in k-Group

- [Reverse Nodes in k-Group](linkedlists/reverse_node_in_k_group/): A solution to reverse nodes in k-group in a linked list.

#### Possible solutions

Here are some possible approaches to solve the Reverse Nodes in k-Group problem:

1. **Iterative Approach**: Use an iterative approach to reverse nodes in groups of k.
    - complexity: O(n) time, O(1) space.


## Trees

Below are some of the tree-related problems I've solved:

### Invert Binary Tree

- [Invert Binary Tree](trees/invert_binary_tree/): A solution to invert a binary tree.

#### Possible solutions

Here are some possible approaches to solve the Invert Binary Tree problem:

1. **Recursive Approach**: Recursively swap the left and right children of each node.
    - complexity: O(n) time, O(n) space (due to recursion stack).


### Maximum Depth of Binary Tree 

- [Maximum Depth of Binary Tree](trees/maximum_depth_of_binary_tree/): A solution to find the maximum depth of a binary tree. 

#### Possible solutions

Here are some possible approaches to solve the Maximum Depth of Binary Tree problem:

1. **Recursive Approach**: Recursively calculate the depth of left and right subtrees and return the maximum. - complexity: O(n) time, O(n) space (due to recursion stack). 

2. **Iterative Approach**: Use a queue for level order traversal to calculate the depth iteratively. - complexity: O(n) time, O(n) space.

3. **Depth-First Search (DFS)**: Use a stack to perform DFS and calculate the depth. - complexity: O(n) time, O(n) space (due to stack).

### Diameter of Binary Tree

- [Diameter of Binary Tree](trees/diameter_of_binary_tree/): A solution to find the diameter of a binary tree.

#### Possible solutions

Here are some possible approaches to solve the Diameter of Binary Tree problem:

1. **Recursive Approach**: Use a recursive function to calculate the depth of the tree while updating the diameter at each node.
    - complexity: O(n) time, O(n) space (due to recursion stack).