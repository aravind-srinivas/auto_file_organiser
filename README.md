## Auto File Organizer

1. This is automation script which organize files into sub-folders when an file is dropped into the source directory after running this script the file will move and group it based on your priority. 

2. This can come in handy when you are downloading multiple file for an project or can be use in your downloads folder 

3. This script will arrange and move the files when it is downloaded. 


### Prerequisites

1. Python installed on your machine
2. Watchdog module for monitoring the folder when an file is created

### Installing

1. Go to https://www.python.org/ and download the latest python version and install it if python is not already installed in your system

2. Install the watchdog module by typing -- "pip3 install watchdog" in terminal or command prompt

### Things to Change

1. Change the "folder_to_track" and "folder_destination" path - If both are same paste the same path in both the variables
2. Changes the file types - I have added the common files types and its respective grouping sub folder names 
3. If you want to save an specific file type alone in an folder Eg. If you want Only Word Documents alone in a specific folder then change the file type in src.endswith((".docx" , ".doc")) and change the sub folder name in "dest_sub_folder" as "Word Documents/"

### Autorun at Startup

1. Enable Autorun to run this python file at startup to run it automatically during every boot up else need to run manually

### Logs

1. An log file named "auto_file_organizer_log.txt" will be created in the same directory and once the file is moved there will be an log in this text file

### Authors

#### **Aravind Srinivasan** 
* **GitHub** : https://github.com/aravind-srinivas
* **Email** : aravind.s.srinivas@gmail.com




