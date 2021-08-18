# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os
MY_LINE_TOKEN = os.getenv('MY_LINE_TOKEN')
MY_NOTIFY_URL = os.getenv('MY_NOTIFY_URL')