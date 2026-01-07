L = [1,2,3,4,"strings", True, False, 1.23,4.4] # mutable
#print(L, "before appending")
D = {"name": "ravi", "address":"india"} # mutable
T = (1,2,3,4,"strings", True, False, 1.23,4.4) # immutable
S = {1,2,3,4,"strings", True, False, 1.23,4.4} # mutable, unordered and doest keey duplicated

# L.append("appending my name")

# print(L, "after appending")

########### 1 scripting , 2. OOP manner
#### classes and objects methods

def check_package_version1(arg):
    if type(arg) == "":
        return "python version is" + arg
    else:
        return "please provide string as function arguments"
    
def check_package_version2(arg):
    if type(arg) == "":
        return "python version is" + arg
    else:
        return "please provide string as function arguments"

def check_package_version3(arg):
    if type(arg) == "":
        return "python version is" + arg
    else:
        return "please provide string as function arguments"
    
def check_package_version4(arg):
    if type(arg) == "":
        return "python version is" + arg
    else:
        return "please provide string as function arguments"

# res = check_package_version1(3.12)
# print(res)


class Combining_All_Function:
    def check_package_version1(self, arg):
        if type(arg) == "":
            print("printed something!!")
            return "python version is" + arg
        else:
            print("printed something else")
            return "please provide string as function arguments"
        
    def check_package_version2(self, arg):
        if type(arg) == "":
            print("method two is being called")
            return "python version for second method" + arg
        else:
            print("second method is being calles inside else condition")
            return "please provide string as function arguments"

    def check_package_version3(self, arg):
        if type(arg) == "":
            return "python version is" + arg
        else:
            return "please provide string as function arguments"
        
    def check_package_version4(self, arg):
        if type(arg) == "":
            return "python version is" + arg
        else:
            return "please provide string as function arguments"


class Combining_All_Function1(Combining_All_Function):
    def check_package_version1(self, arg):
        if type(arg) == "":
            print("printed something!!")
            return "python version is" + arg
        else:
            print("printed something else")
            return "please provide string as function arguments"
        
    def check_package_version2(self, arg):
        if type(arg) == "":
            print("method two is being called")
            return "python version for second method" + arg
        else:
            print("second method is being calles inside else condition")
            return "please provide string as function arguments"

    def check_package_version3(self, arg):
        if type(arg) == "":
            return "python version is" + arg
        else:
            return "please provide string as function arguments"
        
    def check_package_version4(self, arg):
        if type(arg) == "":
            return "python version is" + arg
        else:
            return "please provide string as function arguments"



test_class_obj1 = Combining_All_Function()
test_class_obj1.check_package_version1(3.10)
test_class_obj2 = Combining_All_Function()
test_class_obj2.check_package_version2("3.14")
test_class_obj3 = Combining_All_Function()
test_class_obj4 = Combining_All_Function()
