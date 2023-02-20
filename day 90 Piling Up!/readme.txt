There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example

Result: No

After choosing the rightmost element, , choose the leftmost element, . After than, the choices are  and . These are both larger than the top block of size .


Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.

Input Format

The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Constraints




Output Format

For each test case, output a single line containing either Yes or No.

Sample Input

STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]
Sample Output

Yes
No
Explanation

In the first test case, pick in this order: left - , right - , left - , right - , left - , right - .
In the second test case, no order gives an appropriate arrangement of vertical cubes.  will always come after either  or .

Language
Python 3

More
1234567891011
# Enter your code here. Read input from STDIN. Print output to STDOUT
for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left,reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
Line: 2 Col: 1

Submit Code

Run Code

Upload Code as File

Test against custom input
Python
You have earned 50.00 points!
51/115 challenges solved.
44%
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn
Next Challenge

Test case 0

Test case 1

Test case 2

Test case 3

Test case 4
Compiler Message
Success
Input (stdin)

Download
2
6
4 3 2 1 3 4
3
1 3 2
Expected Output

Download
Yes
No
