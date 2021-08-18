import requests
from bs4 import BeautifulSoup
import re
import datetime
import time
from contextlib import closing
import config

# LINEのトークン
MY_LINE_TOKEN = config.MY_LINE_TOKEN
# 　LINE NotifyのURL
MY_NOTIFY_URL = config.MY_NOTIFY_URL

print("処理開始")
# 現在時刻(日本時間)
now = datetime.datetime.now()
jp_now = now + datetime.timedelta(hours=9)

token = config.MY_LINE_TOKEN
url = config.MY_NOTIFY_URL
headers = {"Authorization": "Bearer " + token}

# 全メンバーの記事を取得
top_url = "https://www.hinatazaka46.com/s/official/diary/member?ima=0000"  # 日向坂ブログトップページ
hina_url = "https://www.hinatazaka46.com"
bs = BeautifulSoup(requests.get(
    top_url, headers=headers).content, 'html.parser')
articles = bs.find_all("li", "p-blog-top__item p-blog-top__item--noneshadow")

# トップページに記載されている最新記事を取得
for article in articles:
    # ブログの更新時間を取得し、現在時刻との時差を計算
    date = article.select_one('time.c-blog-top__date').text
    blog_dt = datetime.datetime.strptime(date, '%Y.%m.%d %H:%M')
    Rusult_dt = jp_now - blog_dt
    # 更新時間が現時刻より1時間以内のブログのみを抽出
    t = datetime.timedelta(hours=24)
    name = article.select_one('div.c-blog-top__name').text.strip()
    if t > Rusult_dt and (name == '宮田　愛萌' or name == '上村 ひなの'):
        massage = '\n'
        massage += name+'\n'
        title = article.select_one('p.c-blog-top__title').text.strip()
        massage += "タイトル："+title+'\n'
        blog_url = hina_url+article.select_one('a').attrs["href"]
        massage += blog_url
        payload = {"message": massage}
        requests.post(url, headers=headers, params=payload)
        print(massage)
print('処理終了')