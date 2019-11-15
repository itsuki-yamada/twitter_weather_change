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

from weather_info_get import weather_search


def main():
    user_name = 'hoge'
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
    print(user_name)


if __name__ == '__main__':
    main()
