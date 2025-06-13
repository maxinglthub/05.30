#Hi

done = False
answer_first_num = 0
answer_num = 0
check = 0

answer = input("Enter some integers: ")
answer_first_num = int(answer)

while (not done):
    answer = input("Enter some integers: ")
    if answer == "0" and check == 1:
        done = True
        print("Total: ", int(answer_num + answer_first_num))
    elif answer == "0" and check == 0:
        done = True
        print("Total: ", int(answer_first_num))
    else:
        answer_num = int(answer_num) + int(answer)
        answer = 0
        check = 1



print("hello" < "hi")
