from bs4 import BeautifulSoup

'''Get price and product name'''


def get_price_and_name_frm_mvideo(page):
    # get cost of item(product) N
    soup = BeautifulSoup(page, 'html.parser')

    '''<span _ngcontent-serverapp-c10="" class="price__main-value"> 34&nbsp;999&nbsp;₽ </span>'''
    container = soup.find('span', attrs={
       'class': 'price__main-value'})

    # name of item(product)
    '''
    # <h1 class="lm">Блок питания для монитора LG 19V 1.7A (32W) 6.5x4.4мм с иглой</h1>
    '''
    item_name = soup.h1.text

    # remove space and symbol ₽. Strip needed to del space after ₽
    current_price = container.text.translate(str.maketrans('', '', ' \xa0₽')).strip()

    # print("container: ", container)
    # print("curr price: ", current_price)
    # print("item_name: ", item_name)
    return item_name, current_price