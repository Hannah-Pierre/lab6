print "how many numbers do you want to add"
userinput = int(raw_input())
total = 0
for x in range(userinput) :
    print "enter a number"
    userinput2 = int(raw_input())
    total = total + userinput2
print total 

list1 =[]
print "how many numbers do you want to add"
userinput = int(raw_input())
for x in range(userinput) :
    print "enter a number"
    userinput2 = int(raw_input())
    list1.append(userinput2)
print sum(list1)

print "what number do you want to print the factoral of?"
userinput3 = int(raw_input())
total = 1 
for x in range(1,userinput3 + 1, 1) :
    total = total * x
print total

userinput4 = int(raw_input())
print "what number do you want to find the factors of?"
for x in range(1,userinput4 + 1) :
    if userinput4 % x == 0 :
        print x