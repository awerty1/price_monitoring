from colorama import Fore

from marketplaces import get_price_and_name_frm_wildberries
from marketplaces import get_price_and_name_frm_ozon
from marketplaces import get_price_and_name_frm_ymarket
from marketplaces import get_price_and_name_frm_smm

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
    else:
        print(f"{Fore.RED}Invalid site name:{Fore.RESET} "
              f"{Fore.BLUE}{site_name}{Fore.RESET}")
        return None, None
