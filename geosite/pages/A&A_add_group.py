from selenium import webdriver


URL = 'http://localhost:8080'

driver = webdriver.Chrome()
driver.get(URL)

# Authentication and Authorization Objects
linktext_Groups = 'Groups'
linktext_Users = 'Users'
linktext_Add = 'Add'
linktext_Change = 'Change'

#  Core_Admin Objects
linktext_Add = 'Add'
css_core_admin = '.app-core_admin caption'  
linktext_Add = 'Change'

#Core Admin object

css_ca_add_link ='.model-organization .addlink'
css_ca_change_link = '.model-organization .changelink'
css_mo_add_link = '.model-subscription .addlink'
css_mo_change_link = '.model-subscription .changelink'


def click_linktext(webdriver, object):
    driver.find_element_by_link_text(object).click()

def click_link_css(webdriver, object):
    driver.find_elements_by_css_selector(object).click()

    