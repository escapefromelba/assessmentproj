import pytest
import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DemoBlaze():


    def __init__(self, brandNewUserName):

        self.brandNewUserName = brandNewUserName;
        self.url = "https://www.demoblaze.com/index.html"
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.url)
        self.browser.implicitly_wait(30)

        #Top Links

        self.signUpButton = self.browser.find_element(by="id", value="signin2")
        self.loginButton = self.browser.find_element(by="id", value="login2")
        self.homeLink = self.browser.find_element(by="xpath", value="//*[@id=\"navbarExample\"]/ul/li[1]/a")
        self.cartLink = self.browser.find_element(by="xpath", value="//*[@id=\"cartur\"]")
        self.logOutButton = self.browser.find_element(by="id", value="logout2")

        #User Name and Password fields
        self.newUserName = self.browser.find_element(by="id", value="sign-username")
        self.newPassword = self.browser.find_element(by="id", value="sign-password")
        self.loginUserName = self.browser.find_element(by="id", value="loginusername")
        self.loginPassword = self.browser.find_element(by="id", value="loginpassword")
        self.completeSignUp = self.browser.find_element(by="xpath", value="//*[@id=\"signInModal\"]/div/div/div[3]/button[2]")
        self.loginModal = self.browser.find_element(by="xpath", value="//*[@id=\"logInModal\"]/div/div/div[3]/button[2]")

        #Order Items
        self.samSungS6 = self.browser.find_element(by="xpath", value="//*[@id=\"tbodyid\"]/div[1]/div/div/h4/a")
        self.nokia1520 = self.browser.find_element(by="xpath", value="//*[@id=\"tbodyid\"]/div[2]/div/div/h4/a")

    def createSignUp(self):
        self.signUpButton.click()
        time.sleep(1)
        self.newUserName.send_keys(self.brandNewUserName)
        self.newPassword.send_keys("password")
        self.completeSignUp.click()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("Trying to close alert again..")
            time.sleep(3)
            alert = self.browser.switch_to.alert
            alert.accept()
            signUpCloseButton = self.browser.find_element(by="xpath", value="//*[@id=\"signInModal\"]/div/div/div[3]/button[1]")
            signUpCloseButton.click()


    def login(self):
        try:
            self.loginButton.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying click log in, trying to find element again')
            time.sleep(2)
            self.loginButton = self.browser.find_element(by="id", value="login2")
            self.loginButton.click()
        time.sleep(1)

        try:
            self.loginUserName.send_keys(self.brandNewUserName)
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying enter username, trying to find element again')
            time.sleep(2)
            self.loginUserName = self.browser.find_element(by="id", value="loginusername")
            self.loginUserName.send_keys(self.brandNewUserName)

        try:
            self.loginPassword.send_keys("password")
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying enter password, trying to find element again')
            time.sleep(2)
            self.loginPassword = self.browser.find_element(by="id", value="loginpassword")
            self.loginPassword.send_keys("password")

        try:
            self.loginModal.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying click login, trying to find element again')
            time.sleep(2)
            self.loginModal = self.browser.find_element(by="xpath", value="//*[@id=\"logInModal\"]/div/div/div[3]/button[2]")
            self.loginModal.click()



    def addTwoItems(self):

        addToCart = self.browser.find_element(by="xpath", value="//*[@id=\"tbodyid\"]/div[2]/div/a")

        try:
            self.samSungS6.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying click samsung, trying to find element again')
            self.samSungS6 = self.browser.find_element(by="xpath", value="//*[@id=\"tbodyid\"]/div[1]/div/div/h4/a")
            self.samSungS6.click()

        try:
            addToCart.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying click add to cart, trying to find element again')
            addToCart = self.browser.find_element(by="xpath", value="//*[@id=\"tbodyid\"]/div[2]/div/a")
            addToCart.click()

        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("Trying to close alert again..")
            time.sleep(3)
            alert = self.browser.switch_to.alert
            alert.accept()

        try:
            self.homeLink.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying click home, trying to find element again')
            self.homeLink = self.browser.find_element(by="xpath", value="//*[@id=\"navbarExample\"]/ul/li[1]/a")
            self.homeLink.click()

        try:
            self.nokia1520.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying to click nokia, trying to find element again')
            self.nokia1520 = self.browser.find_element(by="xpath", value="//*[@id=\"tbodyid\"]/div[2]/div/div/h4/a")
            self.nokia1520.click()

        try:
            addToCart.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying click add to cart, trying to find element again')
            addToCart = self.browser.find_element(by="xpath", value="//*[@id=\"tbodyid\"]/div[2]/div/a")
            addToCart.click()

        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("Trying to close alert again..")
            time.sleep(3)
            alert.accept()

        try:
            self.cartLink.click()
        except StaleElementReferenceException:
            print('StaleElementReferenceException while trying click add to cart, trying to find element again')
            self.cartLink = self.browser.find_element(by="xpath", value="//*[@id=\"cartur\"]")
            self.cartLink.click()

        placeOrderButton = self.browser.find_element(by="xpath", value="//*[@id=\"page-wrapper\"]/div/div[2]/button")
        placeOrderButton.click()

    def fillAndCancel(self):

        #orderSummary

        # self.deleteButton2 = self.browser.find_element(by="xpath", value="/html/body/div[6]/div/div[1]/div/table/tbody/tr[2]/td[4]/a")
        # orderpage
        orderName = self.browser.find_element(by="id", value="name")
        orderCountry = self.browser.find_element(by="id", value="country")
        orderCity = self.browser.find_element(by="id", value="city")
        orderCC = self.browser.find_element(by="id", value="card")
        orderMonth = self.browser.find_element(by="id", value="month")
        orderYear = self.browser.find_element(by="id", value="year")
        closeButton = self.browser.find_element(by="xpath", value="//*[@id=\"orderModal\"]/div/div/div[3]/button[1]")

        orderName.send_keys("Jacob")
        orderCountry.send_keys("USA")
        orderCity.send_keys("Rockville")
        orderCC.send_keys("Nice Try")
        orderMonth.send_keys("June")
        orderYear.send_keys("2022")
        closeButton.click()

    def placeAndDeleteOrder(self, numberDeleted):
        deleteButton1 = self.browser.find_element(by="xpath", value="//*[@id=\"tbodyid\"]/tr/td[4]/a")
        # deleteButton2 = self.browser.find_element(by="xpath", value="//*[@id=\"tbodyid\"]/tr[1]/td[4]/a")


        for i in range(0, numberDeleted):
            try:
                deleteButton1.click()
                time.sleep(2)
            except StaleElementReferenceException:
                print('StaleElementReferenceException while trying click delete, trying to find element again')
                time.sleep(2)
                deleteButton1 = self.browser.find_element(by="xpath", value="//*[@id=\"tbodyid\"]/tr/td[4]/a")
                deleteButton1.click()

        try:
            self.logOutButton.click()
        except StaleElementReferenceException:
            print('StaleElementReferenceException while trying click delete, trying to find element again')
            time.sleep(2)
            self.logOutButton = self.browser.find_element(by="id", value="logout2")
            self.logOutButton.click()

    def countShoppingCartItems(self):
        try:
            self.cartLink.click()
        except StaleElementReferenceException:
            print('StaleElementReferenceException while trying click add to cart, trying to find element again')
            time.sleep(2)
            self.cartLink = self.browser.find_element(by="xpath", value="//*[@id=\"cartur\"]")
            self.cartLink.click()

        time.sleep(2)
        rows = self.browser.find_elements(by="xpath", value="//*[@id=\"tbodyid\"]/tr")

        print("There are "+str(len(rows))+ " items in the cart")

        try:
            self.homeLink.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying click home, trying to find element again')
            self.homeLink = self.browser.find_element(by="xpath", value="//*[@id=\"navbarExample\"]/ul/li[1]/a")
            self.homeLink.click()


j=DemoBlaze("acme112")
j.createSignUp()
j.login()
j.addTwoItems()
j.fillAndCancel()
j.placeAndDeleteOrder(2)
j.login()
j.countShoppingCartItems()
j.addTwoItems()
j.fillAndCancel()
j.placeAndDeleteOrder(1)


