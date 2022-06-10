from main import DemoBlaze

j = DemoBlaze("acme112")

def test_CreateSignUp():
    j.createSignUp()

def test_Login1():
    j.login()

def test_AddTwoItems():
    j.addTwoItems()

def test_FillAndCancel():
    j.fillAndCancel()

def testPlaceAndDeleteOrder1():
    j.placeAndDeleteOrder(2)

def test_Login2():
    j.login()

def test_CountItems():
    j.countShoppingCartItems()

def test_AddTwoItems2():
    j.addTwoItems()

def test_FillAndCancel2():
    j.fillAndCancel()

def test_PlaceAndDeleteOrder2():
    j.placeAndDeleteOrder(1)