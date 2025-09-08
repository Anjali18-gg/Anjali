def fibonacci(n):
    a,b = 0,1
    while a<n:
        yield a
        a,b = b,a+b

for num in fibonacci(10):
    print(num)  #outputs:0,1,1,2,3,5,8
print("This code is written and executed by Anjali_0231BCA188")    
