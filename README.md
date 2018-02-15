#RDS Automation - Manual Snapshot Creation

AWS Lambda is a compute service that lets you run code without provisioning or managing servers. AWS Lambda executes your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time you consume - there is no charge when your code is not running. With AWS Lambda, you can run code for virtually any type of application or backend service - all with zero administration. 


Requirements:
1. Python 3.6 - boto
2. AWS Account - user access and secret access credentials

Installation:
1. Kindly install the packages involved by checking the lambdaEvent.py file
	example:	pip install shutil
2. Change the session details in the file and add your aws account details. 


Run:
1. run the lambdaEvent.py file
	python lambdaEvent.py
