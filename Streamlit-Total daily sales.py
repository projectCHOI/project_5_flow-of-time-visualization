# pandas 판매 데이터의 웹 기반 대시보드를 만들기

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
data = pd.read_csv(r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\Master daily sales.csv')

# Streamlit 인터페이스 설정
st.title('Sales Data Analysis and Visualization')
st.write('This is a web dashboard for displaying sales data.')

# 데이터 표시
st.subheader('Sales Data')
st.dataframe(data)

# 연간 판매 추세 그래프
st.subheader('Yearly Sales Trends')
plt.figure(figsize=(10, 6))
for column in data.columns[1:]:
    sns.lineplot(data=data, x='TIME', y=column, label=column)
plt.xticks(rotation=45)
plt.ylabel('Sales')
plt.legend(title='Year')
st.pyplot(plt)

# 히트맵 생성
st.subheader('Sales Heatmap')
plt.figure(figsize=(10, 8))
heatmap_data = data.set_index('TIME')
sns.heatmap(heatmap_data, annot=True, cmap='viridis', linewidths=.5)
st.pyplot(plt)
