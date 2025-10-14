# Let's call a string consisting of characters ( and ) a parenthesis sequence. 
# We will consider the parenthesis sequence to be correct if:

# for each opening parenthesis, there is a closing parenthesis.
# The brackets are closed in the correct order, that is, in each pair of opening and closing brackets, the opening one is to the left.
# Write a program that determines whether the parenthesis sequence is correct.

stroka = input()
left_cnt = 0
right_cnt = 0


for el in stroka:
    if el == '(':
        