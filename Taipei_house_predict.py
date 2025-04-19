import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 檔案
file_path = "Taipei_house.csv"  # 如果是本地端執行，請確保檔案路徑正確
df = pd.read_csv(file_path)

# 將交易日期轉換為 datetime 格式
df["交易日期"] = pd.to_datetime(df["交易日期"], errors="coerce")

# 移除無效日期資料
df = df.dropna(subset=["交易日期"])

# 提取年月作為分析單位
df["年月"] = df["交易日期"].dt.to_period("M")

# 計算每月的平均總價
monthly_avg_price = df.groupby("年月")["總價"].mean().sort_index()

# 繪製房價趨勢圖
plt.figure(figsize=(12, 6))
monthly_avg_price.plot(marker='o', color='steelblue')
plt.title("台北房價趨勢（每月平均總價）")
plt.xlabel("年月")
plt.ylabel("平均總價（萬元）")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
