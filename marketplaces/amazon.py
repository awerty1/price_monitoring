import re

from bs4 import BeautifulSoup
from colorama import Fore

'''Get price and product name'''


def get_price_and_name_frm_amazon(page):
    # get cost of item(product) N

    soup = BeautifulSoup(page, 'html.parser')

    try:
        '''<span id="color_name_0_price" class="olp-message a-color-price">        
        <span class="a-size-mini olpMessageWrapper"> 2 options from<br>$79.99 </span>       </span>'''
        container = soup.find('span', attrs={
            'id': 'color_name_0_price'}).get_text().strip()

        # name of item(product)
        '''# <h1 id="title" class="a-size-large a-spacing-none"> <span id="productTitle" class="a-size-large 
        product-title-word-break"> Keychron K14 70% Layout 72 Keys Bluetooth Wireless/USB Wired Mechanical Keyboard 
        for Mac with Gateron G Pro Blue Switch/Multitasking/RGB Backlight/Aluminum Frame Computer Keyboard for 
        Windows Laptop       </span>       </h1>'''

        item_name = soup.h1.text.strip()
        # remove space and symbol ₽. Strip needed to del space after ₽
        current_price = re.search(r'\d+\.\d+', container).group()
    except AttributeError:
        # Actions on error
        item_name = None
        current_price = None
        print(f"{Fore.RED}Error opening site. The link is outdated or there is protection from scripts.{Fore.RESET}")

    # print("container: ", container)
    # print("curr price: ", current_price)
    # print("item_name: ", item_name)
    return item_name, current_price
