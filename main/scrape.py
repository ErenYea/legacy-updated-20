from selenium import webdriver
from selenium.webdriver.chrome import options
import time,csv
import re, datefinder
import main.constants as const
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.common.proxy import Proxy, ProxyType
# import spacy

# load english language model


# import undetected_chromedriver as uc
# import win32com.client as win32

import os
# desired_cap = {
#  'browser': 'chrome',
#  'browser_version': 'latest',
#  'os': 'Windows',
#  'os_version': '10',
#  'build': 'Python Sample Build',
#  'name': 'Pop-ups testing'
# }
# desired_cap["chromeOptions"] = {}
# desired_cap["chromeOptions"]["excludeSwitches"] = ["disable-popup-blocking"]

# self = webdriver.Remote(
#     command_executor='https://YOUR_USERNAME:YOUR_ACCESS_KEY@hub-cloud.browserstack.com/wd/hub',
#     desired_capabilities=desired_cap
#     )

class Scrape(webdriver.Chrome):
    options = webdriver.ChromeOptions() 
    # options = webdriver.ChromeOptions() 
    # options.add_argument("start-maximized")
    # webdriver.DesiredCapabilities.CHROME
    options.headless = False
    # options.add_argument("window-size=1200x600")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.headless = False
    options.add_argument("--disable-infobars")
    # options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")    
    options.add_argument("window-size=1200x600")
    options.add_argument("test-type")
    options.add_argument('--disable-useAutomationExtension')
    # options.add_experimental_option('useAutomationExtension', False)
    # options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--disable-xss-auditor")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-webgl")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("no-default-browser-check")
    options.add_argument("--disable-notifications")
    # py = '103.205.28.238:8080'
    # py = '101.99.95.54:80'
    capabilities = options.to_capabilities()
    # nlp = spacy.load('en_core_web_sm')
    # capabilities = {
    #     'browserName': 'chrome',
    #     'chromeOptions':  {
    #         'useAutomationExtension': False,
    #         'forceDevToolsScreenshot': True,
    #         'args': ['--disable-infobars','--disable-setuid-sandbox','--disable-popup-blocking','--disable-notifications','--allow-running-insecure-content','--disable-web-security','--disable-extensions']
    #     }
    # }
    
    # py = '136.228.141.154:80'
    # options.add_argument('--proxy-server=%s' % py)
    # options.add_argument("no-first-run")
    # options.add_argument("disable-gpu")
   
    # prox = Proxy()
    # prox.proxy_type = ProxyType.MANUAL
    # prox.http_proxy = "185.125.169.24:8118"
    # prox.socks_proxy = "185.125.169.24:8118"
    # prox.ssl_proxy = "185.125.169.24:8118"

    # capabilities = webdriver.DesiredCapabilities.CHROME
    # prox.add_to_capabilities(capabilities)

    # self = webdriver.Chrome(desired_capabilities=capabilities)


    # initializing the webdriver instance

    def __init__(self, ):
        
        super(Scrape, self).__init__(desired_capabilities=self.capabilities)
        # self = uc.Chrome(options=self.options)
        self.result = {}
        self.results = {}
        self.state = None
        self.states = {}
        self.city = None
        self.cities = []
        self.date_from = None
        self.date_to = None
        self.count = 1
        self.absPath = os.path.abspath('results.xlsx')
        # self = uc.Chrome(options=options)
       
        # pythoncom.CoInitialize()
        # self.dff = pd.read_excel('results.xlsx')
       
        # self.ExcelApp = win32.gencache.EnsureDispatch("Excel.Application")
        # self.ExcelApp.Visible = True
        # self.ExcelApp.WindowState = win32.constants.xlMaximized
       
        self.headers = ['State', 'City', 'Range of Dates from:', 'Range of Dates to:', 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS', 'FULL NAME OF THE DECEASED PERSON WITH COMMAS', 'YEAR OF BIRTH', 'YEAR OF DEATH', 'DATE OF DEATH', 'Funeral Home Name',
                            'Funeral Home Street Address', 'Funeral Home City', 'Funeral Home State', 'Funeral Home ZIP Code', 'Upcoming Service Name', 'Upcoming Service Date', 'Upcoming Service City', 'List of Next of Kin', "Link to the deceased person's obituary"]
        # self.df = pd.DataFrame([],columns=self.headers)
        with open("results.csv", 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', 
                                fieldnames=self.headers)
            dw.writeheader()
        with open("error.csv", 'w',newline='') as file:
            dw = csv.DictWriter(file, delimiter=',', 
                                fieldnames=['URL'])
            dw.writeheader()
        # if len(self.dff) == 0:


        #     self.wb = self.ExcelApp.Workbooks.Open(self.absPath)
            
        #     self.ws = self.wb.Worksheets("Sheet1")
           
            
        #     for i in range(1,len(self.headers)+1):
        #         self.ws.Cells(1,i).Value = self.headers[i-1]
        #         self.ws.Cells(1,i).Font.Name = 'Verdana'
        #         self.ws.Cells(1,i).Font.Size = 13
        #         self.ws.Cells(1,i).Font.Bold = True
                
        # else:
        #     self.wb = self.ExcelApp.Workbooks.Open(self.absPath)
            
        #     self.ws = self.wb.Worksheets("Sheet1")    
        #     for i in range(1,len(self.headers)+1):
        #         self.count = 2
        #         self.ws.Cells(1,i).Value = self.headers[i-1]
        #         self.ws.Cells(1,i).Font.Name = 'Verdana'
        #         self.ws.Cells(1,i).Font.Size = 13
        #         self.ws.Cells(1,i).Font.Bold = True
        #         for j in self.dff[self.headers[i-1]]:
        #             if str(j) == 'nan':
        #                 self.ws.Cells(self.count,i).Value = "-"
        #             else:
        #                 self.ws.Cells(self.count,i).Value = str(j)
        #             self.count += 1
                

        # self.ws.Columns.AutoFit()
        # self.ws.Rows.AutoFit()
        
        self.implicitly_wait(const.IMPLICIT_WAIT)
        
        self.keywords = pd.read_csv('keywords.csv')
        # self.URLS = pd.read_csv('error.csv')
        # self.keyword = list(self.keywords)
        # with open('file.csv','r') as f:
        #     csv_reader = csv.reader(f)
        #     self.csv_list = []
            
        #     for i in csv_reader:
        #         print(i)
        #         if len(i) == 0:
        #             continue
        #         self.csv_list.append(i[0])
        # print(self.csv_list) 

    # Loading the frist page
    def land_on_first_page(self):
        self.get(const.BASE_URL)

    def click_on_popup(self):

        btn = self.find_element_by_xpath(
            "//div[@class='fc-dialog-container']/div/div[2]/div[2]/button")

        print(btn)

        btn.click()
    
    def ad_pop_up(self):
        element = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="fEy1Z2XT "]/div/div/div/div[3]/span/button')))
        # element = self.find_element_by_xpath('//div[@class="fEy1Z2XT "]/div/div/div/div[3]/span/button')
        element.click()
         

    # Selecting the country
    def select_contry(self):
        select = Select(self.find_element_by_id(
            'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_uxSearchWideControl_ddlCountry'))
        select.select_by_visible_text('United States')

    # Getting the names of state

    def get_states(self):
        states = self.find_elements_by_xpath(
            "//select[@id='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_uxSearchWideControl_ddlState']/option")
        for i in states:
            print(f"Value: {i.get_attribute('value')} , Text: {i.text}")
            self.states[i.get_attribute('value')] = i.text

    # Takingt the input of state
    def input_state(self, state=''):
        try:
            select = Select(self.find_element_by_id(
                'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_uxSearchWideControl_ddlState'))
        except:
            select = Select(self.find_element_by_xpath('//select[@name="ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$uxSearchWideControl$ddlState"]'))

        if state == '':
            
            select.select_by_value('57')
            self.state = self.states['57']
            
        else:
            
            select.select_by_visible_text(state)
            self.state = state

     # selecting the keywords
    def keyword(self, keyword=''):
        self.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        
        button = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_uxSearchWideControl_txtKeyword')))
        print(button)
        
        key = self.find_element_by_xpath(
            '//div[@class="trKeyword"]/input')
        
        self.city = keyword
        
        try:

            key.clear()
        except:
            button = WebDriverWait(self, 10).until(EC.element_located_to_be_selected((By.ID, 'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_uxSearchWideControl_txtKeyword')))
            print(button)
            ActionChains(self).move_to_element(key).click(key).perform()
            key.clear()
        key.send_keys(keyword)

    # Selecting the date

    def select_date(self):
        select = Select(self.find_element_by_id(
            'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_uxSearchWideControl_ddlSearchRange'))
        select.select_by_value('88888')

    # Selcting the date range
    def date_range(self, date_from='02/12/2020', date_to='02/12/2021'):
        div_tag_for_date = self.find_elements_by_class_name('DateValue')
        self.date_from = date_from
        self.date_to = date_to
        print(len(div_tag_for_date))
        date_from_tag = div_tag_for_date[0].find_element_by_tag_name('input')
        date_to_tag = div_tag_for_date[1].find_element_by_tag_name('input')
        date_from_tag.clear()
        date_to_tag.clear()
        date_from_tag.send_keys(date_from)
        date_to_tag.send_keys(date_to)

    # Clicking on search button
    def search(self):
        search = self.find_element_by_link_text("Search")
        search.click()

    # testing the condtition of result
    def get_result(self):
        try:

            txt = self.find_element_by_xpath("//div[@class='InlineTotalCountText']").text
            lst = [int(x) for x in txt.split() if x.isdigit()]
            print(max(lst))
            if max(lst) <= 10:
                return "less than 10"
        except:
            try:
                result = self.find_element_by_class_name('RefineMessage').text
                print(result)
                if '1000+' in result:
                    return True
                elif 'did not find any obituaries' in result:
                    return 'Didnot'
                else:
                    return False
            except:
                return False

    def click_all_results(self):
        try:
            result = self.find_element_by_class_name('RefineMessage').text
            if 'View all results.' in result:
                self.find_element_by_id(
                    'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_uxSearchLinks_ViewAllLink').click()
        except:
            pass

    # scrolling down the window to show all the results
    def scrolldown(self):
        # Get scroll height
        last_height = self.execute_script("return document.body.scrollHeight")
        print(f"last_height {last_height}")

        while True:
            # Scroll down to bottom
            self.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(const.SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def result_to_csv(self, name='result.csv'):
        results = self.find_elements_by_xpath('//div[@class="mainScrollPage"]')
        self.result = {}
        for i in results:
            a = i.find_elements_by_class_name('entryContainer')
            print(len(a))
            for j in a:
                s = j.find_element_by_class_name("obitName")
                h = s.find_element_by_tag_name('a')
                
                # if h.get_attribute('href') in self.csv_list:
                #     continue
                print(f"TExt: {s.text}  link: {h.get_attribute('href')}")
                
                self.result[s.text] = h.get_attribute('href')
                print("\n")
        self.close()


    def legacy(self,driver):
        try:
            # paras = self.find_element_by_xpath("//div[@data-component='ObituaryParagraph']").text.strip()
            para = driver.find_element_by_xpath("//div[@data-component='ObituaryParagraph']").text.split('.')
            date_of_death = '-'
            dob = '-'
            dod = '-'
            try:
                dob = driver.find_element_by_xpath("//div[@class='Box-sc-5gsflb-0 iobueB']/div/div/div/div").text
                dod = driver.find_element_by_xpath("//div[@class='Box-sc-5gsflb-0 iobueB']/div/div[2]/div/div").text
                if '/' in dob:
                    dob = dob.split('/')[-1]
                if '/' in dod:
                    dod  = dod.split('/')[-1]
                else:
                    try:
                        match  = datefinder.find_dates(dob)   
                        if len(list(match)) == 0:
                            if dob.isnumeric():
                                pass
                            else:
                                dob = '-'
                        
                        else:
                            match  = datefinder.find_dates(dob)
                            for j in match:
                                # date_of_bith = f"{j.month}/{j.day}/{j.year}"
                                dob = j.year
                                print(j)
                                break
                    except:
                        dob='-'
                    try:
                        match  = datefinder.find_dates(dod)
                        if len(list(match)) == 0:
                            if dod.isnumeric():
                                pass
                            else:
                                dod = '-'
                        
                        else:
                            for j in match:
                                try:
                                    date_of_death = f"{j.month}/{j.day}/{j.year}"
                                except:
                                    date_of_death='-'
                                dod = j.year
                                print(j)
                                break
                    except:
                        dod = '-'
                
            except:
                dob = '-'
                dod = '-'
                
            try:
                funeral_home_list = driver.find_element_by_xpath("//div[@class='Box-sc-5gsflb-0 iobueB']/div[2]/div").text.split('\n')
                funeral_home_name = funeral_home_list[1]
                funeral_home_street = funeral_home_list[2]
                funeral_home_city = funeral_home_list[3].split(',')[0]
                funeral_home_state = funeral_home_list[3].split(',')[1]
                funeral_home_zipcode = '-'
                
            except:
                try:
                    funeral_home_list = driver.find_element_by_xpath("//div[@class='Box-sc-5gsflb-0 iobueB']/div[2]/div").text.split('\n')
                    funeral_home_name = funeral_home_list[1]
                    funeral_home_street = funeral_home_list[2]
                    funeral_home_city = funeral_home_list[3].split(',')[0]
                    funeral_home_state = funeral_home_list[3].split(',')[1]
                    funeral_home_zipcode = '-'
                except:
                    funeral_home_name = '-'
                    funeral_home_street = '-'
                    funeral_home_city = '-'
                    funeral_home_state = '-'
                    funeral_home_zipcode = '-'
            
            # try:
            #     if date_of_death == '-':
            #         for i in para:
            #             if 'passed away' in i.strip().lower():
            #                 a= i.split('passed away')[-1].split('.')[0]
            #                 match  = datefinder.find_dates(a.strip())
            #                 if len(list(match)) == 0:
            #                     a= i.split('passed away')[0].split('.')[0]
            #                     match  = datefinder.find_dates(a.strip())
            #                     for j in match:
            #                         date_of_death = f"{j.month}/{j.day}/{j.year}"
            #                         dod = j.year
            #                         print(j)
            #                         break
            #                 else:
            #                     for j in match:
            #                         date_of_death = f"{j.month}/{j.day}/{j.year}"
            #                         dod = j.year
            #                         print(j)
            #                         break
            #                 break
            #             elif 'died' in i.strip().lower():
            #                 a = i.split('died')[-1]
            #                 match  = datefinder.find_dates(a.strip())
            #                 if len(list(match)) == 0:
            #                     a= i.split('died')[0].split('.')[0]
            #                     match  = datefinder.find_dates(a.strip())
            #                     for j in match:
            #                         date_of_death = f"{j.month}/{j.day}/{j.year}"
            #                         dod = j.year
            #                         print(j)
            #                         break
            #                 else:
            #                     for j in match:
            #                         date_of_death = f"{j.month}/{j.day}/{j.year}"
            #                         dod = j.year
            #                         print(j)
            #                         break
            #                 break
            #             else:
            #                 date_of_death = '-'
            #     else:
            #         pass

            # except:
            #     date_of_death = '-'
            fullname = driver.find_element_by_xpath('//div[@data-component="NameHeadingText"]').text.strip()
            TITLE = r"(?:[A-Z][a-z]\.\s)?"
            NAME1 = r"[A-Z][a-z]+,?\s+"
            MIDDLE_I = r"(?:[A-Z][a-z]\.?\s)?"
            NAME2 = r"[A-Z][a-z]+"
            res = re.findall(TITLE + NAME1 + MIDDLE_I + NAME2, para[0])
            if len(res) != 0:
                if 'In Loving Memory' in res[0]:
                    full_name = res[1]

                else:
                    full_name = res[0]
                if len(fullname) < len(full_name):
                    fullname =full_name
            if ',' in fullname:
                full_name_with_commas = fullname
                full_name_without_commas = ''
            else:
                full_name_with_commas = ''
                full_name_without_commas = fullname


            try:
                upcoming_service_list = driver.find_elements_by_xpath("//div[@class='Box-sc-5gsflb-0 bQzMjo']/div[2]/div[@class='Box-sc-5gsflb-0 kwgeEM']")[0].text.split('\n')
                if 'Plant Memorial Trees' in upcoming_service_list[-1]:
                    upcoming_service_month = ''
                    upcoming_service_day = '-'
                    upcoming_service_name = '-'
                else:
                    upcoming_service_month = upcoming_service_list[0]
                    upcoming_service_day = upcoming_service_list[1]
                    upcoming_service_name = upcoming_service_list[2]
            except:
                upcoming_divs = driver.find_elements_by_xpath("//div[@class='Box-sc-5gsflb-0 bQzMjo']/div[2]/div")
                upcoming_service_month = []
                upcoming_service_day = []
                upcoming_service_name = []

                for i,h in enumerate(upcoming_divs):
                    data = driver.find_elements_by_xpath(f"//div[@class='Box-sc-5gsflb-0 bQzMjo']/div[2]/div[{i+1}]/div/div")
            #         j = i.find_element_by_tag_name('div')
            #         l = j.find_elements_by_tag_name('div')
                    date = data[0].text.strip().split('\n')
                    upcoming_service_month.append(date[0])
                    upcoming_service_day.append(date[1])
                    service_name = driver.find_element_by_xpath(f"//div[@class='Box-sc-5gsflb-0 bQzMjo']/div[2]/div[{i+1}]/div/div[2]/div[3]").text.strip()
                    address_service = driver.find_element_by_xpath(f"//div[@class='Box-sc-5gsflb-0 bQzMjo']/div[2]/div[{i+1}]/div/div[2]/div[4]").text.strip()
                    print(date)
                    upcoming_service_name.append(service_name)
                    print(service_name)
                    print(address_service)
                        
            #         print(j.text)
            #         if 'Plant Memorial Trees' in j[-1]:
            #             upcoming_service_month.append('-')
            #             upcoming_service_day.append('-')
            #             upcoming_service_name.append(j[-1]) 
            #         else:
            #             upcoming_service_month.append(j[0]) 
            #             upcoming_service_day.append(j[1]) 
            #             upcoming_service_name.append(j[2])


            upcoming_service_date = ''
            try:
                for i in range (0, len(upcoming_service_month)):
                    if i == len(upcoming_service_month)-1:
                        upcoming_service_date += f'{upcoming_service_month[i]}-{upcoming_service_day[i]}'
                    else:
                        upcoming_service_date += f'{upcoming_service_month[i]}-{upcoming_service_day[i]}, '

                if len(upcoming_service_name) == 1:
                    upcoming_service_name = upcoming_service_name[0]
                else:
                    upcoming_service_names = upcoming_service_name
                    upcoming_service_name = ''
                    for i in range (0, len(upcoming_service_names)):
                        if i == len(upcoming_service_names)-1:
                            upcoming_service_name += f'{upcoming_service_names[i]}'
                        else:
                            upcoming_service_name += f'{upcoming_service_names[i]}, '

            except:
                upcoming_service_name = ''
                upcoming_service_date = '' 
            keywords = ['Preceded', 'Survived', 'Wife', 'Husband', 'Mother', 'Father', 'Sister', 'Brother', 'civil partner', 'daughter', 'son', 'parents', 'grandparent', 'grandchild', 'parent-in-law', 'son-in-law', 'daughter-in-law', 'sister-in-law', 'brother-in-law', 'stepmother', 'step mother', 'stepfather', 'step father', 'stepchild', 'step child', 'stepsister', 'step sister', 'stepbrother', 'step brother', 'foster child', 'guardian', 'domestic partner', 'fiancé', 'fiancée', 'bride', 'dad', 'mom', 'grandchild','grandchildren', 'granddaughter', 'grandfather','granddad','grandpa', 'grandmother','grandma', 'grandson', 'great-grandparents', 'groom', 'half-brother', 'mother-in-law', 'mum','mummy','nephew', 'niece', 'twin', 'twin-brother', 'siblings']
            lst = []
            # about_doc = self.nlp(paras)
            # sentences = list(about_doc.sents)
            for sentence in para:
                k = sentence.strip().lower()
                try:
                    if date_of_death != '-':

                        if 'passed away' in k:
                            a= k.split('passed away')[-1]
                            match  = datefinder.find_dates(a.strip())
                            if len(list(match)) == 0:
                                a= k.split('passed away')[0]
                                match  = datefinder.find_dates(a.strip())
                                if len(list(match)) == 0:
                                    pass
                                else:
                                    match  = datefinder.find_dates(a.strip())
                                    for j in match:
                                        date_of_death = f"{j.month}/{j.day}/{j.year}"
                                        dod = j.year
                                        print(j)
                                        break
                            else:
                                match  = datefinder.find_dates(a.strip())
                                for j in match:
                                    date_of_death = f"{j.month}/{j.day}/{j.year}"
                                    dod = j.year
                                    print(j)
                                    break
                            
                        elif 'died' in k:
                            a = k.split('died')[-1]
                            match  = datefinder.find_dates(a.strip())
                            if len(list(match)) == 0:
                                a= k.split('died')[0]
                                match  = datefinder.find_dates(a.strip())
                                for j in match:
                                    date_of_death = f"{j.month}/{j.day}/{j.year}"
                                    dod = j.year
                                    print(j)
                                    break
                            else:
                                match  = datefinder.find_dates(a.strip())
                                for j in match:
                                    date_of_death = f"{j.month}/{j.day}/{j.year}"
                                    dod = j.year
                                    print(j)
                                    break
                except:
                    date_of_death = '-'

                        
                for j in range(len(self.keywords)):
                    if f" {self.keywords.loc[j,'Keywords'].strip().lower()}" in k:
                        if k in lst:
                            continue
                        lst.append(f"{sentence.strip()}.\n")
                        break

            # for i in range(len(self.keywords)):
            #     for j in para:
            #         if self.keywords.loc[i,'Keywords'] in j:
            #             if j in lst:
            #                 continue
            #             lst.append(j)
                        
            lonok = ''
            for i in lst:
                lonok += i
                        
            # print(f"Birth Year: {dob} Death Year: {dod} Funeral Home Name: {funeral_home_name} Street: {funeral_home_street} City: {funeral_home_city} State: {funeral_home_state} Zip Code: {funeral_home_zipcode}")
            # print("---------------------------------------------------------")
            # print(lst)
            # print("---------------------------------------------------------")
            # print(upcoming_service_month, upcoming_service_day, upcoming_service_name)
            # print("---------------------------------------------------------")
            # print(f"Full Name: {full_name_with_commas}{full_name_without_commas}")
            # print("---------------------------------------------------------")
            # print(f"Date of death: {date_of_death}") 

            # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': full_name_without_commas, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': full_name_with_commas, 'YEAR OF BIRTH': dob, 'YEAR OF DEATH': dod, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': funeral_home_name,
            #         'Funeral Home Street Address': funeral_home_street, 'Funeral Home City': funeral_home_city, 'Funeral Home State': funeral_home_state, 'Funeral Home ZIP Code': funeral_home_zipcode, 'Upcoming Service Name': upcoming_service_name, 'Upcoming Service Date': upcoming_service_date, 'Upcoming Service City': funeral_home_city, 'List of Next of Kin': lonok, 'Link to the deceased person': url}


            # print(rows)
            # self.df.append(rows,ignore_index=True)
            # self.count += 1
            # for index,key in enumerate(rows):
            #     self.ws.Cells(self.count,index+1).Value = rows[key]
            
                
            # self.ws.Columns.AutoFit()
            # self.ws.Rows.AutoFit()
            data = [self.state,self.city,self.date_from,self.date_to,full_name_without_commas,full_name_with_commas,dob,dod,date_of_death,funeral_home_name,funeral_home_street,funeral_home_city,funeral_home_state,funeral_home_zipcode,upcoming_service_name,upcoming_service_date,funeral_home_city,lonok,driver.current_url]
            return data
            # with open('results.csv','a',newline='') as f:
            #     csv_writer = csv.writer(f)
            #     csv_writer.writerow(data)
            
        except Exception as e:
            error = str(e)
            if 'Url denied'.lower() in error.lower():
                driver.refresh()
                data = self.legacy(driver)
                if data[0] == 'Error':
                    return ["Error",driver.current_url]
                else:
                    return data
            return ["Error",driver.current_url]


            
            # self.close()
            # with open('file.csv','a',newline="") as f:
            #     csv_writer = csv.writer(f)
            #     csv_writer.writerow([url])
            
    def chisolmsfuneral(self,driver):
        try:
            # self.get('https://www.chisolmsfuneral.com/obituary/mrs-sandra-l-albert')
            try:
                data = driver.find_element_by_class_name('subpage').find_element_by_class_name('container').find_element_by_tag_name('div').find_element_by_tag_name('h1').text.split('|')
                name = data[0].split('of')[0]
                city = data[0].split('of')[1].split(',')[0]
            except:
                name = driver.find_element_by_class_name('obit_name').text
                city = '-'
            try:
                date = driver.find_element_by_class_name('lifespan').text.split('-')
                date_of_birth = date[0]
                date_of_death = date[1]
                match  = datefinder.find_dates(date_of_death)
                for j in match:
                    date_of_death = f"{j.month}/{j.day}/{j.year}"
                    year_of_death = j.year
                    print(j)
                    break
                match  = datefinder.find_dates(date_of_birth)
                for j in match:
                    # date_of_birth = f"{j.month}/{j.day}/{j.year}"
                    year_of_birth = j.year
                    print(j)
                    break
            except:
                date_of_birth = '-'
                date_of_death = '-'
                year_of_birth = '-'
                year_of_death = '-'
            lst = []
            try:
                para = driver.find_elements_by_xpath('//div[@class="obit-content"]/p')
                # lst = []
                for i in para:
                    about_doc = i.text.strip().split('.')
                    # sentences = list(about_doc.sents)
                    for sentence in about_doc:
                        k = sentence.strip().lower()
                        for j in range(len(self.keywords)):
                            if f"{self.keywords.loc[j,'Keywords'].strip().lower()}" in k:
                                if k in lst:
                                    continue
                                lst.append(f"{sentence.strip()}.\n")
                                break
            except:
                pass
            funeral_home_name = []
            funeral_home_city = []
            funeral_home_state = []
            funeral_home_street = []
            funeral_home_zipcode = []
            upcoming_service_city = []
            upcoming_service_date = []
            upcoming_service_name = []
            
            try:
                services = driver.find_elements_by_xpath('//fieldset[@id="serviceinfo"]/div/div')
                for i in services:
                    da = i.find_element_by_tag_name('address').text.split('\n')
                    date = i.find_element_by_tag_name('p').text.split('\n')
                    if 'Funeral Service' in i.find_element_by_tag_name('strong').text:
                        funeral_home_name.append(da[0])
                        funeral_home_city.append(da[2].split(',')[0])
                        funeral_home_state.append(da[2].split(',')[1].strip().split(' ')[0])
                        funeral_home_zipcode.append(da[2].split(',')[1].strip().split(' ')[-1])
                        funeral_home_street.append(da[1])
                        print(f"Service Name: {da[0]}")
                        print(f"Serivce date {date[0]}")
                        print(f"Service City{da[2].split(',')[0]}")
                        print(f"Service zip code {da[2].split(',')[1].strip().split(' ')[-1]}")
                    else:
                        upcoming_service_city.append(da[2].split(',')[0])
                        match  = datefinder.find_dates(date[0])
                        for j in match:
                            upcoming_service_name.append(f"{j.month}/{j.day}/{j.year}")
                            # year_of_birth = j.year
                            print(j)
                            break
                        upcoming_service_name.append(da[0])
                        upcoming_service_date.append(date[0])
                        print(f"Service Name: {da[0]}")
                        print(f"Serivce date {date[0]}")
                        print(f"Service City{da[2].split(',')[0]}")
                        print(f"Service zip code {da[2].split(',')[1].strip().split(' ')[-1]}")
                #     print(f"Servi")
            except:
                pass
            data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,funeral_home_name,funeral_home_street,funeral_home_city,funeral_home_state,funeral_home_zipcode,upcoming_service_name,upcoming_service_date,funeral_home_city,'\n'.join(lst),driver.current_url]
            # with open('results.csv','a',newline='') as f:
            #     csv_writer = csv.writer(f)
            #     csv_writer.writerow(data)
            return data
        except Exception as e:
            # print(e)
            error = str(e)
            if 'Url denied'.lower() in error.lower():
                driver.refresh()
                data = self.chisolmsfuneral(driver)
                if data[0] == 'Error':
                    return ["Error",driver.current_url]
                else:
                    return data
            return ["Error",driver.current_url]


    def billdeberry(self,driver):
        try:
            more = driver.find_element_by_xpath("//label[@class='btn btn-small btn-dark']")
            more.click()
            paras = driver.find_elements_by_xpath("//section[@id='obit-text']")
            para = []
            for i in paras:
                para.append(i.text)

            info = driver.find_element_by_xpath("//div[@class='text-container']")
            name = info.find_element_by_xpath("h1").text
            if ',' in name:
                full_name_with_commas = name
                full_name_without_commas = ''
            else:
                full_name_with_commas = ''
                full_name_without_commas = name

            try:  
                dob = info.find_element_by_xpath("h5/span").text.split(',')[1].replace(" ","")
                dod = info.find_element_by_xpath("h5/span[2]").text.split(',')[1]
            except:
                dob = info.find_element_by_xpath("h5").text.split('-')[0]
                dod = info.find_element_by_xpath("h5").text.split('-')[1]
            date_of_death = dod
            
            match  = datefinder.find_dates(dob)
            if len(list(match)) == 0:
                dob = '-'
            else:
                match  = datefinder.find_dates(dob)
                dob = ''
                for i in match:
                    dob += i.year
            match  = datefinder.find_dates(dod)
            if len(list(match)) == 0:
                dod = '-'
            else:
                match  = datefinder.find_dates(dod)
                dod = ''
                for i in match:
                    dod += i.year
            
            match  = datefinder.find_dates(date_of_death)
            if len(list(match)) == 0:
                date_of_death = '-'
            else:
                try:
                    match  = datefinder.find_dates(date_of_death)
                    date_of_death = ''
                    for i in match:
                        date_of_death = f"{i.month}/{i.day}/{i.year}"
                except:
                    pass

            try:
                funeral_home_name = driver.find_element_by_xpath("//section[@class='title']/span").text
                funeral_home_street = driver.find_element_by_xpath("//li[@class='address']").text.split('\n')[0]
                city = driver.find_element_by_xpath("//li[@class='address']").text.split('\n')[1]
                funeral_home_city = city.split(',')[0]
                funeral_home_state = city.split(',')[1].split(' ')[1]
                funeral_home_zipcode = city.split(',')[1].split(' ')[2]
            except:
                funeral_home_name, funeral_home_street, funeral_home_city, funeral_home_state, funeral_home_zipcode = '-', '-', '-', '-', '-'

                
            upcoming_service_date, upcoming_service_name = '-', '-'

            keywords = ['Preceded', 'Survived', 'Wife', 'Husband', 'Mother', 'Father', 'Sister', 'Brother', 'civil partner', 'daughter', 'son', 'parents', 'grandparent', 'grandchild', 'parent-in-law', 'son-in-law', 'daughter-in-law', 'sister-in-law', 'brother-in-law', 'stepmother', 'step mother', 'stepfather', 'step father', 'stepchild', 'step child', 'stepsister', 'step sister', 'stepbrother', 'step brother', 'foster child', 'guardian', 'domestic partner', 'fiancé', 'fiancée', 'bride', 'dad', 'mom', 'grandchild','grandchildren', 'granddaughter', 'grandfather','granddad','grandpa', 'grandmother','grandma', 'grandson', 'great-grandparents', 'groom', 'half-brother', 'mother-in-law', 'mum','mummy','nephew', 'niece', 'twin', 'twin-brother', 'siblings']
            lst = []
            for i in para:
                k = i.strip().lower()
                for j in range(len(self.keywords)):
                    if f" {self.keywords.loc[j,'Keywords'].strip().lower()}" in k:
                        if k in lst:
                            continue
                        lst.append(f"{i.strip()}.\n")
                        break
            # for i in keywords:
            #     for j in para:
            #         if i in j:
            #             if j in lst:
            #                 continue
            #             lst.append(j)
            lonok = ''
            for i in lst:
                lonok += i

                        
            print(f"Birth Year: {dob} Death Year: {dod} Funeral Home Name: {funeral_home_name} Street: {funeral_home_street} City: {funeral_home_city} State: {funeral_home_state} Zip Code: {funeral_home_zipcode}")
            print("---------------------------------------------------------")
            # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': full_name_without_commas, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': full_name_with_commas, 'YEAR OF BIRTH': dob, 'YEAR OF DEATH': dod, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': funeral_home_name,
            #             'Funeral Home Street Address': funeral_home_street, 'Funeral Home City': funeral_home_city, 'Funeral Home State': funeral_home_state, 'Funeral Home ZIP Code': funeral_home_zipcode, 'Upcoming Service Name': upcoming_service_name, 'Upcoming Service Date': upcoming_service_date, 'Upcoming Service City': funeral_home_city, 'List of Next of Kin': lonok, 'Link to the deceased person': url}
            # print(lst)
            # self.df.append(rows,ignore_index=True)
            # self.count += 1
            # for index,key in enumerate(rows):
            #     self.ws.Cells(self.count,index+1).Value = rows[key]
            data = [self.state,self.city,self.date_from,self.date_to,full_name_without_commas,full_name_with_commas,dob,dod,date_of_death,funeral_home_name,funeral_home_street,funeral_home_city,funeral_home_state,funeral_home_zipcode,upcoming_service_name,upcoming_service_date,funeral_home_city,lonok,driver.current_url]
            # with open('results.csv','a',newline='') as f:
            #     csv_writer = csv.writer(f)
            #     csv_writer.writerow(data)
            return data
            # self.ws.Columns.AutoFit()
            # self.ws.Rows.AutoFit()
            # with open('file.csv','a') as f:
            #     csv_writer = csv.writer(f)
            #     csv_writer.writerow([url])
            # print("---------------------------------------------------------")
            # print("---------------------------------------------------------")
            # print(f"Full Name: {full_name_with_commas}{full_name_without_commas}")
            # print("---------------------------------------------------------")
            # print(f"Date of death: {date_of_death}")
        except Exception as e:
            # print(e)
            error = str(e)
            if 'Url denied'.lower() in error.lower():
                driver.refresh()
                data = self.billdeberry(driver)
                if data[0] == 'Error':
                    return ["Error",driver.current_url]
                else:
                    return data
            return ["Error",driver.current_url]
                # self.close()
                # with open('file.csv','a',newline="") as f:
                #     csv_writer = csv.writer(f)
                #     csv_writer.writerow([url])

    def acreswestfuneral(self,driver):
        try:
            try: 
                tex = driver.find_element_by_class_name('obit-name-text')
            except:
                try:
                    tex = driver.find_element_by_class_name('text-container')
                except:
                    tex = driver.find_element_by_class_name('obit-content').find_element_by_tag_name('div')
            name = tex.text.split('\n')[0]
            date = tex.text.split('\n')[1].split('-')
            year_of_birth = date[0].split(',')[1]
            year_of_death = date[1].split(',')[1]
            date_of_birth = date[0]
            date_of_death =date[1]
            match  = datefinder.find_dates(date_of_birth)
            for i in match:
                date_of_birth = f"{i.month}/{i.day}/{i.year}"
            match  = datefinder.find_dates(date_of_death)
            for i in match:
                date_of_death = f"{i.month}/{i.day}/{i.year}" 
            try:
                data = self.find_element_by_class_name('obitBody')
            except:
                try:
                    data = self.find_element_by_class_name('obit-content')
                except:
                    try:
                        self.find_element_by_class_name('read-more').click()
                        data = self.find_element_by_id('obit-text')
                    except:
                        print("not found")
            keywords = ['Preceded', 'Survived', 'Wife', 'Husband', 'Mother', 'Father', 'Sister', 'Brother', 'civil partner', 'daughter', 'son', 'parents', 'grandparent', 'grandchild', 'parent-in-law', 'son-in-law', 'daughter-in-law', 'sister-in-law', 'brother-in-law', 'stepmother', 'step mother', 'stepfather', 'step father', 'stepchild', 'step child', 'stepsister', 'step sister', 'stepbrother', 'step brother', 'foster child', 'guardian', 'domestic partner', 'fiancé', 'fiancée', 'bride', 'dad', 'mom', 'grandchild','grandchildren', 'granddaughter', 'grandfather','granddad','grandpa', 'grandmother','grandma', 'grandson', 'great-grandparents', 'groom', 'half-brother', 'mother-in-law', 'mum','mummy','nephew', 'niece', 'twin', 'twin-brother', 'siblings']
            lst = []
            # for i in range(len(self.keywords)):
            #     for j in para:
            #         if self.keywords.loc[i,'Keywords'] in j:
            #             if j in lst:
            #                 continue
            #             lst.append(j)
            for i in data.text.split('\n'):
                for j in i.split('.'):
                    for il in j:
                        k = il.strip().lower()
                        for b in range(len(self.keywords)):
                            if f" {self.keywords.loc[b,'Keywords'].strip().lower()}" in k:
                                if k in lst:
                                    continue
                                lst.append(f"{il.strip()}.\n")
                                
                                break
                    # for k in range(len(self.keywords)):
                    #     h = self.keywords.loc[k,'Keywords']
                    #     if h in j.strip():
                    #         if j.strip() in lst:
                    #             continue
                    #         lst.append(j.strip())
                    #         print(j.strip())
            try:
                services = driver.find_elements_by_xpath("//section[@class='obit-services']/div/div/div[2]/div/div")
                if len(services) == 0:
                    try:
                        services = driver.find_elements_by_class_name('service')
                        service_name = []
                        service_date= []
                        service_city = []
                        for i in services:
                            if i.text.strip()=="":
                                continue
                            d = i.text.split('\n')
                            service_name.append(d[1])
                            match  = datefinder.find_dates(d[2])
                            for l in match:
                                service_date.append(f"{l.month}/{l.day}/{l.year}")
                            # service_date.append(d[2])
                            service_city.append(f"{d[5],d[6]}")
                            print(f"Service name = {d[1]}")
                            print(f"Service date = {d[2]}")
                            print(f"Service City = {d[5]},{d[6]}")
                            print(i.text.split('\n'))
            #             print(service.text.strip())
                    except:
                        service_city.append('-')
                        service_date.append('-')
                        service_name.append('-')
                        print('not found')
            except:
                print('not found')
                try:
                    services = driver.find_elements_by_class_name('service')
                    service_name = []
                    service_date= []
                    service_city = []
                    for i in services:
                        if i.text.strip()=="":
                            continue
                        d = i.text.split('\n')
                        service_name.append(d[1])
                        match  = datefinder.find_dates(d[2])
                        for l in match:
                            service_date.append(f"{l.month}/{l.day}/{l.year}")
                        # service_date.append(d[2])
                        service_city.append(f"{d[5],d[6]}")
                        print(f"Service name = {d[1]}")
                        print(f"Service date = {d[2]}")
                        print(f"Service City = {d[5]},{d[6]}")
                        print(i.text.split('\n'))
            #         print(service.text.strip())
                except:
                    service_city.append('-')
                    service_date.append('-')
                    service_name.append('-')
                    print('not found')
            # servicess = []
            
                
                # servicess.append(i.text.strip())
            # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
            #             'Funeral Home Street Address': '-', 'Funeral Home City': '-', 'Funeral Home State': '-', 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '\n'.join(service_name), 'Upcoming Service Date': '\n'.join(service_date), 'Upcoming Service City': '\n'.join(service_city), 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
            # self.df.append(rows,ignore_index=True)
            data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,'-','-','-','-','-','\n'.join(service_name),'\n'.join(service_date),'\n'.join(service_city),'\n'.join(lst),driver.current_url]
            return data
            # with open('results.csv','a',newline='') as f:
            #     csv_writer = csv.writer(f)
            #     csv_writer.writerow(data)
        except Exception as e:
            # print(e)
            error = str(e)
            if 'Url denied'.lower() in error.lower():
                driver.refresh()
                data = self.acreswestfuneral(driver)
                if data[0] == 'Error':
                    return ["Error",driver.current_url]
                else:
                    return data
            return ["Error",driver.current_url]


    def downsfuneralhome(self,driver):
        try:
            data = driver.find_elements_by_xpath('//div[@id="bodyContent"]/div/div/div/div')
            if len(data) == 0:
                data = driver.find_element_by_xpath('//div[@class="common-layout"]/div/div/div/h1')
                city = data.text.split('|')[0].split('of')[1].split(',')[0].strip()
                state = data.text.split('|')[0].split('of')[1].split(',')[1].strip()
            else:

                try:    
                    city = data[0].text.split('|')[0].split('of')[1].split(',')[0].strip()
                    state = data[0].text.split('|')[0].split('of')[1].split(',')[1].strip()
                    if city == '':
                        city = '-'
                    if state == '':
                        state= '-'
                except:
                    city = '-'
                    state = '-'
            ass = driver.find_element_by_xpath('//div[@class="obit-content"]/div').text.split('\n')
            name = ass[0]
            date = ass[1]
            date.split('-')
            date_of_birth = date.split('-')[0]
            date_of_death = date.split('-')[1]
            year_of_birth = date_of_birth.split(',')[1]
            year_of_death = date_of_death.split(',')[1]
            match  = datefinder.find_dates(date_of_birth)
            for l in match:
                date_of_birth = f"{l.month}/{l.day}/{l.year}"
            match  = datefinder.find_dates(date_of_death)
            for l in match:
                date_of_death = f"{l.month}/{l.day}/{l.year}"
            
            content = driver.find_elements_by_xpath('//div[@class="obit-content"]/p')
            lst = []
            for i in content:
                if i.text.strip() == '':
                    continue
                for j in i.text.strip().split('.'):
                    
                    k = j.strip().lower()
                    for l in range(len(self.keywords)):
                        if f" {self.keywords.loc[l,'Keywords'].strip().lower()}" in k:
                            if k in lst:
                                continue
                            lst.append(f"{j.strip()}.\n")
                            
                            break  
            services = driver.find_elements_by_xpath("//fieldset[@id='serviceinfo']/div/div")
            servicess = []
            service_name = []
            service_city = []
            service_date = []
            for i in services:
                da = i.text.strip().split('\n')
                service_name.append(da[0])
                match  = datefinder.find_dates(da[1])
                for l in match:
                    service_date.append(f"{l.month}/{l.day}/{l.year}")
                # service_date.append(da[1])
                print(f"Serivce Name = {da[0]}")
                print(f"Service date= {da[1]}")
                if da[5] == 'Get Directions on Google Maps':
                    service_city.append(f"{da[3]},{da[4]}")
                    print(f"Service City= {da[3]},{da[4]}")
                else:
                    service_city.append(f"{da[4]},{da[5]}")
                    print(f"Service City= {da[4]},{da[5]}")
                print(da)
            # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
            #             'Funeral Home Street Address': '-', 'Funeral Home City': city, 'Funeral Home State': state, 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '\n'.join(service_name), 'Upcoming Service Date': '\n'.join(service_date), 'Upcoming Service City': '\n'.join(service_city), 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
            # self.df.append(rows,ignore_index=True)
            data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,'-','-',city,state,'-','\n'.join(service_name),'\n'.join(service_date),'\n'.join(service_city),'\n'.join(lst),driver.current_url]
            return data
            # with open('results.csv','a',newline='') as f:
            #     csv_writer = csv.writer(f)
            #     csv_writer.writerow(data)
#     servicess.append(i.text.strip())     
        except Exception as e:
            # print(e)
            error = str(e)
            if 'Url denied'.lower() in error.lower():
                driver.refresh()
                data = self.downsfuneralhome(driver)
                if data[0] == 'Error':
                    return ["Error",driver.current_url]
                else:
                    return data
            return ["Error",driver.current_url]

    def owensbrumley(self,driver):
        try:
            a = driver.find_element_by_class_name('text-container').text.split('\n')
            name = a[0]
            date = a[1].split('-')
            date_of_birth = date[0]
            date_of_death = date[1]
            year_of_birth = date_of_birth.split(',')[1]
            year_of_death = date_of_death.split(',')[1]
            match  = datefinder.find_dates(date_of_birth)
            for l in match:
                date_of_birth = f"{l.month}/{l.day}/{l.year}"
            match  = datefinder.find_dates(date_of_death)
            for l in match:
                date_of_death = f"{l.month}/{l.day}/{l.year}"
            
            try:
                time.sleep(2)
                driver.find_element_by_class_name('read-more').click()
            except:
                print('not found')
            data = driver.find_element_by_id('obit-text').text.strip().split('\n')
            lst = []
            for i in data:
                da = i.split('.')
                for d in da:
                    k = d.strip().lower()
                    for j in range(len(self.keywords)):
                        if f" {self.keywords.loc[j,'Keywords'].strip().lower()}" in k:
                            if k in lst:
                                continue
                            lst.append(f"{d.strip()}.\n")
                            
                            break

                
            service_name = []
            service_city = []
            service_date = []
            
            try:
                service = driver.find_elements_by_class_name('service')
                if len(service) == 0:
                    service_name.append('-')
                    service_city.append('-')
                    service_date.append('-')
                    
                else:
                    for i in service:
                        title = i.find_element_by_tag_name('section').find_element_by_tag_name('span').text.strip()
                        # if 'Funeral Services' in title:
                        #     funeral_home_name
                        #     print('funeral')
                        data = i.find_element_by_tag_name('ul').find_elements_by_tag_name('li')
                        date = data[0].text.strip()
                        match  = datefinder.find_dates(date)
                        for l in match:
                            date = f"{l.month}/{l.day}/{l.year}"
                        city = data[-1].text.strip().replace('\n',", ")
                        # da = i.text.split('\n')
                        service_name.append(title)
                        service_city.append(city)
                        service_date.append(date)
                        # print(i.text.split('\n'))
                    # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
                    #         'Funeral Home Street Address': '-', 'Funeral Home City': '-', 'Funeral Home State': '-', 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '\n'.join(service_name), 'Upcoming Service Date': '\n'.join(service_date), 'Upcoming Service City': '\n'.join(service_city), 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
                    # self.df.append(rows,ignore_index=True)
                try:
                    funeral_service=driver.find_element_by_class_name('callback')
                    funeral_home_name = funeral_service.text.strip().split('\n')[0]
                    funeral_home_street =  funeral_service.text.strip().split('\n')[1]
                    funeral_home_city =  funeral_service.text.strip().split('\n')[2].split(',')[0]
                    funeral_home_state =  funeral_service.text.strip().split('\n')[2].split(',')[1].strip().split(' ')[0]
                    funeral_home_zipcode = funeral_service.text.strip().split('\n')[2].split(',')[1].strip().split(' ')[1]
                    
                    data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,funeral_home_name,funeral_home_street,funeral_home_city,funeral_home_state,funeral_home_zipcode,'\n'.join(service_name),'\n'.join(service_date),'\n'.join(service_city),'\n'.join(lst),driver.current_url]
                    # with open('results.csv','a',newline='') as f:
                    #     csv_writer = csv.writer(f)
                    #     csv_writer.writerow(data)
                    return data
                except:
                    data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,'-','-','-','-','-','\n'.join(service_name),'\n'.join(service_date),'\n'.join(service_city),'\n'.join(lst),driver.current_url]
                    # with open('results.csv','a',newline='') as f:
                    #     csv_writer = csv.writer(f)
                    #     csv_writer.writerow(data)
                    return data
            except:
                service_name.append('-')
                service_city.append('-')
                service_date.append('-')
                # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
                #         'Funeral Home Street Address': '-', 'Funeral Home City': '-', 'Funeral Home State': '-', 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '\n'.join(service_name), 'Upcoming Service Date': '\n'.join(service_date), 'Upcoming Service City': '\n'.join(service_city), 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
                # self.df.append(rows,ignore_index=True)
                data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,'-','-','-','-','-','\n'.join(service_name),'\n'.join(service_date),'\n'.join(service_city),'\n'.join(lst),driver.current_url]
                # with open('results.csv','a',newline='') as f:
                #     csv_writer = csv.writer(f)
                #     csv_writer.writerow(data)
                return data
                # print('not found')
        except Exception as e:
            # print('not found')
            error = str(e)
            if 'Url denied'.lower() in error.lower():
                driver.refresh()
                data = self.owensbrumley(driver)
                if data[0] == 'Error':
                    return ["Error",driver.current_url]
                else:
                    return data
            return ["Error",driver.current_url]


    def theangelusfuneralhome(self, driver):
        try:
            a = driver.find_element_by_class_name('text-container').text.split('\n')
            name = a[0]
            date = a[1]
            # date_of_birth = date[0]
            date_of_death = date
            # year_of_birth = date_of_birth.split(',')[1]
            year_of_death = date_of_death.split(',')[1]
            # match  = datefinder.find_dates(date_of_birth)
            # for l in match:
            #     date_of_birth = f"{l.month}/{l.day}/{l.year}"
            match  = datefinder.find_dates(date_of_death)
            for l in match:
                date_of_death = f"{l.month}/{l.day}/{l.year}"
            
            try:
                driver.find_element_by_class_name('read-more').click()
            except:
                print('not found')
            data = driver.find_element_by_id('obit-text').text.strip().split('\n')
            lst = []
            for i in data:
                da = i.split('.')
                for d in da:
                    k = d.strip().lower()
                    for j in range(len(self.keywords)):
                        if f" {self.keywords.loc[j,'Keywords'].strip().lower()}" in k:
                            if k in lst:
                                continue
                            lst.append(f"{d.strip()}.\n")
                            
                            break

                
            service_name = []
            service_city = []
            service_date = []
            
            try:
                service = driver.find_elements_by_class_name('service')
                for i in service:
                    title = i.find_element_by_tag_name('section').find_element_by_tag_name('span').text.strip()
                    # if 'Funeral Services' in title:
                    #     funeral_home_name
                    #     print('funeral')
                    data = i.find_element_by_tag_name('ul').find_elements_by_tag_name('li')
                    date = data[0].text.strip()
                    match  = datefinder.find_dates(date)
                    for l in match:
                        date = f"{l.month}/{l.day}/{l.year}"
                    city = data[-1].text.strip().replace('\n',", ")
                    # da = i.text.split('\n')
                    service_name.append(title)
                    service_city.append(city)
                    service_date.append(date)
                    # print(i.text.split('\n'))
                # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
                #         'Funeral Home Street Address': '-', 'Funeral Home City': '-', 'Funeral Home State': '-', 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '\n'.join(service_name), 'Upcoming Service Date': '\n'.join(service_date), 'Upcoming Service City': '\n'.join(service_city), 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
                # self.df.append(rows,ignore_index=True)
                data = [self.state,self.city,self.date_from,self.date_to,name,'-','-',year_of_death,date_of_death,'-','-','-','-','-','\n'.join(service_name),'\n'.join(service_date),'\n'.join(service_city),'\n'.join(lst),driver.current_url]
                # with open('results.csv','a',newline='') as f:
                #     csv_writer = csv.writer(f)
                #     csv_writer.writerow(data)
                return data
            except:
                service_name.append('-')
                service_city.append('-')
                service_date.append('-')
                # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
                #         'Funeral Home Street Address': '-', 'Funeral Home City': '-', 'Funeral Home State': '-', 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '\n'.join(service_name), 'Upcoming Service Date': '\n'.join(service_date), 'Upcoming Service City': '\n'.join(service_city), 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
                # self.df.append(rows,ignore_index=True)
                data = [self.state,self.city,self.date_from,self.date_to,name,'-','-',year_of_death,date_of_death,'-','-','-','-','-','\n'.join(service_name),'\n'.join(service_date),'\n'.join(service_city),'\n'.join(lst),driver.current_url]
                # with open('results.csv','a',newline='') as f:
                #     csv_writer = csv.writer(f)
                #     csv_writer.writerow(data)

                return data
                # print('not found')
        except Exception as e:
            # print('not found')
            error = str(e)
            if 'Url denied'.lower() in error.lower():
                driver.refresh()
                data = self.theangelusfuneralhome(driver)
                if data[0] == 'Error':
                    return ["Error",driver.current_url]
                else:
                    return data
            return ["Error",driver.current_url]


    def smartcremation(self, driver):
        try:
            name = driver.find_element_by_xpath("//div[@class='name-info']/div").text
            date = driver.find_element_by_xpath("//div[@class='name-info']/ul/li[1]").text
            date_of_birth = date.split('-')[0]
            date_of_death = date.split('-')[1]
            year_of_birth = date_of_birth.split(',')[1]
            year_of_death = date_of_death.split(',')[1]
            match  = datefinder.find_dates(date_of_birth)
            for l in match:
                date_of_birth = f"{l.month}/{l.day}/{l.year}"
            match  = datefinder.find_dates(date_of_death)
            for l in match:
                date_of_death = f"{l.month}/{l.day}/{l.year}"
            
            address = driver.find_element_by_xpath("//div[@class='name-info']/ul/li[2]").text
            city = address.split(',')[0]
            state = address.split(',')[1]
            lst = []
            for i in driver.find_elements_by_xpath("//div[@id='obit_text_page_1']/p"):
                if i.text == '.' or i.text == '':
                    break
                da = i.text.split('.')
                for d in da:
                    k = d.strip().lower()
                    for j in range(len(self.keywords)):
                        if f" {self.keywords.loc[j,'Keywords'].strip().lower()}" in k:
                            if k in lst:
                                continue
                            lst.append(f"{d.strip()}.\n")
                            
                            break
            funeral_home_name, funeral_home_street, funeral_home_city, funeral_home_state, funeral_home_zipcode = '-', '-', '-', '-', '-'
            upcoming_service_name,upcoming_service_date,upcoming_service_city = '-','-','-'
            
            # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': full_name_without_commas, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': full_name_with_commas, 'YEAR OF BIRTH': dob, 'YEAR OF DEATH': dod, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': funeral_home_name,
            #         'Funeral Home Street Address': funeral_home_street, 'Funeral Home City': funeral_home_city, 'Funeral Home State': funeral_home_state, 'Funeral Home ZIP Code': funeral_home_zipcode, 'Upcoming Service Name': upcoming_service_name, 'Upcoming Service Date': upcoming_service_date, 'Upcoming Service City': funeral_home_city, 'List of Next of Kin': lonok, 'Link to the deceased person': url}
            try:
                services = driver.find_element_by_id('obit_tabs')
                services.find_element_by_link_text('Funeral Services').click()
                if 'Click here to be notified when a service is added' in driver.find_element_by_id('services').text:
                    print('no services')
                    data = [self.state,self.city,self.date_from,self.date_from,name,'-',year_of_birth,year_of_death,date_of_death,'-','-',city,state,'-','-','-','-','\n'.join(lst),url]
                else:
                    service = driver.find_elements_by_xpath('//div[@id="services"]/div')
                    if len(service) == 0:
                        pass
                    else:
                        funeral_home_name, funeral_home_street, funeral_home_city, funeral_home_state, funeral_home_zipcode = [], [], [], [], []
                        upcoming_service_name,upcoming_service_date,upcoming_service_city = [],[],[]
                        for i in service:
                            a = i.find_element_by_tag_name('p').text.strip().split('\n')
                            print()
                            
                            if 'funeral service' in i.find_element_by_tag_name('h5').text.lower() :
                                funeral_home_name.append(a[3].strip())
                                funeral_home_street.append(a[4])
                                funeral_home_city.append(a[5].strip().split(',')[0])
                                funeral_home_state.append(a[5].strip().split(',')[1].strip().split(' ')[0])
                                funeral_home_zipcode.append(a[5].strip().split(',')[1].strip().split(' ')[1])
                                # print(f'service name {a[3].strip()}')
                                # print(f'service day {a[0].strip()}')
                                # print(f"service street address {a[4]}")
                                # print(f"Service state {a[5].strip().split(',')[1].strip().split(' ')[0]}")
                                # print(f"Service city {a[5].strip().split(',')[0]}")
                                # print(f"Service zip code {a[5].strip().split(',')[1].strip().split(' ')[1]}")
                        #         print("hamza")
                            else:
                                upcoming_service_city.append(a[5].strip().split(',')[0])
                                upcoming_service_name.append(a[3].strip())
                                match  = datefinder.find_dates(a[0].strip())
                                for l in match:
                                    upcoming_service_date.append(f"{l.month}/{l.day}/{l.year}")
                                # print(f'service name {a[3].strip()}')
                                # print(f'service day {a[0].strip()}')
                                # print(f"Service city {a[5].strip().split(',')[0]}")
                    #         print(f"service address {a[4]},{a[5]}")
                        data = [self.state,self.city,self.date_from,self.date_from,name,'-',year_of_birth,year_of_death,date_of_death,'\n'.join(funeral_home_name),'\n'.join(funeral_home_street),'\n'.join(funeral_home_city),'\n'.join(funeral_home_state),'\n'.join(funeral_home_zipcode),'\n'.join(upcoming_service_name),'\n'.join(upcoming_service_date),'\n'.join(upcoming_service_city),'\n'.join(lst),driver.current_url]
                    # service = self.find_element_by_id('services').text.strip()
            except:
                data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,'-','-',city,state,'-','-','-','-','\n'.join(lst),driver.current_url]
               
            return data
        except Exception as e:
            # print('not foound')
            error = str(e)
            if 'Url denied'.lower() in error.lower():
                driver.refresh()
                data = self.smartcremation(driver)
                if data[0] == 'Error':
                    return ["Error",driver.current_url]
                else:
                    return data
            return ["Error",driver.current_url]


    def eastgate(self,driver):
        try:
            data = driver.find_element_by_class_name('name-info').text.strip().split('\n')
            name = data[0]
            date = data[1].split('-')
            date_of_birth = date[0]
            date_of_death = date[1]
            year_of_birth = date_of_birth.split(',')[1]
            year_of_death = date_of_death.split(',')[1]
            match  = datefinder.find_dates(date_of_birth)
            for l in match:
                date_of_birth = f"{l.month}/{l.day}/{l.year}"
            match  = datefinder.find_dates(date_of_death)
            for l in match:
                date_of_death = f"{l.month}/{l.day}/{l.year}"
            
            adress = data[2].split(',')
            city = adress[0]
            state = adress[1]
            lst = []
            for i in driver.find_element_by_class_name('obit-text-container').text.strip().split('\n'):
                for j in i.split('.'):
                    
                    k = j.strip().lower()
                    for a in range(len(self.keywords)):
                        if f" {self.keywords.loc[a,'Keywords'].strip().lower()}" in k:
                            if k in lst:
                                continue
                            lst.append(f"{j.strip()}.\n")
                            
                            break
            try:
                funeralservices = driver.find_elements_by_xpath('//div[@id="services-glider"]/div/div/div')
                if len(funeralservices) == 0:
                    data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,'-','-',city,state,'-','-','-','-','\n'.join(lst),driver.current_url]
                    
                    return data
                    # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
                    #         'Funeral Home Street Address': '-', 'Funeral Home City': city, 'Funeral Home State': state, 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '-', 'Upcoming Service Date': '-', 'Upcoming Service City': '-', 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
                    # self.df.append(rows,ignore_index=True)
                else:
                    services_name = []
                    services_city = []
                    services_date = []
                    for i in funeralservices:
                        ass =i.text.strip().split('\n')
                        services_name.append(ass[0])
                        match  = datefinder.find_dates(ass[1])
                        for l in match:
                            services_date.append(f"{l.month}/{l.day}/{l.year}")
                        # services_date.append(ass[1])
                        services_city.append(f"{ass[6]}")
                    # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
                    #         'Funeral Home Street Address': '-', 'Funeral Home City': city, 'Funeral Home State': state, 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '\n'.join(services_name), 'Upcoming Service Date': '\n'.join(services_date), 'Upcoming Service City': '\n'.join(services_city), 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
                    # self.df.append(rows,ignore_index=True)
                    data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,'-','-',city,state,'-','\n'.join(services_name),'\n'.join(services_date),'\n'.join(services_city),'\n'.join(lst),driver.current_url]
                    
                    return data
            except:
                # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
                #             'Funeral Home Street Address': '-', 'Funeral Home City': city, 'Funeral Home State': state, 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '-', 'Upcoming Service Date': '-', 'Upcoming Service City': '-', 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
                # self.df.append(rows,ignore_index=True) 
                data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,'-','-',city,state,'-','-','-','-','\n'.join(lst),driver.current_url]
                
                return data
        except Exception as e:
            error = str(e)
            if 'Url denied'.lower() in error.lower():
                driver.refresh()
                data = self.eastgate(driver)
                if data[0] == 'Error':
                    return ["Error",driver.current_url]
                else:
                    return data
            return ["Error",driver.current_url]
        
    def trinityfunerals(self, driver):
        try:

            try:
                tex = driver.find_element_by_xpath('//div[@class="common-layout"]/div/div[1]')
            except:
                try:
                    tex = driver.find_element_by_xpath('//div[@class="subpage"]/div/div[1]')
                except:
                    tex = driver.find_element_by_xpath('//div[@id="bodyContent"]/div/div/div/div[1]')
            ass = tex.text.split('|')
            name = driver.find_element_by_class_name('obit_name')
            try:
                address = ass[0].split('of')[1].strip()
                city = address.split(',')[0]
                state = address.split(',')[1]
            except:
                city = '-'
                state = '-'
                print("not city")
            date = driver.find_element_by_class_name('lifespan')
            date_of_birth = date.text.split('-')[0]
            date_of_death = date.text.split('-')[1]
            year_of_birth = date_of_birth.split(',')[1]
            year_of_death = date_of_death.split(',')[1]
            match  = datefinder.find_dates(date_of_birth)
            for l in match:
                date_of_birth = f"{l.month}/{l.day}/{l.year}"
            match  = datefinder.find_dates(date_of_death)
            for l in match:
                date_of_death = f"{l.month}/{l.day}/{l.year}"
            
            data = driver.find_elements_by_xpath('//div[@class="obit-content"]/p')
            lst = []
            for i in data:
                k = i.text.split('.')
                for a in k:
                    kl= a.strip().lower()
                    for j in range(len(self.keywords)):
                        if f" {self.keywords.loc[j,'Keywords'].strip().lower()}" in kl:
                            if kl in lst:
                                continue
                            lst.append(f"{a.strip()}.\n")
                            
                            break
            services = driver.find_elements_by_xpath('//fieldset[@id="serviceinfo"]/div')
            if len(services) == 0:
                # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
                #             'Funeral Home Street Address': '-', 'Funeral Home City': city, 'Funeral Home State': state, 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '-', 'Upcoming Service Date': '-', 'Upcoming Service City': '-', 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
                # self.df.append(rows,ignore_index=True)
                data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,'-','-',city,state,'-','-','-','-','\n'.join(lst),driver.current_url]
                # with open('results.csv','a',newline='') as f:
                #     csv_writer = csv.writer(f)
                #     csv_writer.writerow(data)
                return data
                # pass
            else:
                services_name = []
                services_date = []
                services_city = []
                for i in services:
                    a = i.find_elements_by_tag_name('div')
                    for j in a:
                        ass = j.text.split('\n')
                        services_name.append(ass[0])
                        # services_date.append(ass[1])
                        match  = datefinder.find_dates(ass[1])
                        for l in match:
                            services_date.append(f"{l.month}/{l.day}/{l.year}")
                        services_city.append(f"{ass[4]},{ass[5]}")
                # rows = {'State': self.state, 'City': self.city, 'Range of Dates from:': self.date_from, 'Range of Dates to:': self.date_to, 'FULL NAME OF THE DECEASED PERSON WITHOUT COMMAS': name, 'FULL NAME OF THE DECEASED PERSON WITH COMMAS': '-', 'YEAR OF BIRTH': year_of_birth, 'YEAR OF DEATH': year_of_death, 'DATE OF DEATH': date_of_death, 'Funeral Home Name': '-',
                #             'Funeral Home Street Address': '-', 'Funeral Home City': city, 'Funeral Home State': state, 'Funeral Home ZIP Code': '-', 'Upcoming Service Name': '\n'.join(services_name), 'Upcoming Service Date': '\n'.join(services_date), 'Upcoming Service City': '\n'.join(services_city), 'List of Next of Kin': '\n'.join(lst), 'Link to the deceased person': url}
                # self.df.append(rows,ignore_index=True)
                data = [self.state,self.city,self.date_from,self.date_to,name,'-',year_of_birth,year_of_death,date_of_death,'-','-',city,state,'-','\n'.join(services_name),'\n'.join(services_date),'\n'.join(services_city),'\n'.join(lst),driver.current_url]
                
                return data
        except Exception as e:
            error = str(e)
            if 'Url denied'.lower() in error.lower():
                driver.refresh()
                data = self.trinityfunerals(driver)
                if data[0] == 'Error':
                    return ["Error",driver.current_url]
                else:
                    return data
            return ["Error",driver.current_url]






    def read_result(self, url):
        # url = self.result[key]
        driver = webdriver.Chrome(desired_capabilities=self.capabilities)
        driver.implicitly_wait(30)
        
        try:
            # self.get(url)
            driver.get(url)
            
            if "legacy" in driver.current_url or 'dallas' in driver.current_url or 'obits.dallasnews.com' in driver.current_url or 'obits.oklahoman.com' in driver.current_url or 'obits.nola.com' in driver.current_url:
                data = self.legacy(driver)
                

            elif 'chisolmsfuneral.com' in driver.current_url:
                data = self.chisolmsfuneral(driver)


            elif 'billdeberry.com' in driver.current_url or 'duncanmortuary.com' in driver.current_url:
                data = self.billdeberry(driver)
            elif 'acreswestfuneral.com' in driver.current_url or 'kleinfh.com' in driver.current_url or 'colemansmortuaryjasper.com' in driver.current_url:
                data = self.acreswestfuneral(driver)
            elif 'downsfuneralhome.com' in driver.current_url or 'lovefuneralhome.net' in driver.current_url or 'whitesfuneral.com' in driver.current_url:
                data = self.downsfuneralhome(driver)
            elif 'heavenlygatefuneralservices.com' in driver.current_url or 'owensbrumley.com' in driver.current_url or 'proctorsmortuary.com' in driver.current_url or 'texarkanafuneralhome.com' in driver.current_url or 'parker-ashworthfuneralhome.com' in driver.current_url or 'sneedfuneralchapel.com' in driver.current_url or 'hurleyfuneralhome.com' in driver.current_url or 'hillcrestfuneralhomelittlefield.com' in driver.current_url or 'internationalfuneralhomes.com' in driver.current_url or 'hughesfunerals.com' in driver.current_url or 'canonfuneralhome.com' in driver.current_url or 'parker-ashworthfuneralhome.com' in driver.current_url or 'cokerfuneralhome.com' in driver.current_url or 'sneedfuneralchapel.com' in driver.current_url or 'owensbrumley.com' in driver.current_url or 'billdeberry.com' in self.current_url or 'bastropprovidencefuneralhome.com' in driver.current_url or 'comeauxchapel.com' in driver.current_url or 'internationalfuneralhomes.com' in driver.current_url or'acreswestfuneral.com' in driver.current_url or 'wisefuneralhome.com' in driver.current_url:
                data = self.owensbrumley(driver)

            elif 'theangelusfuneralhome.com' in driver.current_url:
                
                data = self.theangelusfuneralhome(driver)



            elif 'smartcremation.tributes.com' in driver.current_url or 'charleswsmith-mckinney.tributes.com' in driver.current_url:
                data = self.smartcremation(driver)


            elif 'smithfamilyfuneralhomes.tributes.com' in driver.current_url or 'eastgate-garland.tributes.com' in driver.current_url or 'charleswsmith-sachse.tributes.com' in driver.current_url:

                data = self.eastgate(driver)


            elif 'trinityfunerals.com' in driver.current_url or 'brownfuneraldirector.com' in driver.current_url or 'doeppenschmidtfuneralhome.com' in driver.current_url or 'smithfamilyfh.com' in driver.current_url:
                data = self.trinityfunerals(driver)



            
        except Exception as e:  
            print(e)
            print('Url denied')
            return ["Error",driver.current_url]
            driver.close()

        driver.close()
        return data
        # self.back()

    def runscrapper(self):

        for key in self.result:
            print(
            f"----------------- Extracting Data about {key} -----------------")
            print('')
            data = self.read_result(self.result[key])
            if data[0]=="Error":
                with open('error.csv','a',newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([data[1]])
            else:
                with open('results.csv','a',newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(data)
        # self.wb.Close(True) # save the workbook
        # self.df.to_excel('results.xlsx')
    
    def checkerror(self):
        error = pd.read_csv('error.csv')
        for j in range(len(error)):
            url = error.loc[j,'URL']
            data = self.read_result(url)
            if data[0]=="Error":
                with open('error.csv','a',newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([data[1]])
            else:
                with open('results.csv','a',newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(data)
            

        
        