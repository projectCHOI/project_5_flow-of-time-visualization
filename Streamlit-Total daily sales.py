import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 파일 읽기
data = pd.read_csv(r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\Master daily sales.csv')

# DataFrame 생성
sales_df = pd.DataFrame(sales_data, index=[2016, 2017, 2018, 2019])

# 히트맵 그리기
plt.figure(figsize=(12, 8))
sns.heatmap(sales_df, cmap='viridis', annot=True, fmt=".0f", linewidths=.5)
plt.title('Monthly Sales Heatmap (2016-2019)')
plt.xlabel('Month')
plt.ylabel('Year')
plt.show()
