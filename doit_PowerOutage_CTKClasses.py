"""

"""
from PowerOutages_V2.doit_PowerOutage_ProviderClasses import Provider
from PowerOutages_V2.doit_PowerOutage_UtilityClass import Utility as doit_util
from PowerOutages_V2.doit_PowerOutage_ProviderClasses import Outage


class CTK(Provider):

    def __init__(self, provider_abbrev):
        super().__init__(provider_abbrev=provider_abbrev)
        self.xml_dom = None
        self.xml_metadata_element = None

