from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_page
from pages.catalog_page import Catalog_page
from pages.fridges_catalog_page import Fridges_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.order_page import Order_page


#Test with authorization
def test_buy_fridge(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test")
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.redirect_to_catalog()

    cp = Catalog_page(driver)
    cp.redirect_fridges_catalog()

    fcp = Fridges_page(driver)
    fcp.set_filters()
    value_product_1_name_in_catalog = fcp.get_product_1_name_in_catalog().text
    print(value_product_1_name_in_catalog)
    value_price_product_1_in_catalog = fcp.get_price_product_1_in_catalog().text
    print(value_price_product_1_in_catalog)
    fcp.select_product()
    fcp.enter_to_cart()

    cp = Cart_page(driver)
    value_product_1_name_in_cart = cp.get_product_1_name_in_cart().text
    print(value_product_1_name_in_cart)
    value_product_1_price_in_cart = cp.get_product_1_price_in_cart().text[:-4]
    print(value_product_1_price_in_cart)
    cp.product_confirmation()
    assert value_product_1_name_in_cart == value_product_1_name_in_catalog
    print("Product name in catalog and in cart the same.")
    assert value_product_1_price_in_cart == value_price_product_1_in_catalog
    print("Product price in catalog and in cart the same.")

    op = Order_page(driver)
    op.input_order_info()
    value_product_1_name_in_order = op.get_product_1_name_in_order().text
    assert value_product_1_name_in_catalog.lower() == value_product_1_name_in_order.lower()
    print("Product name in catalog and in order the same.")
    value_total_price = op.get_total_price().text[:-4]
    assert value_total_price == value_product_1_price_in_cart
    print("Total price is correct")

    # print("Finish test")
    # driver.quit()
