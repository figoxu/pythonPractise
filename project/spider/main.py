
from selenium import  webdriver

driver = webdriver.Firefox()

driver.get("https://blog.csdn.net/zhuchen233/article/details/53398234")
em = driver.find_element_by_class_name("read-count")
print(em.text)
em = driver.find_element_by_css_selector(".hide-article-box")
em.click()
driver.quit()

