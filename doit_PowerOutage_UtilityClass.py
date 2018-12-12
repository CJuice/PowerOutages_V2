"""

"""
from datetime import datetime
import configparser
import xml.etree.ElementTree as ET
import json


class Utility:
    """Common/shared static methods and constants for use by all involved Power Outage Project entities.

    The methods in this class are used by many of the provider classes for processing feed responses and outage data.
    """

    COUNTY = "County"
    DELAWARE = "Delaware"
    DISTRICT_OF_COLUMBIA = "District Of Columbia"
    LESS_THAN_FIVE = "Less than 5"
    MARYLAND = "Maryland"
    MARYLAND_COUNTIES = ("Allegany", "Anne Arundel", "Baltimore", "Baltimore City", "Calvert", "Caroline", "Carroll",
                         "Cecil", "Charles", "Dorchester", "Frederick", "Garrett", "Harford", "Howard", "Kent",
                         "Montgomery", "Prince George's", "Queen Anne's", "St. Mary's", "Somerset", "Talbot",
                         "Washington", "Wicomico", "Worcester")
    PARSER = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    ZERO_TIME_STRING = "00:00:00 00:00:00"
    ZIP = "ZIP"

    @staticmethod
    def build_feed_uri(metadata_key: str, data_feed_uri: str) -> str:
        """Build a uri for provider data feed, inserting key into string template

        :param metadata_key: string code given by provider for insertion into data feed uri
        :param data_feed_uri: string uri for accessing the provider data feed
        :return: string uri
        """
        return data_feed_uri.format(metadata_key=metadata_key)

    @staticmethod
    def current_date_time() -> str:
        """
        Create a string representation of the current date and time.
        :return: string representation of date and time
        """
        return "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())

    @staticmethod
    def exchange_state_abbrev_for_full_value(abbrev: str) -> str:
        """
        Get a value from a state abbreviations dictionary using the provided abbreviation.

        :param abbrev: string abbreviation for the state
        :return: string value from state_abbrev_dict for given abbrev, or the abbrev itself if KeyError
        """
        state_abbrev_dict = {"DC": Utility.DISTRICT_OF_COLUMBIA, "DE": Utility.DELAWARE, "MD": Utility.MARYLAND, }
        try:
            return state_abbrev_dict[abbrev]
        except KeyError as ke:
            return abbrev

    @staticmethod
    def extract_all_immediate_child_features_from_element(element: ET.Element, tag_name: str) -> list:
        """
        Extract all immediate children of the element provided to the method.

        :param element: ET.Element of interest to be interrogated
        :param tag_name: tag of interest on which to search
        :return: list of all discovered ET.Element items
        """
        try:
            return element.findall(tag_name)
        except AttributeError as ae:
            print(f"AttributeError: Unable to extract '{tag_name}' from {element.text}: {ae}")
            exit()

    @staticmethod
    def extract_attribute_from_dict(data_dict: dict, attribute_name: str):
        """Extract and return a value from the provided dictionary based on the given key

        :param data_dict: dictionary to interrogate
        :param attribute_name: sought after dictionary key
        :return: value of whatever type the dictionary contains
        """
        try:
            return data_dict[attribute_name]
        except KeyError as ke:
            print(f"KeyError: Unable to extract '{attribute_name}' from {data_dict}: {ke}")
            exit()

    @staticmethod
    def extract_attribute_value_from_xml_element_by_index(root_element: ET.Element, index_position: int = 0) -> str:
        """Extract value of index position defined attribute from xml ET.Element.
        
        :param root_element: element to interrogate
        :param index_position: position of desired value
        :return: string value
        """
        return root_element[index_position].text

    @staticmethod
    def extract_first_immediate_child_feature_from_element(element: ET.Element, tag_name: str) -> ET.Element:
        """Extract first immediate child feature from provided xml ET.Element based on provided tag name

        :param element: xml ET.Element to interrogate
        :param tag_name: name of desired tag
        :return: ET.Element of interest
        """

        try:
            return element.find(tag_name)
        except AttributeError as ae:
            print(f"AttributeError: Unable to extract '{tag_name}' from {element.text}: {ae}")
            exit()

    @staticmethod
    def get_config_variable(parser: configparser.ConfigParser, section: str, variable_name: str) -> str:
        """
        Get the variable of interest from a config file using the provided parser
        :param parser: config parser for use on .cfg file
        :param section: section of interest in the cfg file
        :param variable_name: name of the variable of interest
        :return: string variable value
        """
        try:
            return parser[section][variable_name]
        except KeyError as ke:
            print(f"Section or Variable not found: {section} - {variable_name}")
            exit()
        except Exception as e:  # TODO: Improve exception handling
            print(e)
            exit()

    @staticmethod
    def parse_xml_response_to_element(response_xml_str: str) -> ET.Element:
        """
        Process xml response content to xml ET.Element
        :param response_xml_str: string xml from response
        :return: xml ET.Element
        """
        try:
            return ET.fromstring(response_xml_str)
        except Exception as e:  # TODO: Improve exception handling
            print(f"Unable to process xml response to Element using ET.fromstring(): {e}")
            exit()

    # TODO: process_customer_counts_to_integers & process_outage_counts_to_integers are basically identical. Refactor.
    @staticmethod
    def process_customer_counts_to_integers(objects_list: list):
        """
        Process objects customer count attribute value to integer
        :param objects_list: list of stat objects
        :return: none, revises value of attribute
        """
        replacement_values_dict = {Utility.LESS_THAN_FIVE: 1, "<5": 1}
        for obj in objects_list:
            try:
                obj.customers = int(obj.customers)
            except ValueError as ve:
                try:
                    obj.customers = replacement_values_dict[obj.customers]
                except KeyError as ke:
                    obj.customers = -9999
        return

    @staticmethod
    def process_outage_counts_to_integers(objects_list: list):
        """
        Process objects outage count attribute value to integer
        :param objects_list: list of stat objects
        :return: none, revises value of attribute
        """
        replacement_values_dict = {Utility.LESS_THAN_FIVE: 1, "<5": 1}
        for obj in objects_list:
            try:
                obj.outages = int(obj.outages)
            except ValueError as ve:
                try:
                    obj.outages = replacement_values_dict[obj.outages]
                except KeyError as ke:
                    obj.outages = -9999
        return

    @staticmethod
    def remove_commas_from_counts(objects_list: list):
        """
        Remove commas from string version of number values in objects
        :param objects_list:  list of objects to operate on
        :return: none, revises in place
        """
        for obj in objects_list:
            try:
                obj.outages = obj.outages.replace(",", "")
            except AttributeError as ae:
                # doesn't have .replace method. likely type int
                pass
            try:
                obj.customers = obj.customers.replace(",", "")
            except AttributeError as ae:
                # doesn't have .replace method. likely type int
                pass
        return

    @staticmethod
    def revise_county_name_spellings_and_punctuation(stats_objects_list: list):
        """
        Revise county name spellings and punctuation for attributes in stat objects.
        :param stats_objects_list: list of stat objects
        :return: none, revise in place
        """
        corrections_dict = {"Prince Georges": "Prince George's",
                            "St Marys": "St. Mary's",
                            "St Mary's": "St. Mary's",
                            "St. Marys": "St. Mary's",
                            "Queen Annes": "Queen Anne's",
                            "Kent (MD)": "Kent"}
        for obj in stats_objects_list:
            if obj.area.isupper():
                obj.area = obj.area.title()
            else:
                pass
            try:
                obj.area = corrections_dict[obj.area]
            except KeyError as ke:

                # No correction needed per the dict of items as seen above
                continue
        return

    @staticmethod
    def write_to_file(file: str, content):
        """
        Use context manager to write the content to the provided rile in json format
        :param file: file to which content will be written
        :param content: content to be written to file
        :return:
        """
        with open(file, 'w') as file_handler:
            file_handler.write(json.dumps(content))
        return

    # @staticmethod
    # def change_case_to_title(stats_objects: list):
    #     # Removed use. Causes case errors in apostrophe containing county names. St. Mary's -> St. Mary'S
    #     for obj in stats_objects:
    #         obj.area = obj.area.title()
