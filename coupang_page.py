import requests
import re
from bs4 import BeautifulSoup
import env

headers = {"User-Agent":env.User_Agent}
for i in range(1, 6):
    print("현재 페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")


    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())

    for item in items:
        
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print(" < 광고 상품 제외> ")
            continue
        
        name = item.find("div", attrs={"class":"name"}).get_text()

        # Apple 제외
        if "Apple" in name:
            # print(" < Apple 제품 제외 > ")
            continue

        price = item.find("strong",attrs={"class":"price-value"}).get_text()
        
        # 평점 4.5이상 리뷰 100개이상

        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            # print(" < 평점 없는 상품 제외 > ")
            continue

        rate_count = item.find("span", attrs={"class":"rating-total-count"})
        if rate_count:
            rate_count = rate_count.get_text()[1:-1]
        else:
            # print(" < 평점수 없는 상품 제외 > ")
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_count) >= 50:
            print(f"제품명 : {name}")
            print(f"가격 : {price}원")
            print(f"평점 : {rate}점 ({rate_count}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-" * 100) # 구분선