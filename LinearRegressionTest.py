import pandas as pd
import numpy as np

data=pd.read_csv(r"C:\Users\Sneha Sharma\Downloads\CarPriceCoding.csv")        #insert your csv file address inside ""

curbweight=data['curbweight']                                                  #list containing curbweights
price=data['price']                                                            #listcontaining prices


def mean(list):
    sum=0
    mean=0
    length=len(list)
    for i in list:
        sum=sum+i
    mean=sum/length
    return mean

x_mean=mean(curbweight)
y_mean=mean(price)

def covariance(x,y):                    # x and y are list
    x_error=[]
    y_error=[]
    xy_error=[]

    for i in x:
        x_error.append(i-x_mean)
    for i in y:
        y_error.append(i-y_mean)
    for i in range(len(x)):
        xy_error.append(x_error[i]*y_error[i])

    covar=sum(xy_error)
    return covar

def variance(x):
    x_error=[]

    for i in x:
        x_error.append((i-x_mean)**2)

    var=sum(x_error)
    return var

def slope(x,y):
    m=covariance(x,y)/variance(x)
    return m

def intercept(x,y):
    c=y_mean-(x_mean*slope(x,y))
    return c

def predict_y(x,y,x_predict):                           #x predict is value of x(curbweight) using which we will find the y value(i.e the price value)
    y_predict=(slope(x,y)*x_predict)+intercept(x,y)
    return y_predict

print(predict_y(curbweight,price,3000))
print(predict_y(curbweight,price,3500))
print(predict_y(curbweight,price,4500))
print(predict_y(curbweight,price,5000))
