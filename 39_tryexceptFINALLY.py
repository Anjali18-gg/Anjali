try:
    file = open('example.txt','r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error:The file was not found.")
finally:
    file.close()  #ensures the file is closed whether or not an exception occured)
    
print("This code is written and executed by Anjali_0231BCA188")    
