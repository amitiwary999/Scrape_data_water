import selenium
from selenium import webdriver
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import csv

filename = "getannualdata.csv"
field = ['State_Name', 'District_Name', 'Data Type', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept',
         'oct', 'nov', 'dec']
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(field)
path_to_chromedriver = r'/home/meeera/chromedriver'  # change path as needed
browser = webdriver.Chrome(executable_path=path_to_chromedriver)
url = 'http://www.indiawaterportal.org/met_data/'
browser.get(url)
browser.implicitly_wait(20)
browser.find_elements_by_name('mForm')
el = Select(browser.find_element_by_id('stateSelect'))
opt = tuple(o.text for o in el.options)
for v in opt:  # selecting state
    if v == '--Select State--':
        continue
    elif v == 'ANDAMAN & NICOBAR ISLANDS':
        continue
    else:
        el.select_by_visible_text(v)
        print(v)
        browser.implicitly_wait(10)
        el2 = Select(browser.find_element_by_id('districtSelect'))
        opt2 = tuple(o.text for o in el2.options)
        for v2 in opt2:  # selecting state
            if v2 == '--Select District--':
                continue
            else:
                el2.select_by_visible_text(v2)
                print(v2)
                browser.implicitly_wait(10)
                el3 = Select(browser.find_element_by_id('dataTypeSelect'))
                opt3 = tuple(o.text for o in el3.options)
                for v3 in opt3:  # selecting state
                    if v3 == '--Select Data Type--':
                        continue
                    else:
                        el3.select_by_visible_text(v3)
                        print(v3)
                        browser.find_element_by_xpath(
                            '//*[@id="fromYearSelect"]/option[contains(text(), "1901")]').click()  # from year fixed
                        browser.find_element_by_xpath(
                            '//*[@id="toYearSelect"]/option[contains(text(), "2002")]').click()  # to year fixed
                        try:
                            browser.find_element_by_id('genButton').click()
                        except:
                            print("error")
                        browser.implicitly_wait(20)
                        try:
                            table = browser.find_element_by_xpath('//table[@id="dataTable"]/tbody')
                            browser.implicitly_wait(20)
                            trs = browser.find_elements(By.TAG_NAME, "tr")
                            # ths = trs[0].find_elements(By.TAG_NAME, "th")
                            tds = trs[1].find_elements(By.TAG_NAME, "td")

                            row = [v, v2, v3]
                            for t in tds:
                                # print(t.text)
                                row.append(t.text)

                            with open(filename, 'a') as csvfile:
                                # creating a csv writer object
                                csvwriter = csv.writer(csvfile)

                                # writing the data rows
                                csvwriter.writerow(row)
                                # csvwriter.writerow("\n")
                        except selenium.common.exceptions.NoSuchElementException:
                            continue

