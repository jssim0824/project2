from django.shortcuts import render
import numpy as np
import pandas as pd

# Create your views here.
def home(request):
    return render(request,'home.html')

def bitcoin(request):
    ed = float( request.POST['ed'] )
    bcc = float( request.POST['bcc'] )
    eos = float( request.POST['eos'] )
    tron = float( request.POST['tron'] )
    lc = float( request.POST['lc'] )    

    # 선형회귀 알고리즘
    df = pd.read_csv("price data.csv")
    df.head()
    from sklearn.model_selection import train_test_split
    x = df[['이더리움 고가변동률', '비트코인캐시 고가변동률', '이오스 고가변동률', '트론 고가변동률', '라이트코인 고가변동률']]
    y = df[['비트코인 고가변동률']]
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)
    from sklearn.linear_model import LinearRegression
    mlr = LinearRegression()
    mlr.fit(x_train, y_train)
    today_coin = [[ed, bcc, eos, tron, lc]]
    bitcoin = mlr.predict(today_coin)

    return render(request,'bitcoin.html',{'ed':ed,'bcc':bcc,'eos':eos,'tron':tron,'lc':lc,'bitcoin':bitcoin })