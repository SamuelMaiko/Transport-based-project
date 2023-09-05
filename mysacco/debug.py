from sqlalchemy.orm import sessionmaker
from models import engine, Sacco, Member, Vehicle
from faker import Faker

import random
import string

fake=Faker()

Session=sessionmaker(bind=engine)
session=Session()

session.query(Sacco).delete()
session.query(Vehicle).delete()
session.query(Member).delete()

# # ADDING 10 RANDOM NAMES TO THE DATABASE///////////////////
# random_members=[Member(first_name=fake.first_name(), last_name=fake.last_name()) for n in range(10)]
# session.bulk_save_objects(random_members)

# # ADDING 5 RANDOM SACCOS TO THE DATABASE///////////////////
# random_saccos=[Sacco(name=fake.company(), manager=fake.name()) for n in range(5)]
# session.bulk_save_objects(random_saccos)


# # ADDING 25 RANDOM SHUTTLES TO THE DATABASE///////////////////

# def generate_random_number_plate():
#     # Generate three random letters
#     letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    
#     # Generate three random numbers
#     numbers = ''.join(random.choice(string.digits) for _ in range(3))
    
#     # Combine letters and numbers with a space
#     return f"{letters} {numbers}"

# # Generate a random number plate
# random_plate = generate_random_number_plate()

# random_vehicles=[Vehicle(type=fake.random_element(elements=('Bus', 'Van', 'Minibus')), 
#                          number_plate=generate_random_number_plate(), 
#                          sacco_id=fake.random_int(min=1, max=5),
#                          owner_id=fake.random_int(min=1, max=10) ) 
#                  for n in range(25)]

# session.bulk_save_objects(random_vehicles)


# # RANDOM TESTING
# random_vehicle=session.query(Vehicle).filter(Vehicle.id==3).first()
# print(random_vehicle.its_sacco)


session.commit()
session.close()