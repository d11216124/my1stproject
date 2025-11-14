# 猜數字遊戲
import random                       
def guess_number_game():
    number_to_guess = random.randint(1, 100)  
    attempts = 0                             
    print("歡迎來到猜數字遊戲！請在1到100之間猜一個數字。")

    while True:
        try:
            user_guess = int(input("請輸入你的猜測："))  
            attempts += 1                             

            if user_guess < 1 or user_guess > 100:
                print("請輸入1到100之間的數字。")
                continue

            if user_guess < number_to_guess:
                print("太小了！再試一次。")
            elif user_guess > number_to_guess:
                print("太大了！再試一次。")
            else:
                print(f"恭喜你！猜對了，答案是 {number_to_guess}。你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入一個有效的整數。")
if __name__ == "__main__":
    guess_number_game()
    