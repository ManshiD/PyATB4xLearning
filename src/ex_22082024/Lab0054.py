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
        print("No O/P")

# | i | Condition | O/P
# | 0 | 0 == 6 -> False | O/P -> No O/P
# | 1 | 1 == 6 -> False | O/P -> No O/P
# | 2 | 2 == 6 -> False | O/P -> No O/P
# | 3 | 3 == 6 -> False | O/P -> No O/P
# | 4 | 4 == 6 -> False | O/P -> No O/P
# | 5 | 5 == 6 -> False | O/P -> No O/P
# | 6 | 6 == 6 -> True | O/P -> 6
# | 7 | 7 == 6 -> False | O/P -> No O/P
# | 8 | 8 == 6 -> False | O/P -> No O/P
# | 9 | 9 == 6 -> False | O/P -> No O/P
