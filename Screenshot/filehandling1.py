# file = open("C:\\Users\\91738\\PycharmProjects\\DemoProject\\SecondPracticeProject\\Screenshot\\file_handling", "r")
# file = open("pavan.txt", "w")
# file.write('my name is pavan\ni am from rajampet')

import datetime
import time

for i in range(1,11):
    today_date = datetime.datetime.now()
    b = today_date.strftime("%d_%m_%Y_%H_%M_%S")
    file = open(b, "w")
    file.write(b)
    time.sleep(2)
    file.close()
    print(i)




