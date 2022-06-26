# -*- coding: utf-8 -*-
"""
Created on Sun May  1 17:32:00 2022

@author: fireroka
"""

count=0
sum=0
full_name = input("what is your full name: ")
min_price = float(input("enter the minimum price: "))
price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]
for price in price_list:
    
    sum=sum+price
    if price > min_price:
        count=count+1
        
print("Hello ", full_name," the minimum price is ",min_price)
print("There are ",count,"prices greater than the minimum price")
print("The total price is ",sum)