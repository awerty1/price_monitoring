from bs4 import BeautifulSoup

'''Get price and product name'''


def get_price_and_name_frm_dns(page):
    # get cost of item(product) N
    soup = BeautifulSoup(page, 'html.parser')

    try:
        '''<div class="product-buy__price">10 999&nbsp;₽</div>'''
        container = soup.find('div', attrs={
            'class': 'product-buy__price'})

        # name of item(product)
        '''
        # <h1 class="product-card-top__title" data-product-title="">Клавиатура проводная Thermaltake 
        ARGENT K6 RGB Low Profile Mechanical Gaming Keyboard [GKB-KB6-LSSRRU-01]</h1>
        '''
        item_name = soup.h1.text

        # remove space and symbol ₽. Strip needed to del space after ₽
        current_price = container.text.translate(str.maketrans('', '', ' \xa0₽')).strip()
    except AttributeError:
        # Actions on error
        item_name = None
        current_price = None
        print(f"Error opening site. The link is outdated or there is protection from scripts.")

    # print("container: ", container)
    # print("curr price: ", current_price)
    # print("item_name: ", item_name)
    return item_name, current_price
