#!/usr/env/bin python

a= "Hello "
b= "It is so nice to meet you  "
c=raw_input("What is your name?")

print(a+b+c)

d = raw_input("How old are you?")
print(d + " is a great age!")

e = raw_input("Do You speak English or Spanish?")
English = "I also speak English."
Spanish = "Al espanol yo tambien hablo."


if e == "English":
    print(English)
if e == "Spanish":
     print(Spanish)
elif e != "English" and e != "Spanish":
    print("[-] Please enter either English or Spanish.")



    
