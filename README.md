# Python-Nmap-AutoScan
Python Script to automate Nmap scans against known IP ranges

This was my first crack at using Python to automate some Nmap scans against multiple IP ranges. 

The script is designed to scan against your specified targets with a comprehensive Nmap scan, save the results as a .txt file, and send them via email to the desired recipients.

I've used this to save some time when scanning against entire server ranges and have utilized a cron job to set it on a weekly schedule. 

There are some things to consider when creating the cron job, as it will have to be executed with sudo privileges without passing credentials. 

The details for how I set this up can be found in the "cron-job" section of this repo. 

As this is my first Python script, I welcome any and all feedback!

Looking forward to hearing what everyone thinks of it and seeing how the script will continue to evolve.

Happy Scanning!

Christian Morton (aka ChesterHunicut)
LinkedIn - https://www.linkedin.com/in/christian-morton-7080aa1b2/


