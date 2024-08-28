#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: mean_temp.py
    Author: Michael Pegg
    Description:  Calculates mean daily temperature from two user defined variables representing a daily high (x) and low (y) temperature
    Date created: ENTER TODAY'S DATE in 08/22/2024 FORMAT (e.g., 08/23/2023)
    Python Version: 3.9.16
"""

# Assign variable x the value for the previous day's high temperature
x = 94

# Assign variable y the value for the previous day's low temperature
y =  61

# Create variable z and use mathematical operators to calculate the mean temperature
z = (x+y)/2

# Use this custom statement that prints the result to screen
print("Yesterday's mean daily temperature was {0} degrees.".format(z))
