# Log Analysis Project
This project is required for Udacity's Full Stack Web Developer Nanodegree program.

# Introduction
The purpose is creating an internal reporting tool that answers the following questions about the newspaper site:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Prerequisites
1. Start	with	Software	Installation:
* Vagrant:	https://www.vagrantup.com/downloads.html	
* Virtual	Machine:	https://www.virtualbox.org/wiki/Downloads	
* Download	a	FSND	virtual	machine:	https://github.com/udacity/fullstack-nanodegree-vm	
<br />Once	you	get	the	above	software	installed,	follow	the	following	instructions:	
<br />1. cd vagrant.
<br />2. vagrant up.
<br />3. vagrant ssh. 
<br />4. cd /vagrant.
<br />5. mkdir log-analysis-project.
<br />6. cd log-analysis-project. 
 
2. Download	and	Load	the	Data:
* Download	“newsdata.sql” by	clicking	on	the	following	link: 
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
* Move	the	“newsdata.sql”	to the project	folder	“log-analysis-project”	
* Load	the	data	from	the	“newsdata.sql”	by	using	the	following	command:<br /> psql -d news -f newsdata.sql 
* Note	that	we	are	using	PostgreSQL	for	this	projec.
* Once	you	have	the	data	loaded	into	database,	connect	to	it	using:<br /> psql -d news

# Run The Project
1. Make sure that you have vagrant up and connected to it.
2. cd into the correct project directory: cd /vagrant/log_analysis
3. Run python loganalysisdb.py
# Create Views
```
CREATE VIEW subtotalview AS SELECT DATE(time),COUNT(*) AS subtotal 
FROM log 
WHERE status='404 NOT FOUND' 
GROUP BY DATE(time) 
ORDER BY subtotal DESC;
```
```
CREATE VIEW totalview AS SELECT DATE(time), COUNT(*) AS total
FROM log 
GROUP BY DATE(time) 
ORDER BY total DESC;
```

# The Output
The most popular three articles of all time:
<br /> "Candidate is jerk, alleges rival" - 338647 views
<br /> "Bears love berries, alleges bear" - 253801 views
<br /> "Bad things gone, say good people" - 170098 views
<br />
<br />The most popular article authors of all time:
<br /> Ursula La Multa - 507594 views
<br /> Rudolf von Treppenwitz - 423457 views
<br /> Anonymous Contributor - 170098 views
<br /> Markoff Chaney - 84557 views
<br />
<br /> Days with more than 1% of requests lead to errors is:
<br /> July 17, 2016 - 2.26% errors
