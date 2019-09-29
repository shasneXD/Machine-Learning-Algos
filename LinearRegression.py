X=[1000,2000,20000,30000,75000]
Y=[50,90,4000,5000,20000]

def mean(list):
    sum=0
    mean=1
    length=len(list)
    for i in list:
        sum=sum+i
    mean=sum/length
    return mean

x_mean=mean(X)
y_mean=mean(Y)

def covariance(x,y):
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


def variance(x,y):
    x_error=[]

    for i in x:
       temp=i-x_mean
       x_error.append(temp**2)
    var=sum(x_error)
    return var


def slope(x,y):
    m=covariance(x,y)/variance(x,y)
    return m

def intercept(x,y):
    c=y_mean-slope(x,y)*x_mean
    return c


def predict_y(x,y,x_predict):
    y_predict=slope(x,y)*x_predict+intercept(x,y)
    print(y_predict)
    return y_predict


predict_y(X,Y,25000)
predict_y(X,Y,45000)
predict_y(X,Y,80000)

