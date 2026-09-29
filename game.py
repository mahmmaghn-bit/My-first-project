import random

def guess_number():
    print("أهلاً بك في لعبة تخمين الرقم!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("خمن رقماً بين 1 و 100: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("الرقم صغير جداً، حاول مرة أخرى.")
            elif guess > number_to_guess:
                print("الرقم كبير جداً، حاول مرة أخرى.")
            else:
                print(f"مبروك! لقد فزت بعد {attempts} محاولة.")
                break
        except ValueError:
            print("الرجاء إدخال رقم صحيح.")

if __name__ == "__main__":
    guess_number()
