import requests, bs4

city = 'павловский под'

for i in range(len(city)):
    if city[i] == ' ':
        city = city[:i:] + '-' + city[i + 1::]
request = requests.get("https://sinoptik.com.ru/погода-" + city)
b = bs4.BeautifulSoup(request.text, "html.parser")
#print(b)

try:
    article=b.find_all("div","weather__article_description-text")
    temperature = b.find_all("div","table__temp")
    wind=b.find_all("div","table__wind")

    weather1 = temperature[0].getText()
    wind1=''
    wind1+=str(wind[0]).split(' ')[3][7:-5:1]+', '
    wind1+=wind[0].getText()+' м/с.'
    wind1_1=''
    for i in wind1:
        if i!='\n':
            wind1_1+=i

    weather2 = temperature[2].getText()
    wind2=''
    wind2+=str(wind[2]).split(' ')[3][7:-5:1]+', '
    wind2+=wind[2].getText()+' м/с.'
    wind2_1=''
    for i in wind2:
        if i!='\n':
            wind2_1+=i

    weather3 = temperature[4].getText()
    wind3 = ''
    wind3 += str(wind[4]).split(' ')[3][7:-5:1] + ', '
    wind3 += wind[4].getText() + ' м/с.'
    wind3_1 = ''
    for i in wind3:
        if i != '\n':
            wind3_1 += i

    weather4 = temperature[6].getText()
    wind4 = ''
    wind4 += str(wind[6]).split(' ')[3][7:-5:1] + ', '
    wind4 += wind[6].getText() + ' м/с.'
    wind4_1 = ''
    for i in wind4:
        if i != '\n':
            wind4_1 += i

    result = ''
    result = result + ('Ночью : ' + weather1 + ', Ветер: ' + wind1_1) + '\n'
    result = result + ('Утром : ' + weather2 + ', Ветер: ' + wind2_1) + '\n'
    result = result + ('Днём : ' + weather3 + ', Ветер: ' + wind3_1) + '\n'
    result = result + ('Вечером : ' + weather4 + ', Ветер: ' + wind4_1) + 2 * '\n'
    result+=article[0].getText()
    print(result)
except IndexError:
    result = 'Такого города не найдено'
    print(result)

'''for i in range(len(city)):
        if city[i] == ' ':
            city = city[:i:] + '-' + city[i + 1::]
    request = requests.get("https://sinoptik.com.ru/погода-" + city)
    b = bs4.BeautifulSoup(request.text, "html.parser")
    try:
        p3 = b.select('.temperature .p2')
        p3_1 = str(b.select('.p2')[6])[str(b.select('.p2')[6]).find("data-tooltip=")+14:str(b.select('.p2')[6]).rfind(' ">'):]
        weather1 = p3[0].getText()
        wind1=p3_1
        if len(wind1)<4:
            wind1="Ветра нет"
        #print(weather1,wind1)
        p4 = b.select('.temperature .p4')
        p4_1 = str(b.select('.p4')[6])[str(b.select('.p4')[6]).find("data-tooltip=")+14:str(b.select('.p4')[6]).rfind(' ">'):]
        weather2 = p4[0].getText()
        wind2=p4_1
        if len(wind2)<4:
            wind2="Ветра нет"
        #print(weather2,wind2)
        p5 = b.select('.temperature .p6')
        p5_1 = str(b.select('.p6')[6])[str(b.select('.p6')[6]).find("data-tooltip=")+14:str(b.select('.p6')[6]).rfind(' ">'):]
        weather3 = p5[0].getText()
        wind3=p5_1
        if len(wind3)<4:
            wind3="Ветра нет"
        #print(weather3,wind3)
        p6 = b.select('.temperature .p8')
        p6_1 = str(b.select('.p8')[6])[str(b.select('.p8')[6]).find("data-tooltip=")+14:str(b.select('.p8')[6]).rfind(' ">'):]
        weather4 = p6[0].getText()
        wind4=p6_1
        if len(wind4)<4:
            wind4="Ветра нет"
        #print(weather4,wind4)
        result = ''
        result = result + ('Ночью : ' + weather1+', Ветер: '+wind1) + '\n'
        result = result + ('Утром : ' + weather2+', Ветер: '+wind2) + '\n'
        result = result + ('Днём : ' + weather3+', Ветер: '+wind3) + '\n'
        result = result + ('Вечером : ' + weather4+', Ветер: '+wind4) + 2*'\n'
        temp = b.select('.rSide .description')
        weather = temp[0].getText()
        result = result + weather.strip()
        return result
    except IndexError:
        result = 'Такого города не найдено'
        return result'''
