from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ueq
import pandas as pd
import numpy as np
def converter1(l):
    x=[]
    for i in l:
        bb=0
        nn=''
        for p in i:
            bb=bb+1
            if bb==1 and p == '₹':
                continue
            if p==',':
                continue
            if p == '₹':
                break
            nn=nn+p
        x.append(int(nn))
    return x
def converter2(l):
    x=[]
    for i in l:
        bb=0
        nn=''
        for p in i:
            bb=bb+1
            if p==',':
                continue
            if p == ' ':
                break
            nn=nn+p
        x.append(int(nn))
    return x
def converter3(l):
    x=[]
    for i in l:
        bb=0
        nn=''
        for p in i:
            bb=bb+1
            if bb==1 and p == '/':
                continue
            if p=='-':
                p=' '
            if p == '/':
                break
            nn=nn+p
        x.append(nn)
    return x
def converter4(l):
    x=[]
    for i in l:
        bb=0
        nn=''
        if i == 'Price: Not Available':
                bnn=np.nan
        else:
            for p in i:
                bb=bb+1
                if bb==1 and p == '₹':
                    continue
                if p==',':
                    continue
                nn=nn+p
                bnn=int(nn)
        x.append(bnn)
    return x
def converter5(l):
    x=[]
    for i in l:
        bb=0
        nn=''
        for p in i:
            bb=bb+1
            if bb==1 and p == '(':
                continue
            if p==',':
                continue
            if p == ')':
                break
            nn=nn+p
        x.append(int(nn))
    return x
def find_rishi(st):
    ucl = ueq(st)
    htmlp = ucl.read()
    ucl.close()
    a=soup(htmlp,"html.parser")
    product_name=[]
    for i in a.find_all("div",{"class":"col col-7-12"}):
        product_name.append(i.div.text)
    product_price=[]
    for i in a.find_all("div",{"class":"col col-5-12 _2o7WAb"}):
        product_price.append(i.div.text)
    product_price=converter1(product_price)
    product_rating=[]
    for i in a.find_all("span",{"class":"_2_KrJI"}):
        product_rating.append(float(i.div.text)) 
    product_peoplerat=[]
    for i in a.find_all("span",{"class":"_38sUEc"}):
        product_peoplerat.append(i.span.text)
    product_peoplerat=converter2(product_peoplerat)
    df=pd.DataFrame({'name':[],'price':[],'rating':[],'peoplerat':[]})
    for n,p,r,j in zip(product_name,product_price,product_rating,product_peoplerat):
        rr=pd.DataFrame([[n,p,r,j]],columns=['name','price','rating','peoplerat'])
        df=df.append(rr)
    df=df.reset_index(drop = True)
    return df
def sdf(mn,a,*b):
    c=mn(a)
    for i in b:
        c=c.append(mn(i))
    c=c.dropna()
    c=c.reset_index(drop = True)
    return c
def find_wood(st):
    ucl = ueq(st)
    htmlp = ucl.read()
    ucl.close()
    a=soup(htmlp,"html.parser")
    prod=[]
    prod_p=[]
    prod_r=[]
    prod_a=[]
    for i in a.find_all('div',{"class":"_3liAhj"}):
        qwe=str(i)
        if '_3LWrw9' in qwe:
            prod_a.append(1)
        else:
            prod_a.append(0)
        for p in i.find_all('a',{"class":"_2cLu-l"}):
            prod.append(p.get('href'))
        for p in i.find_all('div',{'class':"_1uv9Cb"}):
            prod_p.append(p.div.text)
        if '_38sUEc' in qwe:
            for p in i.find_all('span',{'class':'_38sUEc'}):
                prod_r.append(p.text)
        else:
            prod_r.append('(0,)')
    prod=converter3(prod)
    prod_p=converter4(prod_p)
    prod_r=converter5(prod_r)   
    df=pd.DataFrame({'name':[],'price':[],'peoplerat':[],'assured':[]})
    for n,p,r,g in zip(prod,prod_p,prod_r,prod_a):
        rr=pd.DataFrame([[n,p,r,g]],columns=['name','price','peoplerat','assured'])
        df=df.append(rr)
    df=df.reset_index(drop = True)
    return df
