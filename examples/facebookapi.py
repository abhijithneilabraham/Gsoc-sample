#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:28:00 2019

@author: abhijithneilabraham
"""
import facebook

token='EAAaq8yfWwV4BAAlqbyBwBc9WpagU8mC20xADoirsnvHEqLA1mfaGqQZBVfLYQ2SCPB6PjAtpbdb9cpcR8jZAyVhdHSmLzPxpUXl8o4qzGuUZBCl9mQjUZBLA7q8LaGraNSe695pHgbPW0hUNM7aZAhGZCvuS8S3ZCLRv9RHZA1AvsQZDZD'
graph = facebook.GraphAPI(access_token=token, version = 3.1)
site_info = graph.get_object(id="https%3A//mobolic.com",
                             fields="og_object")
print(site_info["og_object"]["description"])