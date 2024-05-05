df = pd.read_csv('파일경로.csv')

exclude_keywords = ['키워드1', '키워드2', '키워드3']

for keyword in exclude_keywords:
    df = df[~df['본문'].str.contains(keyword, na=False)]


df.to_csv('바꿀 이름.csv', index=False, encoding='utf-8-sig')
print('결과 저장')