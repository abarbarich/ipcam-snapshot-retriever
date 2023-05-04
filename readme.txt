Use Crontab to run this script at set intervals.
Add the following lines to crontab to have the script download a snapshot every 15 minutes between the hours of UTC16-23 & UTC0-5 (NZST 8AM-5PM)
This was to avoid night time photos. (Im sure there is a way to do that in python also...)
I did not know how to make the script save a file to a certain folder so crontab is instructed to change to the directory then run the script

=============================================================================

# m h  dom mon dow   command
0,15,30,45 16-23 * * * cd ~/<foldername>/ && python3 snapshot.py
0,15,30,45 0-5 * * * cd ~/<foldername>/ && python3 snapshot.py
