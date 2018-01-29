# Logs Analysis Project #

This project is for building a reporting tool that prints out reports that are plain text from the SQL Server database using python program. It uses the tables articles, authors and logs  from the database to print 3 reports.

## Software Requirements: ##

*     [Python Download](https://www.python.org/downloads/)

*     [Git Download](https://git-scm.com/downloads)

*     [Virtual Box](https://www.virtualbox.org/wiki/Downloads)

*     [Vagrant Download](https://www.vagrantup.com/downloads.html)

*     [VM Configuartion](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

## Installation: ##

- Install the python according to your system configuration using default options.
- Install git according to your system configuration using default options.
- Install Virtual Box according to your system configuration using default options. Don&#39;t launch after installing.
- Install Vagrant according to your system configuration using default options.
- Unzip the VM Configuration file. It will be downloaded as FSND-Virtual-Machine in the downloads folder.

## Getting Started: ##

- Download the folder news and unzip it in the vagrant folder.
- The vagrant folder is located in the FSND-Virtual-Machine folder.
- Open the news folder and right click in the same window and click on git bash here.
- A  Git terminal page will open and you need to type vagrant up. This may take a few moments.
- After it is done downloading you need to type vagrant ssh and wait for few seconds until it  is done.
- Type cd /vagrant press Enter and then type cd news.
- Then type psql  –d news  –f newsdata.sql  to load data into the database.
- Then type psql –d news and press Enter then type the below sql query to create view tot1.

                 create view tot1 as select time::date, count(status) as tot\_logs from log group by                              time::date order by tot\_logs desc;

- It creates the view required for the project. Also type the below sql to create the
following view.

                  create view tot2 as select time::date, count(status) as tot\_errs from log where status  like &#39;404%&#39;  group by time::date order by tot\_errs desc;

- The views will be created for the project to work.

## Running the Program: ##

- Type \q press Enter. Then type python news.py
-  It prints the reports for you.

## Conclusion: ##

   The project thus displays the 3 reports.

-        Retrieves the 3 popular articles based on views.
-        Retrieves the popular authors based on views.
-        Retrieves the most error prone days.
