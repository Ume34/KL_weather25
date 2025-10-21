import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL例（クアラルンプールの過去天気）
url = "https://www.weather25.com/asia/malaysia/kuala-lumpur?page=past-weather"

# HTMLを取得
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# __NEXT_DATA__ の JSON を抽出
script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
data = json.loads(script_tag.string)

# JSONの中から気象データを探す
# 実際のキー構造は日によって違う場合があるためprintで確認する
forecast_data = data["props"]["pageProps"]

# 例: hourly または daily のリストが含まれている
print(json.dumps(forecast_data, indent=2))  # 👈 まずは構造確認

# ↓ ここから必要な項目（時間、気温など）を抽出するロジックを追加していく
