text = "Hello,world!"

#changing case
lowercase_text = text.lower()  #"Hello,world!"
uppercase_text = text.upper()  #"Hello,world!"
title_text = text.title()      #"Hello,world!"

#Trimming whitespace
stripped_text = text.strip()    #"Hello,world!"
left_stripped_text = text.lstrip()  #"Hello,world!"
right_stripped_text = text.rstrip()  #"Hello,World!"

#splitting and joining
words = stripped_text.split(",")  #['Hello','world!']
joined_text = "-".join(words)  #"Hello- world!"

#replacing and finding
replaced_text = stripped_text.replace("world", "Python")  #"Hello, Python!"
index = stripped_text.find("world!")   #7
count = stripped_text.count("o")   #2

print(lowercase_text)
print(uppercase_text)
print(title_text)
print(stripped_text)
print(left_stripped_text)
print(right_stripped_text)
print(words)
print(joined_text)
print(replaced_text)
print(index)
print(count)

print("This code is written and executed by Anjali_0231BCA188")
