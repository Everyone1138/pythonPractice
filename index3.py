import time

while True:
    with open("assets/text.txt") as file:
        print(file.read())
        time.sleep(10)