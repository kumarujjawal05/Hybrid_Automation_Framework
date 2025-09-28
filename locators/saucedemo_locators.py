
login_locators = {

    "username" : "user-name",
    "password" : "password",
    "login_button" : "login-button"
}

inventory_locators = {

    "inventory_items" : '//div[@class="inventory_item_name "]',
    "add_to_cart" : '//button[@class="btn btn_primary btn_small btn_inventory "]',
    

} 

checkout_locators = {
    "checkout" : "checkout",
    "firstName" : "first-name",
    "lastName" : "last-name",
    "zipCode" : "postal-code",
    "continue" : "continue",
    "finish" : "finish",
    "message" : "complete-header"

}

addtocart_locators = {
    "cart" : "shopping_cart_container",
    "product_list" : "//div[@class='inventory_item_name']"

}

logout_locators = {
    "menu" : "//button[@id='react-burger-menu-btn']",
    "logout" : "//a[@id='logout_sidebar_link']"

}