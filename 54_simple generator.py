def count_up_to(max):
    count = 1
    while count<=max:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)  #outputs:1,2,3,4,5
print("This code is written and executed by Anjali_0231BCA188")    
