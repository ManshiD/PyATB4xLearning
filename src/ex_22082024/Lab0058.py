# Continue Statement
# Continue statement skips the current iteration of a loop and
# moves to the next iteration.

for number in range(10):
    if number % 2 == 0:
        continue
        #pass
    else:
        print(number)

# | i | Condition | O/P
# | 0 | 0 % 2 == 0 - True | continue - skip No O/P for even nos we will continue no putput
# | 1 | 1 % 2 is not equal to 0 - False | O/P -> No Output for odd nos we will print
# | 2 | 2 % 2 == 0 - True | continue - skip No O/P for even nos we will continue no putput
# | 3 | 3 % 2 is not equal to 0 - False | O/P -> No Output for odd nos we will print
# | 4 | 4 % 2 == 0 - True | continue - skip No O/P for even nos we will continue no putput
# | 5 | 5 % 2 is not equal to 0 - False | O/P -> No Output for odd nos we will print
# | 6 | 6 % 2 == 0 - True | continue - skip No O/P for even nos we will continue no putput
# | 7 | 7 % 2 is not equal to 0 - False | O/P -> No Output for odd nos we will print

# pass - can be used in the statement, functions, class and objects
