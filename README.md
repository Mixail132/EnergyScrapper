## Description
The project is about getting data from third party application database using Python.\
The application is called 'Energy Control Center'.\
The purpose of the application is collecting energy consumption data from energy counters.\
The application has Firebird database.\
The project scripts retrieve the data from the database without using the application.\
After that the data will be stored into Excel file to get more readable view and to process the data.

## Initials
Firebird (win32) should be installed.\
The project works on Poetry, it should be installed and initialized.\
Python 32 bit should be installed.\
Firebird driver 'fdb' is needed.\
The Firebird service called FirebirdServerDefaultInstance should be running on your computer.\
You can run 'fbserver.exe' if the service that mentioned above is running.\
You don't need 'Energy Control Center' software running on your computer.\
You even don't  need 'Energy Control Center' to be installed on your computer.\
All you need is the database with the latest data for today.\
Also you need '.env' file with paths to the database, dbclient file and receiving the data Excel file.


## Components
Firebird 2.1.3\
Poetry 1.7.1\
Python 3.8.10\
Fdb    2.18.3\
Tkinter 0.1.0

## Launching
For launching the database scrapping simply run 'views.py' for 31 days retrieving from today.
