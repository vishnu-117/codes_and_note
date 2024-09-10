echo "\
def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)
binaryToDecimal(100)
" | python3



python3 - <<'EOF'
def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)
binaryToDecimal(100)
EOF

exec("""
def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)
binaryToDecimal(100)
""")


Array:

Easy:
1)Remove Duplicates from Sorted Array
2)Best Time to Buy and Sell Stock II
3)Rotate Array
4)Contains Duplicate
5)Single Number
6)Intersection of Two Arrays II
7)Plus One
8)Move Zeroes
9)Two Sum
10)Valid Sudoku
11)Rotate Image

Medium:
1)"3Sum"
2)"Set Matrix Zeroes"
3)"Group Anagrams"
4)"Longest Substring Without Repeating Characters"
5)"Longest Palindromic Substring"
6)"Increasing Triplet Subsequence"
7)"Missing Ranges"
8)"Count and Say"

String:

Easy:
1)Reverse String
2)Reverse Integer
3)First Unique Character in a String
4)Valid Anagram
5)Valid Palindrome
6)String to Integer (atoi)
7)Implement strStr()
8)Longest Common Prefix

LinkedList:

Easy:
1)Delete Node in a Linked List
2)Remove Nth Node From End of List
3)Reverse Linked List
4)Merge Two Sorted Lists
5)Palindrome Linked List
6)Linked List Cycle

Medium:
1)"Add Two Numbers",
2)"Odd Even Linked List",
3)"Intersection of Two Linked Lists",


Tree:

Easy:
1)Maximum Depth of Binary Tree
2)Validate Binary Search Tree
3)Symmetric Tree
4)Binary Tree Level Order Traversal
5)Convert Sorted Array to Binary Search Tree

Medium:
1)"Binary Tree Inorder Traversal",
2)"Binary Tree Zigzag Level Order Traversal",
3)"Construct Binary Tree from Preorder and Inorder Traversal",
4)"Populating Next Right Pointers in Each Node",
5)"Kth Smallest Element in a BST",
6)"Inorder Successor in BST",
7)"Number of Islands",



Sorting & searching:

Easy:
1)Merge Sorted Array
2)First Bad Version

Medium:
1)"Sort Colors",
2)"Top K Frequent Elements",
3)"Kth Largest Element in an Array",
4)"Find Peak Element",
5)"Search for a Range",
6)"Merge Intervals",
7)"Search in Rotated Sorted Array",
8)"Meeting Rooms II",
9)"Search a 2D Matrix II",

Backtraking:
1)"Letter Combinations of a Phone Number",
2)"Generate Parentheses",
3)"Permutations",
4)"Subsets",
5)"Word Search",

Dp:

Easy:
1)Climbing Stairs
2)Best Time to Buy and Sell Stock
3)Maximum Subarray
4)House Robber

Medium:
1)"Jump Game",
2)"Unique Paths",
3)"Coin Change",
4)"Longest Increasing Subsequence",

Math:

Medium:
1)"Happy Number",
2)"Factorial Trailing Zeroes",
3)"Excel Sheet Column Number",
4)"Pow(x, n)",
5)"Divide Two Integers",
6)"Fraction to Recurring Decimal",


Other:

Easy:
1)Number of 1 Bits
2)Hamming Distance
3)Reverse Bits
4)Pascal's Triangle
6)Valid Parentheses
7)Missing Number

Medium:
1)"Sum of Two Integers",
2)"Evaluate Reverse Polish Notation",
3)"Majority Element",
4)"Find the Celebrity",
5)"Task Scheduler",



os:
https://www.youtube.com/watch?v=_hrKEA1sEUo&list=PLDzeHZWIZsTr3nwuTegHLa2qlI81QweYG&index=33
https://www.almabetter.com/bytes/articles/cpu-scheduling-in-os
https://takeuforward.org/operating-system/most-asked-operating-system-interview-questions
https://leetcode.com/discuss/study-guide/4043781/OS-Last-Minute-Revision
https://github.com/aghosh0605/os-notes-2022?tab=readme-ov-file
https://www.gatevidyalay.com/paging-formulas-practice-problems/

NOsql db:
https://pandorafms.com/blog/nosql-databases-the-definitive-guide/

mysql db internals:
https://dev.to/gbengelebs/unboxing-a-database-how-databases-work-internally-155h

aws:
https://www.youtube.com/watch?v=9OpRBa0CNRw&list=PL6XT0grm_TfgtwtwUit305qS-HhDvb4du&index=27
https://aws-dojo.com/workshoplists/

Dsa:
https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/