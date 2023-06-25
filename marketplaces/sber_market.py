from bs4 import BeautifulSoup

'''Get price and product name'''


def get_price_and_name_frm_smm(page):
    # get cost of item(product) N
    soup = BeautifulSoup(page, 'html.parser')

    '''
    # <span class="pdp-sales-block__price-final">
    # 	1 616 ₽
    # 	<meta itemprop="price" content="1616"> <meta itemprop="priceCurrency" content="RUB">
    # 	<link itemprop="availability" href="http://schema.org/InStock" content="InStock">
    # 	<link itemprop="url" content="https://sbermegamarket.ru/"></span>
    '''

    container = soup.find_all('span', attrs={
        'class': 'pdp-sales-block__price-final'})

    '''
    <h1 itemprop="name" class="pdp-header__title page-title">
    Блок питания для LG / HP 19V 4.74A
    </h1>
    '''

    # name of item(product)
    item_name = soup.h1.text.strip()

    # remove space and symbol ₽.
    current_price = container[0].text.translate(str.maketrans('', '', ' \xa0₽')).strip()

    # print("container ", current_price)
    # print("item_name ", item_name)
    return item_name, current_price
