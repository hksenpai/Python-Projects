import math,random
def check_guess(num,expected_num):
    if(num<expected_num):
        print("your guess is low")
        return -1
    elif(num>expected_num):
        print("your guess is high")
        return 1
    else:
        return 0

print("enter lower bound of number")
lower_bound=int(input())
print("enter lower bound of number")
upper_bound=int(input())
expected_num=random.randint(lower_bound,upper_bound)
no_guesses=int(math.ceil(math.log(upper_bound-lower_bound+1,2)))
print(no_guesses)
user_guesses=1
while(user_guesses<=no_guesses):
    print("enter your guess")
    num=int(input())
    if check_guess(num,expected_num)==0:
        print("Correct! you guessed the answer in ",user_guesses," attempts")
        exit(0)
    user_guesses+=1
print("Maximum guesses reached !")
