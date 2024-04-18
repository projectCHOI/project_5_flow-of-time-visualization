import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


# 파일 경로
file_path = r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\16y17y18y19y_Total daily sales.csv'
data = pd.read_csv(file_path)

# 데이터 확인
st.write(data)

# 'TIME' 열을 datetime 객체로 변환
data['TIME'] = pd.to_datetime(data['TIME'])

# 연도 추출
data['Year'] = data['TIME'].dt.year

# 연도별로 데이터를 재구성하여 각 연도를 별도의 행으로 표시
# 예: 모든 '2016' 값은 1행에, '2017' 값은 2행에 등
pivot_table = data.pivot_table(index='Year', columns='TIME', values='SALES', aggfunc='sum')

# 히트맵 생성
plt.figure(figsize=(20, 5))  # 차트 크기 조정
sns.heatmap(pivot_table, cmap='Reds', annot=True, fmt=".0f")
plt.title('Yearly Sales Heatmap by Date')
plt.xlabel('Date')
plt.ylabel('Year')

# Streamlit에 차트 표시
st.pyplot(plt)