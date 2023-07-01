from bs4 import BeautifulSoup

'''Get price and product name'''


def get_price_and_name_frm_wildberries(page):
    # get cost of item(product) N
    soup = BeautifulSoup(page, 'html.parser')

    try:
        '''#<ins class="price-block__final-price">690&nbsp;₽</ins>'''
        container = soup.find_all('ins', attrs={
            'class': 'price-block__final-price'})

        # name of item(product)
        '''
        # <h1 data-link="text{:selectedNomenclature^goodsName}">
        Блок питания для монитора LG 19V 1.7A (32W) 6.5x4.4мм</h1>
        '''
        item_name = soup.h1.text

        # check the price change
        # current_price = container[0].text.replace("₽", '').replace(' ', '').replace('\xa0', '')
        current_price = container[0].text.translate(str.maketrans('', '', ' \xa0₽'))
    except AttributeError:
        # Actions on error
        item_name = None
        current_price = None
        print(f"Error opening site. The link is outdated or there is protection from scripts.")

    # print(current_price)
    return item_name, current_price
