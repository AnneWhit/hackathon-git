#!/usr/env/bin python

a = "Hello "
b = "It is so nice to meet you  "
c = input("What is your name?")

print(a+b+c)

d = input("How old are you?")
print(d + " is a great age!")

e = input("Do You speak English or Spanish?")
e = e.lower()
english = "I also speak English."
spanish = "Al espanol yo tambien hablo."


if e == "english":
    print(english)
    print("I am so happy, " + c + " that you are here with me today.")
    print("Trying to learn Github by myself is hard.")
if e == "spanish":
    print(spanish)
    print("Estoy tan feliz" + c + "que hoy estas aqui conmigo.")
    print("tratar de aprender github por mi cuenta es difficil.")
elif e != "english" and e != "spanish":
    print("[-] Please enter either English or Spanish.")

    