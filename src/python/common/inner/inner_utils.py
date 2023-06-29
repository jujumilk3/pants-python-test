from datetime import datetime

from pytz import timezone

KST = timezone("Asia/Seoul")


def get_kst_time_inner():
    return datetime.now(KST).strftime("%Y-%m-%d %H:%M:%S") + "This is inner get_kst_time_inner"


if __name__ == "__main__":
    print(get_kst_time_inner())
