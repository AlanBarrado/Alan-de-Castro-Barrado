import time

n = "nickname"
p = "password"
c = "maybe"

print("welcome, choose your nickname and password ")
time.sleep(1.5)
n = input ("enter nickname here: ")
time.sleep(1.5)
p = input("enter password here: ")
time.sleep(1.5)
print("your name is", (n), "and your password is", (p))
time.sleep(2)
c = input("is it correct? (s for yes and n for no)")

if (c == "s"):
    print("login set")
    time.sleep(1)
    print("enjoy your account")
    brake
elif (c == "n"):
    print("change your login")
    time.sleep(1)
    n = input ("enter nickname here: ")
    time.sleep(1)
    p = input("enter password here: ")
    time.sleep(1)
    print("your name is", (n), "and your password is", (p))
    time.sleep(1)
    c = input("is it correct? (s for yes and n for no)")
    time.sleep(1)

    if (c == "s"):
        print("login set")
        time.sleep(1)
        print("enjoy your account")
        brake
    elif (c == "n"):
        print("change your login")
        time.sleep(1)
        n = input ("enter nickname here: ")
        time.sleep(1)
        p = input("enter password here: ")
        time.sleep(1)
        print("your name is", (n), "and your password is", (p))
        time.sleep(1)
        c = input("is it correct? (s for yes and n for no)")
        time.sleep(1)

