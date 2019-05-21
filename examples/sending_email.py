#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:45:21 2019

@author: abhijithneilabraham
"""

import smtplib, ssl
sender_email="abhijithneilabrahampk@gmail.com"
receiver_email="augustinjose1221@gmail.com"
port = 465  # For SSL
password = input("enter password here")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("abhijithneilabrahampk@gmail.com", password)
    server.sendmail(sender_email, receiver_email, "helllo")