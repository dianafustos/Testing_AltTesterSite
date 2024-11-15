# used to add pauses (to better understand and see what will be executed)
import time

# used to wait for the loading of the pages
from selenium.webdriver.support.ui import WebDriverWait

# importing the Selenium webdriver, to control the web browser through the tests written in Python
from selenium import webdriver

# importing the Service class, which manages the ChromeDriver
from selenium.webdriver.chrome.service import Service

# importing ChromeDriverManager, which automatically installs the correct version of ChromeDriver for the version of Chrome installed on my system
from webdriver_manager.chrome import ChromeDriverManager

# other imports: By for locating elements. EC comes from expected conditions, used with Wait - if then, else
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# this creates an instance of ChromeOptions, which will allow me to customise the settings of the Chrome browser (see below)
options = webdriver.ChromeOptions()

# remove "sandbox" security feature, a permission issue
options.add_argument('--no-sandbox')
# prevents Chrome from crashing
options.add_argument('--disable-dev-shm-usage')

# Setting up the ChromeDriver 'Service' using 'ChromeDriverManager'
# installs the correct version
service = Service(ChromeDriverManager().install())



# webDriver:
# We launching a new Chrome browser window controlled by Selenium
# service configures the driver, the ChromeDriver 
# and options customises the browser's - Chrome’s settings
# The 'Ddriver' object is our MAIN TOOL TO CONTROL Chrome
driver = webdriver.Chrome(service=service, options=options)

# opening the AltTeser site
driver.get("https://alttester.com")
time.sleep(2)

# prints the title of the page - the current page
print("The title of the site is:", driver.title)

#Accept button
try:
    # Locate the "Accept" button
    accept_cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wt-cli-accept-btn"]'))
    )
    # Click the button
    accept_cookies_button.click()
    print("Clicked on 'Accept' button for cookies")
except Exception as e:
    print("Accept button could not be clicked:", e)
time.sleep(2)


# we navigate to Tools page:
# first, we use find_element method from Selenium to locate this element - Tools on the page
# "link text" is used to search for a link
tools_link = driver.find_element("link text", "Tools")
# we click on Tools
tools_link.click()
# Now we are on Tools page 

# wait 3 second for the Tools page to load and get some time to see it
time.sleep(2)

# check if the text in URL includes the word "tools"
assert "tools" in driver.current_url, "Tools page is not loading"
# make the test fail:
#assert "toolss" in driver.current_url, "Tools page is not loading"

# check elements on the Tools page. Make sure they are visible
# check if the see pricing button is displayed and click on it
see_pricing_button = driver.find_element("link text", "See pricing")
try:
    see_pricing_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/header/div/div[1]/div/div[1]/div[1]/div/div[1]/a'))
    )

    if see_pricing_button.is_displayed():
        print("'See Pricing' button is displayed")
        
    # click
        see_pricing_button.click()
        print("Clicked on 'See Pricing' button")
    else:
        print("'See Pricing' button is not displayed on the Tools page")

except Exception as e:
    # print an error message
    print("Error: Unable to spot 'See the pricing'", e)

# wait 2 seconds to see the page
time.sleep(2)

#why do the page scrolls? 

# "Buy" a free subscription of AltTester
#First, click on Start Free Trial (AltTester® Pro)
#see_start_free_trial_button = driver.find_element("link text", "Start free trial")
try:
    see_start_free_trial_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-button-17484"]'))
    )

    if see_start_free_trial_button.is_displayed():
        print("'Start free trial' button is displayed")
        
    # click
        see_start_free_trial_button.click()
        print("Clicked on 'Start Free Trial' button")
    else:
        print("'Start free trial' button is not displayed")

except Exception as e:
    # print an error message
    print("Error: Unable to spot 'Start free trial'", e)
time.sleep(1)

#check user is on Cart's page
# verify the URL
try:
    #wait
    WebDriverWait(driver, 10).until(EC.url_contains("/cart/"))
    print("User is on Cart's page")
except Exception as e:
    print("Error: User did not get to the Cart's page", e)    

#assert driver.current_url == "https://alttester.com/cart/", "User did not navigate to the Cart's page"
#print ("User got to Cart's page")
#click Next
# make sure the button Next is visible
next_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div/a')
#scroll - we use JavaScript
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", next_button)
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div/a'))
    )
    if next_button.is_displayed():
        print("'Next' button is displayed")
    else:
        print("'Next' button is not displayed")
except Exception as e:
    print("Error: Unable to see the Next button", e)
        
#click
time.sleep(1)
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div/a')))
#next_button.click()

try:
    next_button.click()
    print("Clicked on 'Next' button")
except Exception as e:
    print("Error: Unable to click on the the Next button", e)

time.sleep(1)

#check user is on Checkout page
# verify the URL
try:
    #wait
    WebDriverWait(driver, 10).until(EC.url_contains("/checkout/"))
    print("User is on Checkout page")
except Exception as e:
    print("Error: User did not get to the Checkout page", e)

#Fill in the fields in order to buy a product
try:
    email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='billing_email']"))
    )
    email_field.click()
    print("Clicked on the Email field")
except Exception as e:
    print("Error: Not able to click on email field")

email_field.clear()
email_field.send_keys("diana.fustos+777@icloud.com")    

print("Email entered successfully")

#close the browser
driver.quit()