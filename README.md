# CodeForces Contest Reminder
Desktop notifications scripting application which will remind you about upcomming Codeforces contest.

Currently, It will push notifications reminder in your desktop pc. <br/>
![Untitled](https://user-images.githubusercontent.com/17263976/132727396-9c515aa9-9879-485f-bbff-2b3f3e38bc9f.png)

## Reminder time
- New contest arrival after finising of latest contest.
- 6 Hours before the contest
- 1 Hour before the contest.
- 30 minutes before the contest.
- 5 Minutes before the contest.
- Contest started

## Uses
- Clone the reposity in your suitable directory.
- Install <kbd>requirements.txt</kbd> file
```bash
pip install -r requirements.txt
```
- Run the script
```bash
python cfreminder.py
```
- To run the srcipt as application in background for infinite time.
```bash
pythonw.exe .\cfreminder.py
```
## Kill the application from background
- Go to <kbd>Taskbar > Task Manager</kbd>
- Find `Python` from <kbd> Background Processes </kbd>
- Select and Press `End Task` from bottom right button.

## Warning!
- It may have bugs. Since i used timer sleep, it may show you a lots of notification. If it this happens then [go](#Kill-the-application-from-background) to the above killing process. 

**NB** Feel free to use and contribute the repository. If you found any bugs the report as Issues or Send a PR.
