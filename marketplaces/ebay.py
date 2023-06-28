from bs4 import BeautifulSoup

'''Get price and product name'''


def get_price_and_name_frm_ebay(page):
    # get cost of item(product) N
    soup = BeautifulSoup(page, 'html.parser')

    '''<span class="ux-textspans ux-textspans--SECONDARY ux-textspans--BOLD">1&nbsp;363,99 руб.</span>'''
    container = soup.find('span', attrs={
       'class': 'ux-textspans ux-textspans--SECONDARY ux-textspans--BOLD'})

    # name of item(product)
    '''
    # <span class="ux-textspans ux-textspans--BOLD">Warcraft 3: власть хаоса региона бесплатный 
    [Pc скачать | официальный сайт | ключ]</span>
    '''
    #item_name = soup.h1.text
    item_name = soup.find('span', attrs={
        'class': 'ux-textspans ux-textspans--BOLD'})

    # remove space and symbol ₽. Strip needed to del space after ₽
    current_price = container.text.translate(str.maketrans('', '', ' \xa0₽')).strip()

    # print("container: ", container)
    # print("curr price: ", current_price)
    # print("item_name: ", item_name)
    return item_name, current_price