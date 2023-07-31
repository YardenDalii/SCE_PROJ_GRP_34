#this is a readme file for explorair website
#this project has been developed by
#Achva Skuri
#Mor Bar
#Eshed Sorotsky
#Yarden Dali


#installation
there are quite alot of prerequisite.
the project was develeoped in django on AWS EC2 windows server 2019.

#steps

#1 -
create AWS EC2 instance running windows server 2019.
configure security groups for the EC2 instance (inbound and outbound)
assign public static IP to the Instance

#2 - 
install python (currently using V3.7.9)

#3 - 
install django (using pip install)

#4 - 
install mysqlclient (pip install)

#5 -
install wsgi (pip install)

#6 - 
install apache2.4 on C:\

#7 - 
install mysqlserver for windows

#8 - 
pull/clone the git repo

#9 -
configure apache to communicate with WSGI in django project (refer online for assistance)
configure apache to listen to port 80 (should be by default)
configure apache to allow access for WSGI file 
configure apache to allow access to all static/template files folders

#configuring
need to configure the settings.py in the django app to communicate with local mysqlserver (refer online for assistance)

#running the server
after all the configurations has been made
open CMD and run the command "cd c:\apache24\bin"
run command "httpd.exe"
and try to access the website using the public ip you assigned to your EC2 Instance

*can also purchase a domain and assign it to access using a DNS server and not directly using the server IP
