import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 파일 경로 설정
file_path = r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\hourly sales.csv'

# Streamlit을 사용하여 데이터 불러오기
@st.cache_data  # 데이터 캐싱을 위한 새로운 메소드 사용
def load_data(path):
    data = pd.read_csv(path)
    return data

# 데이터 불러오기
data = load_data(file_path)

# Streamlit에 데이터 표시
st.write(data)

# 그래프 그리기 준비
sales_data = data[['TIME', 'SALES1', 'SALES2', 'SALES3', 'SALES4', 'SALES5', 'SALES6', 'SALES7']]
sales_data = sales_data.set_index('TIME')

# 히트맵 생성
plt.figure(figsize=(10, 8))
sns.heatmap(sales_data, cmap='Reds', linewidths=.5)
plt.title('Hourly Sales Heatmap')
plt.xlabel('Sales')
plt.ylabel('Time')

# Streamlit에 그래프 표시
st.pyplot(plt)
