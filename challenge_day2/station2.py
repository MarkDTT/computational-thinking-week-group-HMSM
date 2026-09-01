from datetime import datetime

def solution_station_2(date_string, date_format = "%y-%m-%d"):
    japanese_week_days = ["月曜日","火曜日","水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    dates = datetime.strptime (date_string, date_format)
    weekday_index = dates.weekday()

    return japanese_week_days[weekday_index]