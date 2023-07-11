from bs4 import BeautifulSoup
from colorama import Fore

'''Get price and product name'''


def get_price_and_name_frm_ebay(page):
    # get cost of item(product) N
    soup = BeautifulSoup(page, 'html.parser')

    try:
        '''<span class="ux-textspans ux-textspans--SECONDARY ux-textspans--BOLD">1&nbsp;363,99 руб.</span>'''
        container = soup.find('span', attrs={
            'class': 'ux-textspans ux-textspans--SECONDARY ux-textspans--BOLD'})

        # name of item(product)
        '''
        # <span class="ux-textspans ux-textspans--BOLD">Warcraft 3: власть хаоса региона бесплатный 
        [Pc скачать | официальный сайт | ключ]</span>
        '''
        # item_name = soup.h1.text
        item_name = soup.find_all('span', attrs={
            'class': 'ux-textspans ux-textspans--BOLD'})
        item_name = item_name[1].text

        # remove space and symbol ₽. Strip needed to del space after ₽
        current_price = container.text.translate(str.maketrans('', '', ' \xa0₽')).strip()
    except AttributeError:
        # Actions on error
        item_name = None
        current_price = None
        print(f"{Fore.RED}Error opening site. The link is outdated or there is protection from scripts.{Fore.RESET}")

    # print("container: ", container)
    # print("curr price: ", current_price)
    # print("item_name: ", item_name)
    return item_name, current_price
