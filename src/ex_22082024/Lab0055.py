# Break - Based on condition, exit the loop
#for i in range (0, 10, 1): # 0 to 9, start
#    print(i)

# range(0, 10, 1)
# range(0, 10)
# range(10)

for i in range (0, 10, 1): # 0 to 9, start
    if i == 6:
        print(i)
    else:
        pass


# | i | Condition | O/P
# | 0 | 0 == 6 -> False |
# | 1 | 1 == 6 -> False |
# | 2 | 2 == 6 -> False |
# | 3 | 3 == 6 -> False |
# | 4 | 4 == 6 -> False |
# | 5 | 5 == 6 -> False |
# | 6 | 6 == 6 -> True | O/P -> 6
# | 7 | 7 == 6 -> False |
# | 8 | 8 == 6 -> False |
# | 9 | 9 == 6 -> False |
