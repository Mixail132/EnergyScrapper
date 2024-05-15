## Main
There are three parts in the project.
The first, called 'enargyscraper' - gets the electrical energy counters data.\
The second, called 'heatscrapper' - gets the heat energy counters data.\
The third, called 'excelupdater' - updates an Excel file , where all the data are shown together.

## Energy scraper
Gets an electrical energy consumption data from the third party application Firebird database.\
The application is called 'Energy Control Center' that collects consumption data from energy counters.\
Retrieves the data from the database without using the application.\
Stores the data into Excel file to get more readable view and to further process the data.

## Excel updater
Updates the links in Ecxel target storage file. 

## Initials
Firebird (win32) should be installed.\
The project works on Poetry, it should be installed and initialized.\
Python 32 bit should be installed.\
Firebird driver 'fdb' is needed.\
The Firebird service called FirebirdServerDefaultInstance should be running on your computer.\
You can run 'fbserver.exe' if the service that mentioned above is running.\
You don't need 'Energy Control Center' software running on your computer.\
You even don't  need 'Energy Control Center' to be installed on your computer.\
All you need is the database with the latest data.\
Also you need '.env' file with paths to the database, dbclient file and receiving the data Excel file.

## Modules 
Firebird 2.1.3\
Poetry 1.7.1\
Python 3.8.9\
Fdb    2.18.3

## Launching
For launching the database scraping simply run 'views.py'.\
For launching the updater simply run 'updater.py'.