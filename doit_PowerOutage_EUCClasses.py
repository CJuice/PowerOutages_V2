"""

"""
from PowerOutages_V2.doit_PowerOutage_ProviderClasses import Provider
from PowerOutages_V2.doit_PowerOutage_UtilityClass import Utility as doit_util
from PowerOutages_V2.doit_PowerOutage_ProviderClasses import Outage
import json


class EUC(Provider):
    def __init__(self, provider_abbrev, style):
        super().__init__(provider_abbrev=provider_abbrev, style=style)
        self.xml_element = None
        self.events_list = None
        self.stats_objects = None

    def extract_outage_events_list_from_xml_str(self, content_list_as_str):
        self.events_list = json.loads(content_list_as_str)
        return

    def extract_outage_counts(self):
        list_of_stats_objects = []
        for event in self.events_list:
            outages = doit_util.extract_attribute_from_dict(data_dict=event, attribute_name="Count")
            customers = doit_util.extract_attribute_from_dict(data_dict=event, attribute_name="AccountCount")
            area = doit_util.extract_attribute_from_dict(data_dict=event, attribute_name="ZipCode")
            list_of_stats_objects.append(Outage(abbrev=self.abbrev,
                                                style=self.style,
                                                area=area,
                                                outages=outages,
                                                customers=customers,
                                                state="MD")
                                         )
        self.stats_objects = list_of_stats_objects
        return

    def extract_date_created(self):
        for event in self.events_list:
            self.date_created = doit_util.extract_attribute_from_dict(data_dict=event, attribute_name="TimeStamp")
        return