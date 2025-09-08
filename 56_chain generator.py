def count_up_to(max):
    count = 1
    while count<=max:
        yield count
        count+=1

def squared_numbers(numbers):
    for number in numbers:
        yield number**2

for square in squared_numbers(count_up_to(5)):
    print(square)  #outputs:1,4,9,16,25
print("This code is written and executed by Anjali_0231BCA188")        
