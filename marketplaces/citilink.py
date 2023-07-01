from bs4 import BeautifulSoup

'''Get price and product name'''


def get_price_and_name_frm_citilink(page):
    # get cost of item(product) N
    soup = BeautifulSoup(page, 'html.parser')

    try:
        '''<span class="e1j9birj0 e106ikdt0 app-catalog-1f8xctp e1gjr6xo0" color="None">55 990</span>'''
        container = soup.find('span', attrs={
           'class': 'e1j9birj0 e106ikdt0 app-catalog-1f8xctp e1gjr6xo0'})

        # name of item(product)
        '''
        # <h1 class="e1ubbx7u0 eml1k9j0 app-catalog-tn2wxd e1gjr6xo0" color="Main">
        Процессор AMD Ryzen 9 7950X, SocketAM5,  BOX (без кулера) [100-100000514wof]</h1>
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