from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import string


def wait_for_element(attribute, value):
    while True:
        try:
            driver.find_element(attribute, value)
            sleep(0.5)
            break
        except NoSuchElementException:
            pass


def random_string(n):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(n))
    return result_str

def add_products(n):
    product_ids = random.sample(range(0, 12), n)
    for i in range(n):
        driver.find_elements(By.CLASS_NAME, "product")[product_ids[i]].click()
        driver.find_element(By.CLASS_NAME, "add-to-cart").click()
        wait_for_element(By.ID, "blockcart-modal")
        driver.find_element(By.ID, "blockcart-modal").find_element(By.TAG_NAME, "button").click()
        driver.find_element(By.ID, "wrapper").find_elements(By.TAG_NAME, "a")[1].click()

if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost/")
    action_chain = ActionChains(driver)
    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()

#Creating new account
    first = driver.find_element(By.CLASS_NAME, "hidden-sm-down")
    first.find_element(By.CLASS_NAME, "hidden-sm-down").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Nie masz konta? Załóż je tutaj").click()
    sleep(0.5)
    driver.find_element(By.ID, "field-id_gender-" + str(random.randint(1, 2))).click()
    driver.find_element(By.ID, "field-firstname").send_keys(random_string(random.randint(5, 10)))
    driver.find_element(By.ID, "field-lastname").send_keys(random_string(random.randint(5, 10)))
    driver.find_element(By.ID, "field-email").send_keys(random_string(random.randint(5, 10)) + "@yahoo.com")
    driver.find_element(By.ID, "field-password").send_keys(random_string(20))
    sleep(0.5)
    driver.find_element(By.NAME, "psgdpr").click()
    sleep(0.5)
    driver.find_element(By.NAME, "customer_privacy").click()
    driver.find_element(By.CLASS_NAME, "form-control-submit").click()
    sleep(0.5)

#First category
    action_chain.move_to_element(driver.find_element(By.CLASS_NAME, "dropdown-item")).perform()
    sleep(0.5)
    driver.find_element(By.ID, "category-18").click()

#Add 5 random products in a category
    add_products(5)

#Second category
    driver.find_element(By.PARTIAL_LINK_TEXT,"minimalistyczny").click()

#Add 5 random products
    add_products(5)

#Remove from cart
    driver.find_element(By.ID, "_desktop_cart").click()
    driver.find_element(By.CLASS_NAME, "remove-from-cart").click()
    sleep(0.5)

#Complete Order
    driver.find_element(By.CLASS_NAME, "cart-detailed-actions").click()
    driver.find_element(By.ID, "field-address1").send_keys(random_string(8) + str(random.randint(1, 9)))
    driver.find_element(By.ID, "field-postcode").send_keys(str(random.randint(10, 99)) + "-" + str(random.randint(100, 999)))
    driver.find_element(By.ID, "field-city").send_keys(random_string(10))
    sleep(3)
    driver.find_element(By.NAME, "confirm-addresses").click()
    wait_for_element(By.NAME, "confirmDeliveryOption")
    driver.find_element(By.NAME, "confirmDeliveryOption").click()
    wait_for_element(By.ID, "payment-confirmation")
    driver.find_element(By.ID, "payment-option-1").click()
    driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
    driver.find_element(By.CLASS_NAME, "btn.btn-primary.center-block").click()
    wait_for_element(By.ID, "content-hook_order_confirmation")

    # Order Status check
    driver.find_element(By.CLASS_NAME, "account").click()
    driver.find_element(By.ID, "history-link").click()
    sleep(5)

    # Exit
    driver.quit()