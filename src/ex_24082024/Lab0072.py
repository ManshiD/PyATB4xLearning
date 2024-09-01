def print_arguments(*args):
    #*args = multiple arguments with no limits, -> list
    #print(args[0])
    for i in args:
        print(i)

print_arguments("ARGUMENT Line 1:","pramod","amit","lucky")
print_arguments("ARGUMENT Line 2:","amit","lucky")
print_arguments("ARGUMENT Line 3:","amit",10)
print_arguments("ARGUMENT Line 4:","amit",10,True)
print_arguments("ARGUMENT Line 5:","amit",10,True,False)
print_arguments("ARGUMENT Line 6:","amit",10,True, False,"PRAMOD")
print_arguments("ARGUMENT Line 7:","lucky")