import sys
import undetected_chromedriver.v2 as uc
import time

if len(sys.argv) <= 1:

    print("Please, inform your login: ")
    login = input()
    print("Please, inform your password: ")
    password = input()
else:

    login = sys.argv[1]
    password = sys.argv[2]

classes = {
    'login-btn' : {
        'login-link': 'hm-MainHeaderRHSLoggedOutWide_LoginContainer',
        'username': 'lms-StandardLogin_Username',
        'password': 'lms-StandardLogin_Password',
        'login'   : 'lms-StandardLogin_LoginButtonText', 
    },
    'sports-dropdown': {
        'dropdown-click' : 'ips-InPlayNavHeader_ClassificationLabel',
        'dropdown'       : 'ips-ClassificationDropDownContainer_Inner',
        'dropdown-item'  : 'ips-DropDownItem_Label'
    },
    'matches': 'ips-EventRow_HasPreMatchLink.ips-EventRow.ips-EventRow_SportsFilter',
    'match-navbar': 'sph-HorizontalNavBarScroller_Contents',
    'match-navbar-itens': 'sph-MarketGroupNavBarButton',
    'match-name': 'ips-EventRow_EventName',
    'minute-title': 'gl-MarketGroupButton_Text', 
    'table-title': 'srb-ParticipantLabel_Name',
    'table-bet': 'srb-ParticipantCenteredStackedMarketRow.gl-Participant_General.gl-Market_General-cn1.srb-ParticipantCenteredStackedMarketRow-hashandicap.srb-ParticipantCenteredStackedMarketRow-wide',
    'bet-place': 'qbs-StakeBox_StakeAmount',
    'bet-amount': 'qbs-StakeBox_StakeValue.qbs-StakeBox_StakeValue-input',
    'place-bet' : 'qbs-PlaceBetButton_Wrapper',
}

xpaths = {
    'bet-table':{
        'table-titles': '/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[1]/div/div/div[2]/div/div[3]/div[2]/div/div[1]',
        'table-bets': '/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[1]/div/div/div[2]/div/div[3]/div[2]/div/div[2]',
    }
}

matches_checked = []
def login(driver):
    time.sleep(5)
    driver.find_element_by_class_name(classes['login-btn']['login-link']).click()
    time.sleep(5)
    driver.find_element_by_class_name(classes['login-btn']['username']).send_keys(login)
    time.sleep(5)
    driver.find_element_by_class_name(classes['login-btn']['password']).send_keys(password)
    time.sleep(5)
    driver.find_element_by_class_name(classes['login-btn']['login']).click()
    time.sleep(5)

def select_soccer_type(driver):
    time.sleep(5)
    driver.find_element_by_class_name(classes['sports-dropdown']['dropdown-click']).click()
    time.sleep(5)
    dropdown = driver.find_element_by_class_name(classes['sports-dropdown']['dropdown'])
    dropdown_itens = dropdown.find_elements_by_class_name(classes['sports-dropdown']['dropdown-item'])
    for item in dropdown_itens:
        if item.text == 'Futebol':
            item.click()
            time.sleep(5)
            break


def select_matches(driver):
    return driver.find_elements_by_class_name(classes['matches'])



def check_minutes_market_exist(driver, match):
    match_navbar = driver.find_elements_by_class_name(classes['match-navbar-itens'])
    for item in match_navbar:
        if item.text == 'Minutos':
            item.click()
            time.sleep(5)
            return True


def check_corner_market_exist(driver):
    market_group = driver.find_elements_by_class_name('gl-MarketGroup')
    for market in market_group:
        market_title = market.find_element_by_class_name('gl-MarketGroupButton_Text').text
        if 'Primeiros 10 Minutos' in market_title:
            return True  


def select_corner_bet(driver):
    corner_market = market


def go_to_match(driver, matches):
    for match in matches:
        matches_checked.append(match.find_element_by_class_name('ips-EventRow_EventName').text)
        match.click()
        if check_minutes_market_exist(driver, match):
            if check_corner_market_exist(driver):
                






url = 'https://www.bet365.com/#/IP/SCHEDULE'


driver = uc.Chrome()
with driver:
    driver.get(url)
    login(driver)
    driver.get(url)
    select_soccer_type(driver)
    matches = select_matches(driver)
    for match in matches:
        matches_checked.append(match.find_element_by_class_name('ips-EventRow_EventName').text)
        match.click()
        match_navbar = driver.find_elements_by_class_name(classes['match-navbar-itens'])
        for item in match_navbar:
            if item.text == 'Minutos':
                item.click()
                time.sleep(5)
                market_group = driver.find_elements_by_class_name('gl-MarketGroup')
                for market in market_group:
                    market_title = market.find_element_by_class_name('gl-MarketGroupButton_Text').text
                    if 'Primeiros 10 Minutos' in market_title:
                        corner_market = market
                        titles = corner_market.find_elements_by_class_name(classes['table-title'])
                        for i in range(len(titles)):
                            if titles[i].text == 'Escanteios':
                                corner_index = i
                                bets = corner_market.find_elements_by_class_name(classes['table-bet'])
                                bets[corner_index].click()
                                bet_place = driver.find_element_by_class_name(classes['bet-place'])
                                bet_place.click()
                                bet_amount = driver.find_element_by_class_name(classes['bet-amount'])
                                driver.find_element_by_class_name(classes['place-bet']).click()
                        
                    else:
                        driver.get(url)
                        select_soccer_type(driver)
            else:
                driver.get(url)
                select_soccer_type(driver)

            


