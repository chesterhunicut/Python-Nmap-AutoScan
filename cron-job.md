# To create the cron job to schedule this task, you will need to execute the following command as the root user:

crontab -e 

# When prompted, be sure to choose nano as your editor to keep it simple. You will then set the schedule based on your needs in the appropriate format. I use https://crontab.guru/ to help get the correct format. 

# I chose to run the cron job at 5PM every Wednesday evening. You then need to specificy that you want to run the job with sudo priveleges and provide the information to execute the script along 
# with the path where the script is saved. Here is how my cron job is set up:

0 17 * * 3 /usr/bin/sudo /usr/bin/python3 /path/to/your/script.py

# To make the script execute without any user interaction or having to enter a password, I modified the sudoers configureation file with the following command:

sudo visudo

# Find the line of the file that starts with %sudo or %admin, and add this text below:

administrator ALL=(ALL) NOPASSWD: ALL

# Save and exit. This is just what I found worked best for my circumstances but do whatever makes the most sense for your environment and use case. 

# At this point the cron job should be properly configured and you can get to testing!




