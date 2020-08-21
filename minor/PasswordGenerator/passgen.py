# module name 'random' imported It's a built-in module 
import random
# string module imported It's a built-in Module 
import string

if __name__ == "__main__":
    # it contains lowercase alphabets
    s1 = string.ascii_lowercase
    # it contains Uppercase letters
    s2 = string.ascii_uppercase
    # it contains numericals/digits 
    s3 = string.digits
    # it contains punchuations {for,ex = "{},/!@#%^"}etc
    s4 = string.punctuation
    # plen takes input form user in int datatype
    plen = int(input("Enter The password length\n")) #Todo1 : Handle Gibbersish
    # Empty list
    s = []
    # This method add s1 into empty-list s
    s.extend(list(s1))
    # This method add s2 into empty-list s
    s.extend(list(s2))
    # This method add s3 into empty-list s
    s.extend(list(s3))
    # This method add s4 into empty-list s
    s.extend(list(s4))
    print("Your password is:\n")
    print("".join(random.sample(s, plen)))