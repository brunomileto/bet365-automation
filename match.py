from utils import wait

class Match():
    MATCH_TYPE = 'Futebol'
    CLASSES = {
        'match-navbar': 'sph-HorizontalNavBarScroller_Contents',
        'match-navbar-itens': 'sph-MarketGroupNavBarButton',
        'match-name': 'ips-EventRow_EventName',
        'minute-title': 'gl-MarketGroupButton_Text', 
        'table-title': 'srb-ParticipantLabel_Name',
        'table-bet': 'srb-ParticipantCenteredStackedMarketRow.gl-Participant_General.gl-Market_General-cn1.srb-ParticipantCenteredStackedMarketRow-hashandicap.srb-ParticipantCenteredStackedMarketRow-wide',
    }

    def __init__(self, web_driver):
        self.driver = web_driver
        self.matches = None
        
    def select_match_type(self):
        wait()
        self.driver.find_element_by_class_name(self.CLASSES['dropdown-click'])
        wait()
        dropdown = self.driver.find_emlement_by_class_name(self.CLASSES['dropdown'])
        dropdown_itens = dropdown.find_elements_by_class_name(self.CLASSES['dropdown-item'])
        for item in dropdown_itens:
            if item.text == self.MATCH_TYPE:
                item.click()
                wait()
                break
    
    def select_matches(self):
        self.matches = self.driver.find_elements_by_class_name(self.CLASSES['matches'])


