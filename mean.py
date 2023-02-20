def meaN(value):
    if type(value) == dict:
       the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
student_grades = {"Marry": 9.1,"Sim": 8.8, "John": 7.5}
print(meaN(student_grades))
print(meaN(monday_temperatures))


x = 3
y = 1
if x > y:
    print("X is greater than Y")
elif x == y:
    print("X is equal to Y")
else:
    print("X is less than Y")


if      3 > 1:
    print('a')

print('aa')
print('aaa')

if 3>1:
    print('b')

print('bb')
print('bbb')

if 3 > 1:
    print('c')

print('cc')
print('ccc')


message = "hello there"

if "hello" in message:
    print("hi")
else:
    print("I don't understand")


def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter temperature:"))
print(weather_condition(user_input))

