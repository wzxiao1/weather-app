from requests_html import HTMLSession 
exit_status = False
s = HTMLSession() # intit HTMLSESSION class

#where we want the weather to be
while not exit_status:
    try:
        query = input("Which city's weather would you like to see? ")
        url = f'https://www.google.com/search?q={query}+weather' 
        r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
        # looking for units
        unit_status = False
        while not unit_status:
            unit_in = input("In which unit do you wish to view the temperature in? (f/c)")
            if unit_in == "c":        
                temp = r.html.find('div.Ab33Nc', first = True).find('span#wob_tm', first = True).text
                unit = r.html.find('div.vk_bk.wob-unit', first = True).text[0:2]
                unit_status = True
            elif unit_in == 'f':
                temp = r.html.find('div.Ab33Nc', first = True).find('span#wob_ttm', first = True).text
                unit = r.html.find('div.vk_bk.wob-unit', first = True).text[4:6]
                unit_status = True
            else:
                print("Please enter the correct units")

        description = r.html.find('div.VQF4g', first = True).find('span#wob_dc', first = True).text.lower()
        print(f"It looks like in {query} the temperature is around {temp}{unit} and it is {description}!")
        if "sunny" in description:
            print("Be sure to wear a cap and some shades!")
        elif "shower" in description:
            print("Be sure to bring an umbrella!")
        exit = input("Type '0' to exit and press any buttons to continue: ")
        if exit == '0':
            exit_status = True
    except:
        print("Please enter a correct city!")
        exit = input("Type '0' to exit and press any buttons to continue: ")
        if exit == '0':
            exit_status = True