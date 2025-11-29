a = float(input())
if a >= 0:
    if a <= 25:
        print("Interval [0,25]")
    else: #a > 25:
        if a <= 50:
            print("Interval (25,50]")
        else: # a > 50
            if a <= 75:
                print("Interval (50,75]")
            else:
                if a <= 100:
                    print("Interval (75,100]") 
                else:
                    print("Out of Intervals") 
else:
    print("Out of Intervals")                                