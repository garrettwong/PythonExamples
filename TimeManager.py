import time


class TimeManager:
    def getTimeInMilliseconds(self):
        millis = int(round(time.time() * 1000))
        return millis


if __name__ == "__main__":
    tm = TimeManager()
    ms = tm.getTimeInMilliseconds()
    print(ms)