
import json
import urllib3
import requests


class inWHU:
    def __init__(self, page):
        self.get_book_url = r'https://wx-inwhu.afunapp.com/book_transaction.php?act=latest_book&start='
        self.book_detail_url = r'https://wx-inwhu.afunapp.com/book_transaction.php?act=book_detail&isbn='
        self.book_queue = []
        self.wechat_list = {}
        self.get_wechat_from_a_book(page)

    def get_20_books(self, start):
        r = requests.get(self.get_book_url + str(start), verify=False)
        for i in r.json():
            self.book_queue.append(i['isbn'])


    def get_books(self, page):
        for i in range(page):
            self.get_20_books(i * 20)
            print('current page:'+str(i+1))

    def get_wechat_from_a_book(self,page):
        self.get_books(page)
        while len(self.book_queue) > 0:
            isbn = self.book_queue.pop()
            r = requests.get(self.book_detail_url + str(isbn), verify=False)
            wechat_list = r.json()['order_list']
            for i in wechat_list:
                self.wechat_list[str(i['wechat']).split(r'/')[-1]] = i['name']
        self.write_dict_to_file()
        print(self.wechat_list)

    def write_dict_to_file(self):
        file = open('wechat.json', 'w')
        file.write(json.dumps(self.wechat_list,ensure_ascii=False))


if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    inWHU(50)
