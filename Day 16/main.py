from settings import PASSWORD, LOGIN, SITE_URL
from work_with_browser import open_browser, close_browser, parse_page, parse_site
from olx_item.package_module_1 import package_module_1


def main():
    open_browser("Chrome")
    parse_site(SITE_URL)
    parse_page(SITE_URL)
    close_browser("Firefox")
    print(package_module_1)


main()
