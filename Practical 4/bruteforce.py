import itertools
import string

def bruteForce(target):
    characters = string.ascii_letters + string.digits + string.punctuation
    target_len = len(target)
    attempt_count = 0
    # for attempts in itertools.product(characters, repeat=target_len):
    #     guess = ''.join(attempts)
    #     attempt_count += 1
    #     if guess == target:
    #         return attempt_count
    for length in range(target_len):
        for attempts in itertools.product(characters, repeat=target_len):
            guess = ''.join(attempts)
            attempt_count += 1
            if guess == target:
                return attempt_count
            
target = input("Enter password to attack: ")
attempt_count = bruteForce(target)

if attempt_count:
    print(f"Password found in : {attempt_count} attempts")
else:
    print("Password not found")