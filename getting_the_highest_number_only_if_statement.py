#variables for input, making input to int number 1, 2, 3, 4 and 5
var1 = int(input("insert a first number here: "))
var2 = int(input("insert a second number here: "))
var3 = int(input("insert a third number here: "))
var4 = int(input("insert a fourth number here: "))
var5 = int(input("insert a fifth number here: "))

#if any of the last variable are equal to one another! - this would not work considering it find the largest number, not the variable.

#create def find_largest_number and conditional statements
def find_largest_number(var1, var2, var3, var4, var5):
    #if var1 is larger than var2
    if var1 > var2:
        #if var1 is larger than var3:
        if var1 > var3:
            #if var1 is larger than var4:
            if var1 > var4:
                #if var1 is larger than var5:
                if var1 > var5:
                    return var1
                else:
                    return var5
            else:
                #if var4 larger than var5
                if var4 > var5:
                    return var4
                else:
                    return var5
        else: 
            #if var3 is larger than var4:
            if var3 > var4:
                #if var3 is larger than var5:
                if var3 > var5:
                    return var3
                else: 
                    return var5
            else:
                if var4 > var5:
                    return var4
                else:
                    return var5
    else:
        #var2 is larger than var3:
        if var2 > var3:
            #if var2 larger than var4:
            if var2 > var4:
                #if var2 larger than var5:
                if var2 > var5:
                    return var2
                else:
                    return var5
            else:
                if var4 > var5:
                    return var4
                else:
                    return var5
        else:
            #if var3 larger than var4:
            if var3 > var4:
                #if var3 larger than var5:
                if var3 > var5:
                    return var3
                else:
                    return var5
            else:
                
                if var4 > var5:
                    return var4
                else:
                    return var5
result = find_largest_number(var1, var2, var3, var4, var5)
print(f"The highest number is {result}")