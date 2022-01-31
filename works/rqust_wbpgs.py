import requests

CNN = requests.get('https://edition.cnn.com/2022/01/30/football/mason-greenwood-manchester-united-intl-spt-gbr/index.html')
BBC = requests.get('https://www.bbc.com/sport/football')
YT = requests.get('https://www.youtube.com/watch?v=UOXDdY9L-Y4')

print ('what site content would you like to get')

news = str(input())


if (news == "CNN"):
    print (CNN.content)

elif (news == 'BBC'):
    print (BBC.content(news)) 

elif (news == "YT"):
    print (YT.content(news))     

else:
    ('Select CNN, BBC, YT')