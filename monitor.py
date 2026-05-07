import requests
import json
import os

# LINE通知用の設定（LINE Notifyからトークンを取得して入れる）
LINE_TOKEN = "R1rKkKtMC8FexEogefqKITz+pkjLo/cotFCLNvQFcxUKy8u1Cr7A+vjBgnbBrXlzBgmKu1ZtQUDtqPob3YM+QXc7i+SGcf5JQa+uEy/zT5haNKWau9m4CccPZ0TvQ7BPRR5oaW0X0KR1jWMMsx3tmgdB04t89/1O/w1cDnyilFU="

def send_line(message):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    payload = {"message": message}
    requests.post(url, headers=headers, data=payload)

def main():
    # 1. 案件データを取得（前述のCSV読み込みや簡易スクレイピング）
    # 2. 過去のデータと比較して「報酬アップ」や「新規」を探す
    
    # 仮の検知結果
    new_opportunities = [
        {"name": "SBI証券", "reward": 15000, "diff": "+3000円アップ！"}
    ]
    
    if new_opportunities:
        msg = "\n🚀【期待値上昇】案件検知！\n"
        for opt in new_opportunities:
            msg += f"・{opt['name']}: {opt['reward']}円 ({opt['diff']})\n"
        
        send_line(msg)
        print("LINE通知を送信しました")

if __name__ == "__main__":
    main()
