import requests
r=requests.get("https://financialmodelingprep.com/")
print(r.text)

# url="https://financialmodelingprep.com/"
# data={"p1":4,"p2":8}
# r2=requests.post(url=url,data=data)
# print(r2.content)