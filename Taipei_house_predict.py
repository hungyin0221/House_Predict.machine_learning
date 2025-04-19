mport pandas as pd
import matplotlib.pyplot as plt

# 讀取資料
file_path = "Taipei_house.csv"  # 請確認路徑正確
df = pd.read_csv(file_path)

# 處理日期欄位
df["交易日期"] = pd.to_datetime(df["交易日期"], errors="coerce")
df = df.dropna(subset=["交易日期"])
df["年月"] = df["交易日期"].dt.to_period("M")

# 計算每坪單價（避免除以0）
df = df[df["建物總面積"] > 0].copy()
df["每坪單價"] = df["總價"] / df["建物總面積"]

# 分組：依照「行政區」與「年月」
district_trends = df.groupby(["行政區", "年月"])["每坪單價"].mean().unstack(level=0)

# 繪圖
plt.figure(figsize=(14, 7))
district_trends.plot(marker='o', figsize=(14, 7), colormap='tab10')
plt.title("台北各行政區每坪單價趨勢（萬元/坪）")
plt.xlabel("年月")
plt.ylabel("每坪單價（萬元）")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title="行政區", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
