def main():
    value=convert(input("Fraction: "))
    print(gauge(value))



def convert(fraction):
    while True:
         array=fraction.split("/")
         X=int(array[0])
         Y=int(array[1])
         if Y==0:
             raise ZeroDivisionError
         elif X>Y:
             raise ValueError
         elif len(array)>2:
             continue
         else:
             answer=X/Y
             rounded_answer=round(answer*100)
             return rounded_answer




def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
