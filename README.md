# Python Group project #9
Students:
* Glenn Valdivieso
* Jhonatan Salas

## Overview
This code shows a website that is based on flask, and shows a table retrieved from a database which contains a dataframe
collected from an external source.


## What steps you have to follow?
- Internet connection required to retrieve the dataset stored in the internet (csv file) and be imported into a database.
- Download or clone our repository to your device. This includes all files required to run this project.
- type `pip install -r requirements.txt` in command prompt (this will install required package for project). In case you have already installed below libraries, please omit this step:


| Library| Version used in the project |
  |:----------: |:----------------:|
  |pandas | 2.2.2 |
  |flask|3.0.3|
  |pathlib| 1.0.1|


- Execute each block of `main.ipynb` file to create database file. This database will stored data collected from a external source.
	* **N.B.: DB file named `koba.db` will be created at this step, and It needs to be reachable on next stage.**
- Extract the folder path where you stored our repository. Then edit *base_path* variable located in line #8 inside `app_template_detail.py` file.
	This steps allows you read the database file in order to show this data through the website.
- Save `app_template_detail.py` file to keep new modifications.
- Execute `app_template_detail.py` to initialize web server from your device.
- Surf into the website [127.0.0.1/5000](127.0.0.1/5000).

## Project flow & explaination

Our code performs below actions sequencely:

**main.ipynb** file:

1. Import of required libraries. For this stage we will use pandas ans sqlite3.
2. Data collection from external repository reading a CSV file that is located externally. All this data is stored in variable 'df'.
3. After we create 'createDB' function, we pass below inputs to this function:
* DBname: Name of the database.
* FileName: This can be a file path either locally or from the web.
* TableName: Name of the table
4. Access to connection `conn` using sqlite library to check if data is reachable from database file. 
		
**app-template-detail.py** file:

1. Import of required libraries. For this stage we will use flask, sqlite3, and pathlib.
2. In order to find the Database file (in this case `kobe.db`) we need to update this `.py` file to reach this file.
3. Use of modules of flask to show structurally our webpage.
4. Additional implementations:
   	* Use of a filter for 'game' attribute. Only numbers are allowed.
   	* Top navigation bar present on all pages:
   	  	* Home: It goes to index_link.html page (as a typical Home page).
   	  	* Data: It goes to data page (data_table.html)
   	  	* About: It goes to abou page (about.html)
   	  

   Below is a tree of how our website was designed:

		Access to 127.0.0.1:5000:
		
		index page (index_links.html)
   		 Top navigation BAR
   			|---Home (index_links.html) 
			|
			|
			|---Data  (data_table.html)
			|		|
			|	Access to the DB
			|		|
			|	Store of the data into 'kobe' variable
			|		|
			|	Data allocation to proper column
   			|		|
   			|		|-----Box to filter data for 'game' attribute.	
			|
			|
			|
			|---About (about.html)
					|
					|---Source of the data
					|
					|---Definition of the variables
			
			


