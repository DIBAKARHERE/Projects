import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options() #create options class

#we can add multiple arguments like below as characteristics & pass them to webdriver class ***

# options.add_argument("--start-maximized")
options.add_argument("--headless=new") #to run automation in headless way, i.e. code will run in backend no frontend will show
options.add_argument("--window-size=1920,1080")
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options = options)

driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()

#Page scroll from browser window ***

#steps - inspect page > click on console
#command1 - window.scrollBy(0,500) (500 value as y-axis to scroll down the page)
#command2 - window.scrollBy(0,document.body.scrollHeight) (scrollHeight value scroll down to the maximum length of the page)
#command3 - window.scrollTo(0,0) (scroll up to the top of the page)

driver.execute_script("window.scrollBy(0,500)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
driver.save_screenshot("screenshot10.png")
#driver.get_screenshot_as_file("screenshot5.png") #alternate way to capture screenshot
driver.execute_script("window.scrollTo(0,0)")