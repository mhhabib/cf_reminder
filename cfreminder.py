import requests
import time
import datetime as dt
import json
from plyer import notification

# Run the application in Background
# pythonw.exe .\desktopNotifier.py
# To kill the process, Go to taskbar and then found to kill it

contestData = None
try:
    contestData = requests.get('https://codeforces.com/api/contest.list')
except:
    notification.notify(
        title="No internet connection!",
        message="Seem there is no internet connection to your computer!",
        app_icon="cf.ico",
        timeout=60
    )


def contestTime(unixtime):
    date_time_obj = dt.datetime.strptime(unixtime, '%B %d %Y %I:%M %p')
    return date_time_obj.second+300


def timeLeft(unixtime):
    date_time_obj = dt.datetime.strptime(unixtime, '%B %d %Y %I:%M %p')
    time_to_start = date_time_obj-dt.datetime.now()
    return time_to_start, time_to_start.seconds


def convertUnixTime(unixtime):
    date = dt.datetime.fromtimestamp(unixtime).strftime('%B %d %Y')
    time = dt.datetime.fromtimestamp(unixtime).strftime('%I:%M %p')
    return date+" "+time


def convertToHour(secondsTime):
    return str(dt.timedelta(seconds=secondsTime))


def push_notification(c_name, c_time, c_duration, c_left):
    notification.notify(
        title="Contest Reminder!",
        message="{contestName}\n{contestTime}\nDuration : {durations} Hours\nYet to start : {lefttime}\n".format(
            contestName=c_name,
            contestTime=c_time,
            durations=c_duration,
            lefttime=c_left
        ),
        app_icon="cf.ico",
        timeout=60
    )


def contestDetails():
    while True:
        if contestData != None:
            jsonData = contestData.json()
            data = json.dumps(jsonData)
            contests = json.loads(data)
            contestList = []

            for contest in contests['result']:
                if(contest['phase'] == "FINISHED"):
                    break
                else:
                    contest['startTimeSeconds'] = convertUnixTime(
                        contest['startTimeSeconds'])
                    contest['durationSeconds'] = convertToHour(
                        contest['durationSeconds'])
                    contestList.append(contest)

            contestList = contestList[::-1]

            for con in contestList[0:1]:

                left, left_second = timeLeft(con['startTimeSeconds'])

                if(left_second > (6*3600)):
                    push_notification(
                        con['name'], con['startTimeSeconds'], con['durationSeconds'], left
                    )
                    x = left_second-(6*3600)+1
                    time.sleep(x)

                elif left_second == (6*3600):
                    push_notification(
                        con['name'], con['startTimeSeconds'], con['durationSeconds'], "6 Hours"
                    )
                    x = left_second-(5*3600)+1
                    time.sleep(x)
                elif left_second == (1*3600):
                    push_notification(
                        con['name'], con['startTimeSeconds'], con['durationSeconds'], "1 Hours"
                    )
                    x = left_second-(1*1800)+1
                    time.sleep(x)
                elif left_second == (1*1800):
                    push_notification(
                        con['name'], con['startTimeSeconds'], con['durationSeconds'], "30 Minutes"
                    )
                    x = left_second-(1*300)+1
                    time.sleep(x)
                elif left_second == (1*300):
                    push_notification(
                        con['name'], con['startTimeSeconds'], con['durationSeconds'], "5 Minutes"
                    )
                    x = left_second-(1)+1
                    time.sleep(x)
                elif left_second == 0:
                    push_notification(
                        con['name'], con['startTimeSeconds'], con['durationSeconds'], "Contest Started!"
                    )
                    x = contestTime(con['durationSeconds'])
                    time.sleep(x)
                # time.sleep(60)
        else:
            notification.notify(
                title="Contest Reminder!",
                message="No Upcomming contest found!",
                app_icon="cf.ico",
                timeout=60
            )
            time.sleep(300)


if __name__ == "__main__":
    contestDetails()
