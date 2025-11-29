n = input().strip()

if "." in n:
    int_part, dec_part = n.split(".")
    if int(dec_part) == 0:
        print("int", int_part)
    else:
        print("float", int_part, "0." + dec_part)
else:
    print("int", n)
