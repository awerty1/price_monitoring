from bs4 import BeautifulSoup

'''Get price and product name'''


def get_price_and_name_frm_ymarket(page):
    # get cost of item(product) N
    soup = BeautifulSoup(page, 'html.parser')

    try:
        '''<span data-auto="price-value">69</span>'''
        container = soup.find_all('span', attrs={
            'data-auto': 'price-value'})

        '''
        <h1 class="_1BWd_ _2OAAC undefined" data-tid="4c4e628" data-tid-prop="4c4e628" data-baobab-name="title" 
        data-node-id="b4n21d">Мистраль крупа пшеничная Булгур, 500 г</h1>
        '''
        # name of item(product)
        item_name = soup.h1.text

        # remove space and symbol ₽.
        current_price = container[0].text.translate(str.maketrans('', '', ' \xa0₽'))
    except AttributeError:
        # Actions on error
        item_name = None
        current_price = None
        print(f"Error opening site. The link is outdated or there is protection from scripts.")

    # print("container ", current_price)
    # print("item_name ", item_name)

    return item_name, current_price
