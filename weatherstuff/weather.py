from requests_html import HTMLSession 
exit = False
s = HTMLSession() # intit HTMLSESSION class

#where we want the weather to be
while not exit:
    query = input("Which city's weather would you like to see? ")
    url = f'https://www.google.com/search?q={query}+weather' # url that



#gets the url
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

#finding span#wob_tm which is the temperature
    temp = r.html.find('div.Ab33Nc', first = True).find('span#wob_tm', first = True).text
    celsius = r.html.find('div.vk_bk.wob-unit', first = True).text[0:2]
    description = r.html.find('div.VQF4g', first = True).find('span#wob_dc', first = True).text.lower()


    print(f"It looks like in {query} the temperature is around {temp}{celsius} and it is {description}!")
    exit = input("Type 'True' to exit and press any buttons to continue: ")
