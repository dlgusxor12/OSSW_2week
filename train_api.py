import requests

url = "https://apis.data.go.kr/B551457/run/v2/travelerTrainRunPlan2"
serviceKey="jb14LGSONSwtrptaTUfUlGp3fAc0f1MJ78s%252FtRyt0OiffhCXohmDlqutYyCKdHiOTQblmUoVaw27l%252FMYJBN29g%253D%253D"
# GET 요청 보내기
response = requests.get(url)

# 응답 상태 코드 확인
if response.status_code == 200:
    # 응답 데이터를 JSON 형식으로 파싱
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
