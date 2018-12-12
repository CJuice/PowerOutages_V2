"""
The Archive module contains an ArchiveCounty class and a PowerOutagesViewForArchiveCountyData dataclass.
The classes are built for the archive functionality in the power outage process. The County real time data requires
manipulation before being written to the archive tables, unlike the ZIP code real time data.
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
import PowerOutages_V2.doit_PowerOutage_CentralizedVariables as VARS


class ArchiveCounty:
    """
    Object for storing and processing data from real time form to archive form.

    The methods are used to get data from a view, create data class objects of that data, and then insert into the
    county archive table.
    """
    def __init__(self):
        self.county_archive_record_objects_list = None
        self.sql_insert_record_county_archive = VARS.sql_insert_record_county_archive

    def build_list_of_archive_data_record_objects(self, selection):
        """
        Use the data class to create objects for each record in the selection.
        :param selection: records from query
        :return: none, data objects stored in county_archive_record_objects_list
        """
        record_list = []
        for record in selection:
            record_obj = PowerOutagesViewForArchiveCountyData(*record)
            record_list.append(record_obj)
        self.county_archive_record_objects_list = record_list
        return

    def generate_county_archive_insert_sql_statement(self):
        """
        Generator for building and yielding sql statement for insertion of county record object data into archive
        :return: none
        """
        for record_obj in self.county_archive_record_objects_list:
            record_obj.county = record_obj.county.replace("'", "''")  # Prepping county name values for re-entry into DB
            sql = self.sql_insert_record_county_archive.format(
                state=record_obj.state,
                county=record_obj.county,
                outage=record_obj.outage,
                updated=record_obj.updated,
                archived=record_obj.updated,
                percentage=round(record_obj.percentage, 3))
            yield sql


class ArchiveZIP:
    def __init__(self):
        self.master_aggregated_zip_count_objects_dict = {}
        self.sql_insert_record_zip_archive = VARS.sql_insert_record_zip_archive

    def generate_insert_sql_statement_archive(self):
        """
        Build the insert sql statement for archive data and yield the statement.
        For ZIP archive data.
        :return: none
        """
        for aggregated_count_obj in self.master_aggregated_zip_count_objects_dict.values():
            sql = self.sql_insert_record_zip_archive.format(area=aggregated_count_obj.area,
                                                            abbrev=aggregated_count_obj.abbrev,
                                                            outages=aggregated_count_obj.outages,
                                                            date_created=aggregated_count_obj.date_created,
                                                            date_updated=aggregated_count_obj.date_updated
                                                            )
            yield sql


@dataclass
class ZipCodeCountAggregated:
    area: str
    abbrev: str
    outages: int
    date_created: datetime
    date_updated: datetime


@dataclass
class PowerOutagesViewForArchiveCountyData:
    """
    Data class for storing record data pulled from view.
    """
    state: str
    county: str
    outage: int
    updated: datetime
    percentage: Decimal
