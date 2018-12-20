while True:
    try:
        num = int(input('Enter a number: '))
    except ValueError:
        print ("The input must be a integer!")
        continue
    break
    
guess = num / 1.3
middle = num / 2
step = 0

while guess != num:
    if num > guess:
        guess += middle
        print (("I guess: "), guess)
    elif num < guess:
        guess -= middle
        print (("I guess: "), guess)
    middle /= 2
    if middle == 0:
        middle = 1
    step += 1

print (("Aha! The answer is: "), guess)
print (("I totally use %d steps.") % step)