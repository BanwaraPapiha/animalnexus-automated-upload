from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass
import csv
asset = []
not_added = []


def main():
    login()
    with open('test1.csv', 'r') as df:
        reader = csv.reader(df)
        next(reader)
        for line in reader:
            asset.append(line)
            CompanyName = line[1]
            ProductName = line[0]
            DealerPrice = line[2]
            CostumerPrice = line[3]
            print(f'Adding {ProductName} of price {CostumerPrice}?')
            insert_data(CompanyName, ProductName, DealerPrice, CostumerPrice)
    print(asset)


def login():
    user_email = input("Please Enter your Email here: ")
    user_pass = getpass.getpass("\nPlease Enter your password here: ")
    print("\n\nPlease wait for the Browser to open...\n")
    global driver
    driver = webdriver.Chrome(r"C:\Users\muham\pyscraping\chromedriver")
    driver.get("https://www.animalnexus.com.pk/admin")
    # FOLLOWING CODE IS JUST LOGGING IN THE USER
    driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div[1]/input').send_keys(user_email)
    driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div[2]/input').send_keys(user_pass)
    driver.find_element_by_xpath('//*[@id="loginForm"]/button').click()
    print("\nTrying to Log in")
    time.sleep(3)
    # FOLLOWING CODE LEADS US TO DESTINATION AFTER LOGIN
    driver.find_element_by_xpath(
        '/html/body/div[2]/aside/div/nav/ul/li[3]/a/p').click()
    print("Clicked on Products")
    driver.find_element_by_xpath(
        '/html/body/div[2]/aside/div/nav/ul/li[3]/ul/li[1]/a/p').click()
    print("Function login is executed successfully")


def insert_data(company, product, cost, price):
    driver.refresh()
    try:
        # Company
        driver.find_element_by_xpath(
            '//*[@id="select2-brand_id-container"]').click()
        driver.find_element_by_xpath(
            '/html/body/span/span/span[1]/input').send_keys(company)
        print('Company')
        # Category
        driver.find_element_by_xpath(
            '//*[@id="select2-sel_category_id-container"]').click()
        driver.find_element_by_xpath(
            '/html/body/span/span/span[1]/input').send_keys('Livestock')
        print('Company')
        # Product
        driver.find_element_by_xpath(
            '/html/body/span/span/span[1]/input').send_keys(Keys.RETURN)
        driver.find_element_by_xpath(
            '//*[@id="product_name_id"]').send_keys(product)
        print('product')
        # Dealer Price or Cost
        driver.find_element_by_xpath(
            '//*[@id="deal_price_id"]').send_keys(cost)
        print('cost')
        # Costumer Price
        driver.find_element_by_xpath(
            '//*[@id="product_price_id"]').send_keys(price)
        print('price')
        # Submit
        driver.find_element_by_xpath(
            '//*[@id="itemBtn"]').send_keys(Keys.RETURN)
        print('submit')
        time.sleep(2)
    except:
        print("Operation cancelled. Some Problem occured on your side.")
        print(f'{product} of Comapny: {company} with cost of {cost} and price of {price} has not been added')
        time.sleep(2)
    print(not_added)


main()
