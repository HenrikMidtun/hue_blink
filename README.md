# hue_blink
Blink script for Philips Hue
Use a cron job to schedule the script. I am using mine with an hourly schedule, by including the shell file into the /etc/cron.hourly/ directory. Remember to change the path to the python script in accordance.

This project is dependant on phue (https://github.com/studioimaginaire/phue)

Get it with
```
$ pip install phue
```
