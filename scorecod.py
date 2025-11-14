#分數計算功能設計
#1.	設計簡單的分數計算器：輸入考試成績，程式自動計算平均分數。
#2.	加入錯誤處理：遇到非數字輸入時，提示「請輸入有效分數」。
#3.	每次修改後，使用 GitHub 進行版本管理，留下註解。
def score_calculator():
    scores = []
    print("歡迎使用分數計算器！請輸入考試成績，輸入 'done' 結束。")

    while True:
        user_input = input("請輸入分數：")
        if user_input.lower() == 'done':
            break
        try:
            score = float(user_input)
            if score < 0 or score > 100:
                print("請輸入有效分數（0到100之間）。")
                continue
            scores.append(score)
        except ValueError:
            print("請輸入有效分數。")

    if scores:
        average_score = sum(scores) / len(scores)
        print(f"平均分數為：{average_score:.2f}")
    else:
        print("沒有輸入任何分數。")
if __name__ == "__main__":
    score_calculator()
# GitHub 版本管理註解範例：
# v1.0 - 初始版本，實現基本的分數計算功能
# v1.1 - 加入錯誤處理，提示非數字輸入
# v1.2 - 限制分數範圍在0到100之間
# v1.3 - 美化輸出格式，顯示平均分數到小數點後兩位
# v1.4 - 增加結束輸入的選項 'done'
