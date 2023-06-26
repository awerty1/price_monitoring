from bs4 import BeautifulSoup

'''Get price and product name'''


def get_price_and_name_frm_aliexpress(page):
    # get cost of item(product) N
    soup = BeautifulSoup(page, 'html.parser')

    '''<div class="snow-price_SnowPrice__mainS__jlh6el" style="">7 182,00 ₽</div>'''
    container = soup.find_all('div', attrs={
        'class': 'snow-price_SnowPrice__mainS__jlh6el'})

    # name of item(product)
    '''
    <h1 class="snow-ali-kit_Typography__base__1shggo snow-ali-kit_Typography-Primary__base__1xop0e 
    snow-ali-kit_Typography__strong__1shggo snow-ali-kit_Typography__sizeHeadingL__1shggo 
    HazeProductDescription_ProductName__name__q1vxz">Современная потолочная люстра для гостиной, Спальни, 
    кухни, Подвесной светильник, Лампа E27, Освещение из дерева и железа, Подвесной светильник для 
    комнаты в квартире</h1>>
    '''
    item_name = soup.h1.text

    # check the price change
    current_price = container[0].text.translate(str.maketrans('', '', ' \xa0₽'))
    # print(current_price)
    return item_name, current_price
