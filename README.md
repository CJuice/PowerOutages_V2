# MD Power Outages
This project processes power outage data, from provider companies serving MD citizens, for use by the MEMA.

The process consists of a main procedural python script that relies on multiple class modules. The Main script 
coordinates all of the process functionality. Imports to Main include multiple modules that begin with
'doit_' to identify them as custom and not widely available python libraries. 

Main is generally organized into the following order of sections: imports, variable definition/creation, 
web requests for various provider related data, processing of response data, output of feed status to json file,
database transactions for 'realtime' and 'archive' and customer data, and transactions with the open data portal
for cloud storage of outage data.

Main relies on the following imported modules containing classes: ArchiveClasses, BGEClasses, CTKClasses, 
CustomerClass, DatabaseFunctionality, DELClasses, EUCClasses, FESClasses, PEPClasses, 
SMEClasses, UtilityClass. It also relies on a CentralizedVariables python file, and 
access through a parser to a Credentials config file and a ProvidersURI config file.

The process is designed as a main procedural script utilizing class functionality. For power providers, there is a 
top level parent class called Provider. All providers are then subclassed from this parent to create child classes. 
The child classes contain unique behavior specific to a provider. Functionality/behavior common to all providers has 
been placed into the parent class and inherited downward into the children. PEP DEL and BGE are child class that
inherit from Kubra_ParentClass, which inherits from Provider. This class organizes behavior common to Kubra 
feeds which are common to PEP DEL and BGE. Where necessary, some methods in parent classes have been overloaded
by methods in child classes.

A Utility class is used by all modules and serves as a static resource for common/shared helper functions and a few
simple variables. The Centralized Variables module contains variables, no classes or functions, and environment related
variables and sql statements. It is not intended to be used by Utility class.

A Web Related Functionality class exists for web related functionality and is accessed by the Provider exclusively.
The output json file named PowerOutageFeeds_StatusJSON.json is stored in a folder named JSON_Outputs.

This is an overhaul/redesign of an original process developed by CGIS.

#### Code Architecture
![code architecture image](https://github.com/CJuice/PowerOutages_V2/blob/master/Power%20Outage%20Process%20-%20Code%20Architecture.png)