import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 불러오기
file_path = r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\hourly sales.csv'
data = pd.read_csv(file_path)

# 데이터 표시
st.write("Daily Sales Data")
st.dataframe(data)

# 일별 판매액 그래프 그리기
st.write("Sales Graph")
plt.figure(figsize=(10, 6))
for column in ['SALES1', 'SALES2', 'SALES3', 'SALES4', 'SALES5', 'SALES6', 'SALES7']:
    plt.plot(data['TIME'], data[column], label=column)
plt.xlabel('Time')
plt.ylabel('Sales')
plt.legend()
st.pyplot(plt)

# 일별 판매액 히트맵
st.write("Sales Heatmap")
sales_data = data[['SALES1', 'SALES2', 'SALES3', 'SALES4', 'SALES5', 'SALES6', 'SALES7']]
sns.heatmap(sales_data, cmap='Reds')
st.pyplot(plt)

# 'SUM' 열 계산 및 추가
data['SUM'] = data[['SALES1', 'SALES2', 'SALES3', 'SALES4', 'SALES5', 'SALES6', 'SALES7']].sum(axis=1)

# 시간별 판매 합계 꺽은선 그래프 시각화
st.write("Sum of Sales Over Time")
plt.figure(figsize=(10, 6))
plt.plot(data['TIME'], data['SUM'], label='Sum of Sales')
plt.xlabel('Time')
plt.ylabel('Sum of Sales')
plt.legend()
st.pyplot(plt)
