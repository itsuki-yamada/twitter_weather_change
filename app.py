"""
*定期的に実行する
1. 位置情報を取得
    1-1. 座標で取得する必要がある
2. 天気情報を取得(座標で
    2-1. OpenWeatherMapを使用
3. Twitterの名前を取得して@部分を変更
    3-1. TwitterAPI
4. 変更したtwitter名をコミットする

*memo
-   {
    "id": 2112518,
    "name": "Iwate-ken",
    "country": "JP",
    "coord": {
      "lon": 141.359711,
      "lat": 39.596008
    }
"""
import datetime

from requests_oauthlib import OAuth1Session

import config
from weather_info_get import weather_search


def update_name(twitter, user_name):
    url = 'https://api.twitter.com/1.1/account/update_profile.json'
    params = {'name': user_name}
    twitter.post(url, params)


def main():
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理

    user_name = 'itsuki'
    weather_id = weather_search()
    print(weather_search())
    # weather_id = 201

    # AWS lambda内の時刻を合わせる (UST => JST)
    now = datetime.datetime.now()
    # jst = now + datetime.timedelta()
    jst = now.hour

    print(weather_id)
    # weather_id をもとに分類
    if weather_id == 800:
        if 18 <= jst <= 23 or 0 <= jst <= 5:
            user_name = user_name + "🌕"
        else:
            user_name = user_name + "☀"
    elif weather_id >= 801:
        if 18 <= jst <= 23 or 0 <= jst <= 5:
            user_name = user_name + "🌕☁"
        else:
            user_name = user_name + "☀☁"
    elif 802 <= weather_id <= 804:
        user_name = user_name + "☁"
    elif 300 <= weather_id <= 321:
        user_name = user_name + "🌂"
    elif 500 <= weather_id <= 531:
        user_name = user_name + "☔"
    elif 200 <= weather_id <= 232:
        user_name = user_name + "⚡☔"
    elif 600 <= weather_id <= 622:
        user_name = user_name + "⛄"
    elif weather_id >= 900:
        user_name = user_name + "🌀"

    print(jst)
    update_name(twitter, user_name)
    print(user_name)


if __name__ == '__main__':
    main()
