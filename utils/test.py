
from utils.configparserUtil import ConfigUtils

def alam():
    cu = ConfigUtils("testdata")
    cu.set_section_key_value('PLMPage', "ecn_number", "123123")
    print(ConfigUtils("testdata").get_values_by_key('PLMPage', "ecn_number"))

alam()