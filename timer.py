import time
import json
from matplotlib import pyplot as plt

times_file = open(r"times.txt", "r+")
file_text = times_file.read()
times = json.loads(file_text)

while True:
    print("hit enter to start, t for table, e for exit")
    user_in = input()

    if(user_in == ""):
        print("start:")
        curr_time = time.time()
        
        if(input() == ""):
            print("stop:")
            new_time = time.time()
 
        result = new_time - curr_time
        print("your time:")
        print(result)
        
        print("keep this time? type anything for yes, n for no)")
        if(input() != "n"):
            times.append(result)

    elif(user_in == "t"):
        plt.plot(times)
        plt.show()
    else:
        break
    

times_file.close()

json_string = json.dumps(times)
times_file = open(r"times.txt", "w")
times_file.write(json_string)
