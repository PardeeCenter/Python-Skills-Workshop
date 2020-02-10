incorrect_value_count = 0
positive_int_count = 0
odd_count = 0
even_count = 0
odd_sum = 0
even_sum = 0
##
print("--> Input a positive integer, input of 0 will terminate this program.")
correct_input=False
while correct_input==False:
    num1_str = input("Input a positive integer: ")
    try:
        num1_int = int(num1_str)
        if num1_int>0:
            positive_int_count +=1
            if num1_int%2 != 0:
                odd_count += 1 
                odd_sum += num1_int
            else:
                even_count += 1
                even_sum += num1_int
            total_sum = odd_sum + even_sum
            
        elif num1_int ==0:
            print("--> Note: values of 0 terminate this program. \n")
            correct_input=True
            
        else:
            print("--> Input value not valid. Try again. \n")
            incorrect_value_count += 1
    except:
        print("--> Input value not valid. Try again. \n")
        incorrect_value_count += 1
##
print("And now for the totals")
print("sum of positive odds:", odd_sum)
print("sum of positive evens:", even_sum)
print("total positive sum: ", total_sum)
print("positive odd count:", odd_count)
print("positive even count:", even_count)
print("total positive int count:", positive_int_count)
print("total incorrect values count:", incorrect_value_count)