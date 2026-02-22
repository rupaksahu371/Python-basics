#INPUT STRING OR INTEGER AND ADD THEM

def check_user_input(a,b):
    try:
        # Convert it into integer
        val0 = int(a)
        val1 = int(b)
        val = val0+val1
        print(val)
        
    except ValueError:
        try:
            # Convert it into float
            val0 = float(a)
            val1 = float(b)
            
        except ValueError:
            # Convert it into string
            val0 =str(a)
            val1 =str(b)
            
            #PRINT A+B
            
            val = val0+val1
            print(val)

check_user_input(input("ENTER A:"),input("ENTER B:    "))