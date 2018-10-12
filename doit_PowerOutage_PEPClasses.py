"""

"""
from PowerOutages_V2.doit_PowerOutage_ProviderClasses import Provider
from PowerOutages_V2.doit_PowerOutage_PEPDEL_ParentClass import PEPDELParent
from PowerOutages_V2.doit_PowerOutage_UtilityClass import Utility as doit_util
from PowerOutages_V2.doit_PowerOutage_ProviderClasses import Outage


class PEP(Provider, PEPDELParent):
    def __init__(self, provider_abbrev):
        super(PEP, self).__init__(provider_abbrev=provider_abbrev)
