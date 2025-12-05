for num in range (1, 21):
    if num % 3 == 0:
        continue # skip numbers divisible by 3

    if num == 15:
        break #sop the loop completely

    print(num)
