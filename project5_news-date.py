import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

def get_news(url):
    headers = {
        "Cookie": "NNB=OURWEDJJKXKGI; nx_ssl=2; _naver_usersession_=+VdPHYAMq5W53YOSu5ttbQ==; page_uid=ieZzndprvmsssdTDFjRssssssah-332673"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    try:
        # 일반 뉴스
        title = soup.select_one("h2#title_area").text
        date = soup.select_one("div.media_end_head_info_datestamp span")["data-date-time"].split(" ")[0]
        media = soup.select_one("a.media_end_head_top_logo img")["title"]
        content = soup.select_one('div#newsct_article')
    except:
        try:
            # 연예 뉴스
            title = soup.select_one('h2.end_tit').text.strip()
            date = soup.select_one('span.author em').text
            media = soup.select_one('div.press_logo img')['alt']
            content = soup.select_one('div#articeBody')
        except:
            # 스포츠 뉴스
            try:
                title = soup.select_one('h4.title').text
                date = soup.select_one('div.info span').text.split(' ')[1:]
                media = soup.select_one('span.logo img')['alt']
                content = soup.select_one('div#newsEndContents')
##예외 처리
            except:
                # 처리 실패시 로깅
                print("Failed to process URL:", url)
                return None  # 실패 처리를 위해 None 반환

    # 모든 시도 후에도 정보가 없으면 None을 반환
    if not all([title, date, media, content]):
        print("Incomplete data extracted from URL:", url)
        return None

    return (title, date, media, content, url)
##예외 처리

def get_news_list(keyword, start_date, end_date):
    news = []
    dates = pd.date_range(start_date, end_date)
# 페이지 수 제한
    for date in tqdm(dates, desc="Processing dates"):
        str_date = date.strftime("%Y.%m.%d")
        page = 1
        max_pages = 1000  # 최대 페이지 제한

        while True:
            strdate = str_date.replace(".", "")
            start = (page - 1) * 10 + 1
            if start > max_pages * 10:
                break  # 1000페이지를 초과하면 다음 날짜로 넘어감
# 페이지 수 제한

            headers = {"Cookie": "NNB=OURWEDJJKXKGI; nx_ssl=2; _naver_usersession_=+VdPHYAMq5W53YOSu5ttbQ==; page_uid=ieZzndprvmsssdTDFjRssssssah-332673"}
            URL = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&sort=2&photo=0&field=0&pd=3&ds={str_date}&de={str_date}&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:r,p:from{strdate}to{strdate},a:all&start={start}"
            res = requests.get(URL, headers=headers)
            soup = BeautifulSoup(res.text, "html.parser")

            if soup.select_one("div.not_found02") is not None:
                break

            page += 1

            for li in tqdm(soup.select("ul.list_news li"), desc=f"Scraping date: {str_date}, Page: {page}"):
                if len(li.select("div.info_group a")) > 1:
                    news.append(get_news(li.select("div.info_group a")[-1]["href"]))

    News = pd.DataFrame(news, columns=["제목", "날짜", "매체명", "본문", "URL"])

    # CSV
    st_d = start_date.replace('.', '_')
    e_d = end_date.split('.')[-1]
    file_name = f"{st_d}_{e_d}.csv"
    News.to_csv(file_name, mode="w", encoding='utf-8-sig')

    return News

print(get_news_list("마카롱", "2018.01.01", "2018.12.31"))
