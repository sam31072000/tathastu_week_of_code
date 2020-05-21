from collections import Counter
l = ['sam','abhay','akshay','soni','soni','sonu','akshay','tushar','mohit','sam','abhay','akshay','sonu','akshay','tushar','mohit','mohit','tushar','tushar','akshay','sam','sam',]
dic = dict(Counter(l))
dic = list(dic.items())
dic.sort(key = lambda x:x[0])
dic.sort(key = lambda x:x[1])
print(dic)
