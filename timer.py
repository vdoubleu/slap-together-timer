import time
import json
import keyboard
from matplotlib import pyplot as plt

times_file = open(r"times.txt", "r+")
file_text = times_file.read()
times = json.loads(file_text)

print("press space to start, t for table n to remove lasts one and e/anything else for exit")

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
            
            print("press space to start, t for table, n to remove last one and e/anything else for exit")
            time.sleep(0.25)

        elif keyboard.is_pressed('t'):
            plt.plot(times)
            plt.show()
            print("press space to start, t for table, n to remove last one and e/anything else for exit")
        elif keyboard.is_pressed('n'):

            times.pop()
            print("press space to start, t for table, n to remove last one and e/anything else for exit")
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
