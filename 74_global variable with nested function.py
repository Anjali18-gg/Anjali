global_var="I am global"
def outer_function():
    global global_var
    def inner_function():
        global_var="I am modified in inner"
        print(global_var)
    print(global_var)
    inner_function()
outer_function()
print(global_var)  #output:I am modified in inner
print("This code is written and executed by Anajli_0231BCA188")
