# Prompts the user for a level, If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
# If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.



import random


def main():
    score=0
    level=get_level()
    for _ in range(10):
         try:
             tries=0
             expression=generate_integer(level)
             X=expression[0]
             Y=expression[1]
             realAnswer=X+Y
             answer=int(input(f"{X} + {Y} = "))
             while True:
                     try:
                         if answer==realAnswer:
                            score+=1
                            break
                         elif answer != realAnswer:
                            tries+=1
                            if tries==3:
                                print('EEE')
                                print(f"{X} + {Y} = {realAnswer}")
                                break
                            else:
                                print('EEE')
                                answer=int(input(f"{X} + {Y} = "))
                                continue
                     except ValueError:
                         continue

         except ValueError:
               answer=-99999999999
               while True:
                try:
                    if tries==3:
                            print('EEE')
                            print(f"{X} + {Y} = {realAnswer}")
                            break
                    elif answer==realAnswer:
                        score+=1
                        break
                    else:
                        tries+=1
                        print('EEE')
                        answer=int(input(f"{X} + {Y} = "))
                        continue
                except ValueError:
                     continue


    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level==1 or level==2 or level==3:
                break
            else:
                continue
        except ValueError:
            continue
    return level


def generate_integer(level):
    if level==1:
        X=random.randrange(0,10)
        Y=random.randrange(0,10)
    elif level==2:
        X=random.randrange(10,100)
        Y=random.randrange(10,100)
    elif level==3:
        X=random.randrange(100,1000)
        Y=random.randrange(100,1000)
    return X,Y





if __name__ == "__main__":
    main()
