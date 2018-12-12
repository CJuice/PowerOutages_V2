"""
Module containing variables and no functionality. Mostly serves as repository for sql variables that are very long and
exceed the PEP line length guideline, and other values that may need to be edited in the future. The intent is to make
editing easier for non-developers by having a single location for the variables so that they do not need to search
through and interact with the code. This avoids introduction of errors and also makes life easier for those who do not
enjoy mucking about in the code.
"""
import textwrap

credentials_cfg_file = "doit_PowerOutage_Credentials.cfg"
database_connection_string = "DSN={database_name};UID={database_user};PWD={database_password}"
database_flag = -9999
json_file_local_location_and_name = "JSON_Outputs\PowerOutageFeeds_StatusJSON.json"
less_than_five = "Less than 5"
maryland_master_inventory_zip_codes_with_geometry = {'0': 'Assateague Island', '20601': 'Waldorf', '20602': 'Waldorf',
                                                     '20603': 'Waldorf', '20606': 'Abell', '20607': 'Accokeek',
                                                     '20608': 'Aquasco', '20609': 'Avenue', '20611': 'Bel Alton',
                                                     '20612': 'Benedict', '20613': 'Brandywine',
                                                     '20615': 'Broomes Island',
                                                     '20616': 'Bryans Road', '20617': 'Bryantown', '20618': 'Bushwood',
                                                     '20619': 'California', '20620': 'Callaway', '20621': 'Chaptico',
                                                     '20622': 'Charlotte Hall', '20623': 'Cheltenham',
                                                     '20624': 'Clements',
                                                     '20625': 'Cobb Island', '20626': 'Coltons Point',
                                                     '20628': 'Dameron',
                                                     '20629': 'Dowell', '20630': 'Drayden', '20632': 'Faulkner',
                                                     '20634': 'Great Mills', '20636': 'Hollywood',
                                                     '20637': 'Hughesville',
                                                     '20639': 'Huntingtown', '20640': 'Indian Head', '20645': 'Issue',
                                                     '20646': 'La Plata', '20650': 'Leonardtown',
                                                     '20653': 'Lexington Park',
                                                     '20656': 'Loveville', '20657': 'Lusby', '20658': 'Marbury',
                                                     '20659': 'Mechanicsville', '20662': 'Nanjemoy', '20664': 'Newburg',
                                                     '20667': 'Park Hall', '20670': 'Patuxent River',
                                                     '20674': 'Piney Point',
                                                     '20675': 'Pomfret', '20676': 'Port Republic',
                                                     '20677': 'Port Tobacco',
                                                     '20678': 'Prince Frederick', '20680': 'Ridge',
                                                     '20684': 'Saint Inigoes',
                                                     '20685': 'Saint Leonard', '20687': 'Scotland', '20688': 'Solomons',
                                                     '20689': 'Sunderland', '20690': 'Tall Timbers',
                                                     '20692': 'Valley Lee',
                                                     '20693': 'Welcome', '20695': 'White Plains',
                                                     '20701': 'Annapolis Junction',
                                                     '20705': 'Beltsville', '20706': 'Lanham', '20707': 'Laurel',
                                                     '20708': 'Laurel', '20710': 'Bladensburg', '20711': 'Lothian',
                                                     '20712': 'Mount Rainier', '20714': 'North Beach', '20715': 'Bowie',
                                                     '20716': 'Bowie', '20720': 'Bowie', '20721': 'Bowie',
                                                     '20722': 'Brentwood',
                                                     '20723': 'Laurel', '20724': 'Laurel', '20732': 'Chesapeake Beach',
                                                     '20733': 'Churchton', '20735': 'Clinton', '20736': 'Owings',
                                                     '20737': 'Riverdale', '20740': 'College Park',
                                                     '20742': 'College Park',
                                                     '20743': 'Capitol Heights', '20744': 'Fort Washington',
                                                     '20745': 'Oxon Hill',
                                                     '20746': 'Suitland', '20747': 'District Heights',
                                                     '20748': 'Temple Hills',
                                                     '20751': 'Deale', '20754': 'Dunkirk',
                                                     '20755': 'Fort George G Meade',
                                                     '20758': 'Friendship', '20759': 'Fulton',
                                                     '20762': 'Andrews Air Force Base',
                                                     '20763': 'Savage', '20764': 'Shady Side', '20765': 'Galesville',
                                                     '20769': 'Glenn Dale', '20770': 'Greenbelt', '20771': 'Greenbelt',
                                                     '20772': 'Upper Marlboro', '20774': 'Upper Marlboro',
                                                     '20776': 'Harwood',
                                                     '20777': 'Highland', '20778': 'West River',
                                                     '20779': 'Tracys Landing',
                                                     '20781': 'Hyattsville', '20782': 'Hyattsville',
                                                     '20783': 'Hyattsville',
                                                     '20784': 'Hyattsville', '20785': 'Hyattsville', '20794': 'Jessup',
                                                     '20812': 'Glen Echo', '20814': 'Bethesda', '20815': 'Chevy Chase',
                                                     '20816': 'Bethesda', '20817': 'Bethesda', '20818': 'Cabin John',
                                                     '20832': 'Olney', '20833': 'Brookeville', '20837': 'Poolesville',
                                                     '20838': 'Barnesville', '20839': 'Beallsville', '20841': 'Boyds',
                                                     '20842': 'Dickerson', '20850': 'Rockville', '20851': 'Rockville',
                                                     '20852': 'Rockville', '20853': 'Rockville', '20854': 'Potomac',
                                                     '20855': 'Derwood', '20860': 'Sandy Spring', '20861': 'Ashton',
                                                     '20862': 'Brinklow', '20866': 'Burtonsville',
                                                     '20868': 'Spencerville',
                                                     '20871': 'Clarksburg', '20872': 'Damascus', '20874': 'Germantown',
                                                     '20876': 'Germantown', '20877': 'Gaithersburg',
                                                     '20878': 'Gaithersburg',
                                                     '20879': 'Gaithersburg', '20882': 'Gaithersburg',
                                                     '20886': 'Montgomery Village', '20889': 'Bethesda',
                                                     '20892': 'Bethesda',
                                                     '20894': 'Bethesda', '20895': 'Kensington',
                                                     '20899': 'Gaithersburg',
                                                     '20901': 'Silver Spring', '20902': 'Silver Spring',
                                                     '20903': 'Silver Spring',
                                                     '20904': 'Silver Spring', '20905': 'Silver Spring',
                                                     '20906': 'Silver Spring',
                                                     '20910': 'Silver Spring', '20912': 'Takoma Park',
                                                     '21001': 'Aberdeen',
                                                     '21005': 'Aberdeen Proving Ground', '21009': 'Abingdon',
                                                     '21010': 'Gunpowder', '21012': 'Arnold', '21013': 'Baldwin',
                                                     '21014': 'Bel Air', '21015': 'Bel Air', '21017': 'Belcamp',
                                                     '21028': 'Churchville', '21029': 'Clarksville',
                                                     '21030': 'Cockeysville',
                                                     '21031': 'Hunt Valley', '21032': 'Crownsville',
                                                     '21034': 'Darlington',
                                                     '21035': 'Davidsonville', '21036': 'Dayton', '21037': 'Edgewater',
                                                     '21040': 'Edgewood', '21042': 'Ellicott City',
                                                     '21043': 'Ellicott City',
                                                     '21044': 'Columbia', '21045': 'Columbia', '21046': 'Columbia',
                                                     '21047': 'Fallston', '21048': 'Finksburg', '21050': 'Forest Hill',
                                                     '21051': 'Fork', '21053': 'Freeland', '21054': 'Gambrills',
                                                     '21056': 'Gibson Island', '21057': 'Glen Arm',
                                                     '21060': 'Glen Burnie',
                                                     '21061': 'Glen Burnie', '21071': 'Glyndon', '21074': 'Hampstead',
                                                     '21075': 'Elkridge', '21076': 'Hanover', '21077': 'Harmans',
                                                     '21078': 'Havre De Grace', '21082': 'Hydes',
                                                     '21084': 'Jarrettsville',
                                                     '21085': 'Joppa', '21087': 'Kingsville',
                                                     '21090': 'Linthicum Heights',
                                                     '21093': 'Lutherville Timonium', '21102': 'Manchester',
                                                     '21104': 'Marriottsville', '21108': 'Millersville',
                                                     '21111': 'Monkton',
                                                     '21113': 'Odenton', '21114': 'Crofton', '21117': 'Owings Mills',
                                                     '21120': 'Parkton', '21122': 'Pasadena', '21128': 'Perry Hall',
                                                     '21131': 'Phoenix', '21132': 'Pylesville', '21133': 'Randallstown',
                                                     '21136': 'Reisterstown', '21140': 'Riva', '21144': 'Severn',
                                                     '21146': 'Severna Park', '21152': 'Sparks Glencoe',
                                                     '21153': 'Stevenson',
                                                     '21154': 'Street', '21155': 'Upperco', '21156': 'Upper Falls',
                                                     '21157': 'Westminster', '21158': 'Westminster',
                                                     '21160': 'Whiteford',
                                                     '21161': 'White Hall', '21162': 'White Marsh',
                                                     '21163': 'Woodstock',
                                                     '21201': 'Baltimore', '21202': 'Baltimore', '21204': 'Towson',
                                                     '21205': 'Baltimore', '21206': 'Raspeburg', '21207': 'Gwynn Oak',
                                                     '21208': 'Pikesville', '21209': 'Mt Washington',
                                                     '21210': 'Roland Park',
                                                     '21211': 'Baltimore', '21212': 'Govans', '21213': 'Clifton',
                                                     '21214': 'Baltimore', '21215': 'Arlington', '21216': 'Baltimore',
                                                     '21217': 'Druid', '21218': 'Baltimore', '21219': 'Sparrows Point',
                                                     '21220': 'Middle River', '21221': 'Essex', '21222': 'Dundalk',
                                                     '21223': 'Franklin', '21224': 'Highlandtown', '21225': 'Brooklyn',
                                                     '21226': 'Curtis Bay', '21227': 'Halethorpe',
                                                     '21228': 'Catonsville',
                                                     '21229': 'Carroll', '21230': 'Morrell Park', '21231': 'Baltimore',
                                                     '21234': 'Parkville', '21235': 'Baltimore', '21236': 'Nottingham',
                                                     '21237': 'Rosedale', '21239': 'Northwood', '21240': 'BWI Airport',
                                                     '21241': 'Baltimore', '21244': 'Windsor Mill',
                                                     '21250': 'Baltimore',
                                                     '21251': 'Baltimore', '21252': 'Baltimore', '21286': 'Towson',
                                                     '21287': 'Baltimore', '21401': 'Annapolis',
                                                     '21402': 'Naval Academy',
                                                     '21403': 'Eastport', '21405': 'Sherwood Forest',
                                                     '21409': 'Annapolis',
                                                     '21502': 'Cumberland', '21520': 'Accident', '21521': 'Barton',
                                                     '21522': 'Bittinger', '21523': 'Bloomington',
                                                     '21530': 'Flintstone',
                                                     '21531': 'Friendsville', '21532': 'Frostburg',
                                                     '21536': 'Grantsville',
                                                     '21538': 'Kitzmiller', '21539': 'Lonaconing', '21540': 'Luke',
                                                     '21541': 'McHenry', '21545': 'Mount Savage', '21550': 'Oakland',
                                                     '21555': 'Oldtown', '21557': 'Rawlings', '21561': 'Swanton',
                                                     '21562': 'Westernport', '21601': 'Easton', '21607': 'Barclay',
                                                     '21610': 'Betterton', '21612': 'Bozman', '21613': 'Cambridge',
                                                     '21617': 'Centreville', '21619': 'Chester', '21620': 'Chestertown',
                                                     '21622': 'Church Creek', '21623': 'Church Hill',
                                                     '21625': 'Cordova',
                                                     '21626': 'Crapo', '21627': 'Crocheron', '21629': 'Denton',
                                                     '21631': 'East New Market', '21632': 'Federalsburg',
                                                     '21634': 'Fishing Creek', '21635': 'Galena', '21636': 'Goldsboro',
                                                     '21638': 'Grasonville', '21639': 'Greensboro',
                                                     '21640': 'Henderson',
                                                     '21643': 'Hurlock', '21644': 'Ingleside', '21645': 'Kennedyville',
                                                     '21647': 'McDaniel', '21648': 'Madison', '21649': 'Marydel',
                                                     '21650': 'Massey', '21651': 'Millington', '21652': 'Neavitt',
                                                     '21654': 'Oxford', '21655': 'Preston', '21657': 'Queen Anne',
                                                     '21658': 'Queenstown', '21659': 'Rhodesdale', '21660': 'Ridgely',
                                                     '21661': 'Rock Hall', '21662': 'Royal Oak',
                                                     '21663': 'Saint Michaels',
                                                     '21665': 'Sherwood', '21666': 'Stevensville',
                                                     '21667': 'Still Pond',
                                                     '21668': 'Sudlersville', '21669': 'Taylors Island',
                                                     '21671': 'Tilghman',
                                                     '21672': 'Toddville', '21673': 'Trappe', '21675': 'Wingate',
                                                     '21676': 'Wittman', '21677': 'Woolford', '21678': 'Worton',
                                                     '21679': 'Wye Mills', '21701': 'Frederick', '21702': 'Frederick',
                                                     '21703': 'Frederick', '21704': 'Frederick', '21710': 'Adamstown',
                                                     '21711': 'Big Pool', '21713': 'Boonsboro', '21716': 'Brunswick',
                                                     '21718': 'Burkittsville', '21719': 'Cascade',
                                                     '21722': 'Clear Spring',
                                                     '21723': 'Cooksville', '21727': 'Emmitsburg', '21733': 'Fairplay',
                                                     '21737': 'Glenelg', '21738': 'Glenwood', '21740': 'Hagerstown',
                                                     '21742': 'Hagerstown', '21750': 'Hancock', '21754': 'Ijamsville',
                                                     '21755': 'Jefferson', '21756': 'Keedysville', '21757': 'Keymar',
                                                     '21758': 'Knoxville', '21766': 'Little Orleans',
                                                     '21767': 'Maugansville',
                                                     '21769': 'Middletown', '21770': 'Monrovia', '21771': 'Mount Airy',
                                                     '21773': 'Myersville', '21774': 'New Market',
                                                     '21776': 'New Windsor',
                                                     '21777': 'Point of Rocks', '21778': 'Rocky Ridge',
                                                     '21779': 'Rohrersville',
                                                     '21780': 'Sabillasville', '21782': 'Sharpsburg',
                                                     '21783': 'Smithsburg',
                                                     '21784': 'Sykesville', '21787': 'Taneytown', '21788': 'Thurmont',
                                                     '21790': 'Tuscarora', '21791': 'Union Bridge',
                                                     '21793': 'Walkersville',
                                                     '21794': 'West Friendship', '21795': 'Williamsport',
                                                     '21797': 'Woodbine',
                                                     '21798': 'Woodsboro', '21801': 'Salisbury', '21804': 'Salisbury',
                                                     '21811': 'Berlin', '21813': 'Bishopville', '21814': 'Bivalve',
                                                     '21817': 'Crisfield', '21821': 'Deal Island', '21822': 'Eden',
                                                     '21824': 'Ewell', '21826': 'Fruitland', '21829': 'Girdletree',
                                                     '21830': 'Hebron', '21835': 'Linkwood', '21837': 'Mardela Springs',
                                                     '21838': 'Marion Station', '21840': 'Nanticoke', '21841': 'Newark',
                                                     '21842': 'Ocean City', '21849': 'Parsonsburg',
                                                     '21850': 'Pittsville',
                                                     '21851': 'Pocomoke City', '21853': 'Princess Anne',
                                                     '21856': 'Quantico',
                                                     '21862': 'Showell', '21863': 'Snow Hill', '21864': 'Stockton',
                                                     '21865': 'Tyaskin', '21869': 'Vienna', '21871': 'Westover',
                                                     '21872': 'Whaleyville', '21874': 'Willards', '21875': 'Delmar',
                                                     '21890': 'Westover', '21901': 'North East', '21903': 'Perryville',
                                                     '21904': 'Port Deposit', '21911': 'Rising Sun', '21912': 'Warwick',
                                                     '21915': 'Chesapeake City', '21917': 'Colora',
                                                     '21918': 'Conowingo',
                                                     '21919': 'Earleville', '21921': 'Elkton'}
multi_zip_code_value_delimiter = ","
multiple_providers = "MULTI"
provider_uri_cfg_file = "doit_PowerOutage_ProviderURI.cfg"
sme_customer_count_database_location_and_name = "SME_Customer_Count_Memory_DB\SME_Customer_Count_Memory_DB.db"
sme_database_table_name = "SME_Customer_Count_Memory"
sql_create_county_table_sme_sqlite3 = textwrap.dedent(
    """CREATE TABLE {table_name} (
        County_ID integer primary key autoincrement, 
        County_Name text, 
        Customer_Count integer, 
        Last_Updated text
    )"""
)
sql_delete_statement = textwrap.dedent(
    """DELETE FROM RealTime_PowerOutages{style} 
    WHERE PROVIDER = '{provider_abbrev}'"""
)
sql_insert_into_county_table_sme_sqlite3 = textwrap.dedent(
    """INSERT INTO {table_name} VALUES (
        Null,
        '{county_name}', 
        {cust_count}, 
        '{date_updated}'
    )"""
)
sql_insert_record_county_archive = textwrap.dedent(
    """INSERT INTO Archive_PowerOutagesCounty(
            STATE, 
            COUNTY, 
            Outage, 
            updated, 
            archived, 
            percentage
        ) 
        VALUES (
            '{state}',
            '{county}',
            {outage},
            '{updated}',
            '{archived}',
            '{percentage}'
        )"""
)
sql_insert_record_county_realtime = textwrap.dedent(
    """INSERT INTO dbo.RealTime_PowerOutagesCounty(
            STATE, 
            COUNTY, 
            OUTAGE, 
            PROVIDER, 
            UPDATED, 
            CREATED
        ) 
        VALUES (
            '{state}',
            '{county}',
            {outages},
            '{abbrev}',
            '{date_updated}',
            '{date_created}'
        )"""
)
sql_insert_record_zip_archive = textwrap.dedent(
    """INSERT INTO dbo.Archive_PowerOutagesZipcode(
            ZIPCODE,
            ID, 
            PROVIDER, 
            OUTAGE, 
            CREATED, 
            UPDATED, 
            ARCHIVED
        ) 
        VALUES (
            '{area}',
            'NULL',
            '{abbrev}',
            {outages},
            '{date_created}',
            '{date_updated}',
            '{date_updated}'
        )"""
)
sql_insert_record_zip_realtime = textwrap.dedent(
    """INSERT INTO dbo.RealTime_PowerOutagesZipcodes(
            ZIPCODE, 
            PROVIDER, 
            OUTAGE, 
            CREATED, 
            UPDATED
        ) 
        VALUES (
            '{area}',
            '{abbrev}',
            {outages},
            '{date_created}',
            '{date_updated}'
        )"""
)
sql_select_by_provider_abbrev_realtime = textwrap.dedent(
    """SELECT {fields} FROM dbo.RealTime_PowerOutages{style}
    WHERE PROVIDER = '{provider_abbrev}'"""
)
sql_select_counties_viewforarchive = textwrap.dedent(
    """SELECT state, county, outage, updated, percentage 
    FROM OSPREYDB_DEV.dbo.PowerOutages_PowerOutagesViewForArchive 
    WHERE state is not Null"""
)
sql_select_county_data_sme_sqlite3 = textwrap.dedent(
    """SELECT County_ID, County_Name, Customer_Count 
    FROM SME_Customer_Count_Memory"""
)
sql_select_zip_by_provider_abbrev_realtime = textwrap.dedent(
    """SELECT zipcode FROM dbo.RealTime_PowerOutagesZipcodes 
    WHERE PROVIDER = '{provider_abbrev}'"""
)
sql_update_customer_counts_table = textwrap.dedent(
    """UPDATE dbo.RealTime_PowerOutagesCounty_Customers 
    SET Customers = {cust_count} 
    WHERE County = '{area}'"""
)
sql_update_customers_table_sme_sqlite3 = textwrap.dedent(
    """UPDATE SME_Customer_Count_Memory 
    SET Customer_Count = {customers}, Last_Updated = '{date}' 
    WHERE County_Name = '{area}'"""
)

# NOTE: Named style was not working, execute did not succeed. Switched to using .format for sqlite3 db statements.
#Example:
# sql_update_customers_table_sme_sqlite3 = textwrap.dedent(
#     """UPDATE SME_Customer_Count_Memory
#     SET Customer_Count = :customers, Last_Updated = ':date'
#     WHERE County_Name = ':area'"""
# )
