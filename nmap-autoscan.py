#!/usr/bin/env python3

# Objects IN_THIS_FORMAT need to be changed to your specific settings. 

# ________                   ___         
#|\   ____\                _|\  \__      
# \ \  \___|  ____________ |\   ____\     
#  \ \  \    |\____________\ \  \___|_    
#   \ \  \___\|____________|\ \_____  \   
#    \ \_______\             \|____|\  \  
#     \|_______|               ____\_\  \ 
#                             |\___    __\
#                             \|___|\__\_|
#                                   \|__|  

#Christian Morton - Ethical Hacker
#linkedin - https://www.linkedin.com/in/christian-morton-7080aa1b2/
#github - https://github.com/chesterhunicut

import os
import nmap
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Directory path for scan results
results_directory = "/PATH_TO_YOUR_DIRECTORY"

# Define the IP ranges to scan
target_ranges = [
    "IP_RANGE_TO_SCAN",
    "IP_RANGE_TO_SCAN",
    "IP_RANGE_TO_SCAN",
    # Add more target ranges as needed
]

# Get current date in mm_dd_yy format
current_date = datetime.now().strftime("%m_%d_%y")

# Perform Nmap scans against the top 1000 ports for each target range and save the results in TXT format
scan_results = []
for target_range in target_ranges:
    output_file_txt = os.path.join(results_directory, f"scan_{current_date}_{target_range.replace('/', '_')}.txt")
    nm = nmap.PortScanner()
    nm.scan(hosts=target_range, arguments=" -sS -sV -p 1-1000 -oN " + output_file_txt)
    # Append the scan result file to the list
    scan_results.append(output_file_txt)

print("Nmap scans completed successfully.")

# Email configuration
sender_email = "SENDER_EMAIL_ADDRESS"
receiver_email = "RECIPIENT_EMAIL_ADDRESS"
smtp_server = "YOUR_SMTP_SERVER"
smtp_port = 587
smtp_username = "YOUR_SMTP_USERNAME"
smtp_password = "YOUR_SMTP_PASSWORD"

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Weekly Nmap Scan Results"

# Add the scan results as attachments to the email
for file in scan_results:
    with open(file, "rb") as attachment:
        part = MIMEApplication(attachment.read())
    part.add_header("Content-Disposition", "attachment", filename=os.path.basename(file))
    message.attach(part)

# Send the email using SMTP
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(message)
    print("Scan results emailed successfully!")
