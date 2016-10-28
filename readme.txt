https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/

Main challenge: Write a function that, given a 4-digit number, returns the largest digit in that number. Numbers between 0 and 999 are counted as 4-digit numbers with leading 0's.

Bonus 1: Write a function that, given a 4-digit number, performs the "descending digits" operation. This operation returns a number with the same 4 digits sorted in descending order.
Bonus 2: Write a function that counts the number of iterations in Kaprekar's Routine, which is as follows.
Given a 4-digit number that has at least two different digits, take that number's descending digits, and subtract that number's ascending digits. For example, given 6589, you should take 9865 - 5689, which is 4176. Repeat this process with 4176 and you'll get 7641 - 1467, which is 6174.
Once you get to 6174 you'll stay there if you repeat the process. In this case we applied the process 2 times before reaching 6174, so our output for 6589 is 2.

Output:
Main Challenge:
largest_digit(1234) -> 4
largest_digit(3253) -> 5
largest_digit(9800) -> 9
largest_digit(3333) -> 3
largest_digit(120) -> 2

Bonus 1:
desc_digits(1234) -> 4321
desc_digits(3253) -> 5332
desc_digits(9800) -> 9800
desc_digits(3333) -> 3333
desc_digits(120) -> 2100

Bonus 2:
kaprekar(6589) -> 2
kaprekar(5455) -> 5
kaprekar(6174) -> 0
