import requests

url = r'https://wx-inwhu.afunapp.com/book_transaction.php?act=book_detail&isbn=9787307054424'
list = {}
r = requests.get(url,verify=False)
a = r.json()['order_list']
for i in a:
    wechat = str(i['wechat'])
    x = wechat.split(r'/')[-1]
    list[x]=i['name']
print(list)