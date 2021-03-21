from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Enter Location of Project Here
driver =webdriver.Chrome(r"TODO")
driver.get('https://www.sce.com/customer-service/billing-payment/pay-my-bill')

PayWithCredit = driver.find_element_by_xpath('//*[@id="block-sce-responsive-content"]/div/article/div/section/div/div[2]/div/section/div/article/div/div[1]/div/div[2]/div/section[2]/article/p/a')
PayWithCredit.click()






Account = driver.find_element_by_xpath('//*[@id="enterAccInfoCustAccRNum"]')
#Enter Your Account Number Here
Account.send_keys('TODO')

FirstName= driver.find_element_by_xpath('//*[@id="enterAccInfoCustAccFName"]')
#Enter Your First Name Here
FirstName.send_keys('TODO')

LastName= driver.find_element_by_xpath('//*[@id="enterAccInfoCustAccLName"]')
#Enter Your Last Name Here
LastName.send_keys('TODO')

ZipCode= driver.find_element_by_xpath('//*[@id="rZipCode"]')
#Enter Your Zipcode Here
ZipCode.send_keys('TODO')

Next = driver.find_element_by_xpath('//*[@id="guestPayNext"]')
Next.click()








