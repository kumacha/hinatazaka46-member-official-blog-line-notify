## 日向坂46ブログ通知
LINE Notify で推しメンのブログ通知を受け取ることができます。

## 実行内容

bs4とseleniumでスクレイピングを行い、ブログ情報を取得し、それをLINE Notifyを通じて通知します。<br/>
Google Cloud Platformを利用して1時間に1回、スクレイピングを定期実行し、1時間以内に投稿されたブログを通知します。

## フォーク元について
ryfeusさんのgcf-packsを利用し、GCP環境でのスクレイピング実行環境が楽なライブラリを利用させていただきました。

## 使用言語・ライブラリ等
* Python 3.7.1
* BeautifulSoup4
* selenium
* requests
* dotenv-python
* jupyter notebook
* LINE Notify API
* Google Cloud Platfrom
  * Cloud Scheduler
  * Cloud Pub/Sub
  * Cloud Functions
  * Cloud Shell


## 公式アプリとの差異

公式アプリでもブログの通知は来ます。ただ、内容がわからないのと写真が一枚も見えません。<br/>
そこで通知をLINEにまとめ、LINE内でタイトルと記事の写真を見ることができたら良いと思い、実装しました。

## LINE Notifyの画面
![IMG_1328](https://user-images.githubusercontent.com/68047170/129588174-75bc6801-6db0-446f-8159-b2578d78a874.jpg)

