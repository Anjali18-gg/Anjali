#Bytes Example
print("Bytes Example:")
#Creating a bytes object
b = bytes([65,66,67,68])
print(b) #Output:b'ABCD'

#Accessing elements in a bytes object
print(b[0]) #Output: 65
print(b[1]) #Output: 66

#Iterating through a bytes object
for byte in b:
    print(byte, end='') #Output:65 66 67 68
    print("\n")

#Bytearray Example
    print("Bytearray Example:")
    #Creating a bytearray object
    ba = bytearray([65,66,67,68])
    print(ba) #Output:bytearray(b'aBCD')

#Modifying elements in a bytearray
    ba[0] = 97 #Changing'A'(654)to'a'(97)
    print(ba) #Output: bytearray(b'aBCD')

#Adding elements to a bytearray
    ba.append(69) #Adding 'E'(69)
    print(ba) #Output: bytearray(b'aBCDE')

#converting bytearray to bytes
    b_converted = bytes(ba)
    print(b_converted) #output: b'aBCDE'
    print("\n")

#memoryview example
    print("Memoryview Example:")
          #creating a bytes object
    ba_mv = bytes([65,66,67,68,69])

#creating a memoryview object
    mv = memoryview(ba_mv)
    print(mv) #output: <memory at 0x00000123456789AB>

#accessing elements through memoryview
    print(mv[0]) #output: 65

#slicing memoryview
    mv_slice = mv[1:4]
    print(mv_slice.tobytes()) #output: b'BCD'

#creating a bytearray and a memoryview
    ba_mv = bytearray([65,66,67,68,69])
    mv_ba = memoryview(ba_mv)

#modifying the original bytearray through memoryview
    mv_ba[0] = 97 #changing'A'(65) to 'a'(97)
    print(ba_mv) #output: bytearray(b'aBCDE')
    print("This code is written by Anjali_0231BCA188")
          
          

    
