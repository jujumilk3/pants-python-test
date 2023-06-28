from datetime import datetime

from pytz import timezone

KST = timezone("Asia/Seoul")


def get_kst_time():
    return datetime.now(KST)


if __name__ == "__main__":
    print(get_kst_time())
