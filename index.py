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
    print("I am so happy, " + c +" that you are here with me today.")
    print("Trying to learn Github by myself is hard.")
if e == "Spanish":
     print(Spanish)
     print("Estoy tan feliz" + c + "que hoy estas aqui conmigo.")
     print("tratar de aprender github por mi cuenta es difficil.")
elif e != "English" and e != "Spanish":
    print("[-] Please enter either English or Spanish.")



    
