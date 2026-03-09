# PASSWORD STRENGTH CHECKER

pow = input("Enter password: ")

lambai_ok = False
numero_ok = False
abc_ok = False

if len(pow) >= 8:
    lambai_ok = True

    for ch in pow:
       if ch.isdigit():
        numero_ok = True
       if ch.isalpha():
        abc_ok = True

    if lambai_ok and numero_ok and abc_ok:
        print("Strong password")
    elif (numero_ok and abc_ok):
        print("Medium password")
    else:
        print("Weak password")

else:
    print("My dog has a strong password than this....Try Again!")
