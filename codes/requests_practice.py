import requests

res = requests.get("http://google.com")
#res = request.get("http://nadocoding.tistory.com")
print("응답코드 :", res.status_code) # 200 이면 정상

#if res.status_code == requests.codes.ok:
#   print("정상입니다")
#else:
#   print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

res.raise_for_status()
print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)


