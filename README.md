# Transport-based-project
A project that has models ( Sacco, Vehicles and Members(owners of the vehicles)) that try to immitate the transport sector in Kenya, a real world example.

Saccos have may vehicles,each vehicle belongs to a specific sacco --One to many relationship
Members have may vehicles,each vehicle belongs to a specific member --One to many relationship
Saccos have many members , Members can belong to may saccos  --Many to many relationship

# Setting up the project
Clone to local repository , then (pipenv install)
(pipenv shell) , (cd mysacco)

Run (python cli.py --help) to see the command

# Dependencies
sqlalchemy
alembic 
faker
click



