import time
import json
import keyboard
from matplotlib import pyplot as plt
from random import seed
from random import choice
import numpy as np
from numpy.polynomial.polynomial import polyfit


def print_scramble(possible_moves):
    for x in range(0, 15):
        print(choice(possible_moves), end=" ")
    print()

def main():
    possible_moves = ("R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "B", "B'", "B2", "F", "F'", "F2")

    seed(1)

    times_file = open(r"times.txt", "r+")
    file_text = times_file.read()
    times = json.loads(file_text)
    
    print_scramble(possible_moves)
    print("press space to start, t for table n to remove lasts one and e for exit")

    while True:
        try:
            if keyboard.is_pressed(' '):
                print('start:')
                curr_time = time.time()

                time.sleep(0.25)
                
                keyboard.wait(' ')
                print("stop:")
                new_time = time.time()
            
                result = new_time - curr_time
                print("your time:")
                print(result)
                        
                times.append(result) 
                
                print_scramble(possible_moves)
                print("press space to start, t for table, n to remove last one and e for exit")
                time.sleep(0.25)

            elif keyboard.is_pressed('t'):
                plt.plot(times)
                x = np.array(list(range(1, len(times))))
                d, c, b, a = polyfit(x, np.array(times), 3)
                plt.plot(x, a*(x**3) + b*(x**2) + c*x + d, "-")
                
                
                plt.show()
                print_scramble(possible_moves)
                print("press space to start, t for table, n to remove last one and e for exit")
            elif keyboard.is_pressed('n'):

                times.pop()
                print_scramble(possible_moves)
                print("press space to start, t for table, n to remove last one and e for exit")
                time.sleep(0.25)
            elif keyboard.is_pressed('e'):
                

                print("exit")
                break

        except:
            print("error")
            break


    times_file.close()

    json_string = json.dumps(times)
    times_file = open(r"times.txt", "w")
    times_file.write(json_string)


if __name__ == "__main__":
    main()
