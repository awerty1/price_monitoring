from colorama import Fore

from marketplaces import get_price_and_name_frm_wildberries
from marketplaces import get_price_and_name_frm_ozon
from marketplaces import get_price_and_name_frm_ymarket
from marketplaces import get_price_and_name_frm_smm
from marketplaces import get_price_and_name_frm_aliexpress
from marketplaces import get_price_and_name_frm_citilink
from marketplaces import get_price_and_name_frm_mvideo
from marketplaces import get_price_and_name_frm_dns
from marketplaces import get_price_and_name_frm_ebay

'''Chooses the right site'''


def choose_site(site_name, page):
    if site_name == "wildberries":
        return get_price_and_name_frm_wildberries(page)
    elif site_name == "ozon":
        return get_price_and_name_frm_ozon(page)
    elif site_name == "yandex":
        return get_price_and_name_frm_ymarket(page)
    elif site_name == "sbermegamarket":
        return get_price_and_name_frm_smm(page)
    elif site_name == "aliexpress":
        return get_price_and_name_frm_aliexpress(page)
    elif site_name == "citilink":
        return get_price_and_name_frm_citilink(page)
    elif site_name == "mvideo":
        return get_price_and_name_frm_mvideo(page)
    # elif site_name == "dns-shop":
    #     return get_price_and_name_frm_dns(page)
    elif site_name == "ebay":
        return get_price_and_name_frm_ebay(page)
    else:
        print(f"{Fore.RED}Invalid site name:{Fore.RESET} "
              f"{Fore.BLUE}{site_name}{Fore.RESET}")
        return None, None
