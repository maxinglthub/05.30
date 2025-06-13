hour = 0
min = 0
sec = 0

num = int(input("pls enter the number of seconds: "))

hour = num // 3600
min = (num - hour * 3600) // 60
sec = num - hour * 3600 - min * 60

print(hour, "hour", min, "min", sec, "sec")