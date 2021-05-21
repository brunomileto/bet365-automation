from utils import wait

class Matches():
    MATCH_TYPE = 'Futebol'
    CLASSES = {
        'matches': 'ips-EventRow_HasPreMatchLink.ips-EventRow.ips-EventRow_SportsFilter',
        'dropdown-click' : 'ips-InPlayNavHeader_ClassificationLabel',
        'dropdown'       : 'ips-ClassificationDropDownContainer_Inner',
        'dropdown-item'  : 'ips-DropDownItem_Label'
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


