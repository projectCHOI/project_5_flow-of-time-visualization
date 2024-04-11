import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
file_path = r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\daily sales.csv'
data = pd.read_csv(file_path)

# Streamlit에서 파일 확인
st.write(data)

# 'TIME' 열의 데이터를 날짜/시간 형식으로 변환, 변환할 수 없는 값은 NaT으로 설정
data['TIME'] = pd.to_datetime(data['TIME'], errors='coerce')

# NaT 값이 포함된 행을 제거할 수 있음
data = data.dropna(subset=['TIME'])

# 그래프 그리기
plt.figure(figsize=(10, 6))
for column in ['SALES1', 'SALES2', 'SALES3', 'SALES4', 'SALES5', 'SALES6', 'SALES7']:
    plt.plot(data['TIME'], data[column], label=column)
plt.xlabel('Time')
plt.ylabel('Sales')
plt.legend()
plt.title('Daily Sales Over Time')
st.pyplot(plt)

# 히트맵 그리기
sales_data = data[['SALES1', 'SALES2', 'SALES3', 'SALES4', 'SALES5', 'SALES6', 'SALES7']]
sns.heatmap(sales_data.transpose(), cmap='viridis')
plt.title('Sales Heatmap')
st.pyplot(plt)