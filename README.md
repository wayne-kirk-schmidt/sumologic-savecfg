Sumo Logic Save Configuration
=============================

For you Sumo Logic environment as code, you know you want to backup and restore content but what about confiiguration changes?

We have just the thing; Sumo Logic integration to allow you to report and archive your key configuration items.

And, in the spirit of "Sumo on Sumo" we can also publish the record of configuration changes into Sumo Logic to query.

Installing the Scripts
=======================

The scripts are CLI based, designed as a stand alone CLI or incorporated in a DevOPs tool such as Chef or Ansible.

Written in python3, all scripts are listed below, and there is a Pipfile to show what modules are required to run.

You will need to use Python 3.6 or higher and the modules listed in the dependency section.  

Please follow the following steps to install:

    1. Download and install python 3.6 or higher from python.org. Append python3 to the LIB and PATH env.

    2. Download and install git for your platform if you don't already have it installed.
       It can be downloaded from https://git-scm.com/downloads
    
    3. Open a new shell/command prompt. It must be new since only a new shell will include the new python 
       path that was created in step 1. Cd to the folder where you want to install the scripts.
    
    4. Execute the following command to install pipenv, which will manage all of the library dependencies:
    
        sudo -H pip3 install pipenv 
 
    5. Clone this repository and change into the directory.

    6. run pipenv to install dependencies (this may take a while as this will download required libraries):

        pipenv install
        
Dependencies
============

See the contents of "pipfile"

Script Names and Purposes
=========================

Scripts and Functions:

    1. ./bin/sumologic_savecfg.py -h
  
       print a usage message and exit

    2. ./bin/sumologic_savecfg.py -c <cfgile>

       use a configuration file for the API key name, string, API endpoint, and organization ID

    3. ./bin/sumologic_savecfg.py -v <integer>

       provide increasingly verbose output on the script execution

    4. ./bin/sumologic_savecfg.py -p <publishtarget>

       publish the output of the script to a Sumo Logic source Category

NOTE: This may take several minutes to get the indexing done. 

    5. ./bin/sumologic_savecfg.py -a <apikey>:<apisecret>

       specify the API key to use to connect to the Sumo Logic environment

    6. ./bin/sumologic_savecfg.py -q <queryname>

       specify the query to use. the default is run all of the queries

Uncoming Features:
==================

* Provide different output formats in addition to CSV and stdout

* Provide a datestamp for all of the output

License
=======

Copyright 2022 Wayne Kirk Schmidt
https://www.linkedin.com/in/waynekirkschmidt

Licensed under the Apache 2.0 License (the "License");

You may not use this file except in compliance with the License.
You may obtain a copy of the License at

    license-name   APACHE 2.0
    license-url    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Support
=======

Feel free to e-mail me with issues to: 

*    wschmidt@sumologic.com

*    wayne.kirk.schmidt@gmail.com

I will provide "best effort" fixes and extend the scripts.
