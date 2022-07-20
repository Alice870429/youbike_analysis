# Youbike Analysis
- 目標：研究捷運公館站(2號出口) YouBike 站點是否需要提高補車頻率
- 資料來源：
  - 台北市資料大平台——YouBike2.0臺北市公共自行車即時資訊
  - 台北市資料大平台——YouBike臺北市公共自行車即時資訊
- 資料時間範圍：以 7/17 16:00 ~ 7/18 22:00 （30hr）作為分析區間

## 事前作業
- 由於兩個資料平台提供的皆為每分鐘更新的即時資料，以`.json`檔作為串接來源，因此設定排程爬蟲將以上兩個資料來源抓下來導入`SQLite`資料庫進行使用
- [YouBike1.0](https://github.com/Alice870429/youbike_analysis/blob/main/youbike_tp_all.py)
- [YouBike2.0](https://github.com/Alice870429/youbike_analysis/blob/main/youbike_tp_20.py)

## 詳細分析
- [YouBike_Analysis](https://github.com/Alice870429/youbike_analysis/blob/main/YouBike_Analysis.ipynb)

## 補充
- 未來可解決問題：
  - 由於資料庫的限制，本次的分析僅探討 30 小時的資料，因此希望未來可以針對更長時段進行分析
  - 目前並沒有「補車成本」的相關資料，若未來有機會能獲得這部分的資料可以更進一步的影響分析的結論
