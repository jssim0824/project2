from django.shortcuts import render
import numpy as np
import pandas as pd
from django.template import RequestContext

def error(request):
    return render(request, 'error.html')


# Create your views here.
def home(request):
    return render(request,'home.html')

def how(request):
    return render(request,'how.html')

def bitcoin(request):
    eda = float( request.POST['eda'] )
    bca = float( request.POST['bca'] )
    eoa = float( request.POST['eoa'] )
    tra = float( request.POST['tra'] )
    lca = float( request.POST['lca'] )   
    edb = float( request.POST['edb'] )
    bcb = float( request.POST['bcb'] )
    eob = float( request.POST['eob'] )
    trb = float( request.POST['trb'] )
    lcb = float( request.POST['lcb'] )  
    
    eds = (edb - eda)/eda
    bcs = (bcb - bca)/bca
    eos = (eob - eoa)/eoa
    trs = (trb - tra)/tra
    lcs = (lcb - lca)/lca

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
    today_coin = [[eds, bcs, eos, trs, lcs]]
    bitcoin = mlr.predict(today_coin)
    
    bitcoin = round(float(bitcoin), 3)
    if bitcoin >= 3 and bitcoin < 5 :
        a = '매수'
    else :
        a = ''
    if bitcoin >= 5 :
        b = '적극 매수'
    else :
        b = ''
    if bitcoin < 3 :
        c = '중립'
    else :
        c = ''
        
    return render(request,'bitcoin.html',{'eds':eds,'bcs':bcs,'eos':eos,'trs':trs,'lcs':lcs,'bitcoin':bitcoin, 'a':a, 'b':b, 'c':c})