def find_integer_with_most_divisors(input_list):
    test_list=[]
    
    for i in input_list:
        c=0
        for n in range (1,i+1):
            if i%n==0:
                c+=1
        test_list.append(c)
    #print(test_list)
    #print(test_list.index(max(test_list)))
    return input_list[test_list.index(max(test_list))]
