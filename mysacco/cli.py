import click
from models import Sacco, Member, Shuttle, engine
from sqlalchemy.orm import sessionmaker

Session=sessionmaker(bind=engine)
session=Session()

@click.group()
def main():
    pass

# @click.command()
# @click.argument('comp')
# @click.option('--name',"-n", default='John', help='The name to greet.')
# @click.option('--greeting',"-g", default="Hi there", help="Greets the user")
# def greet(comp, name, greeting):
#     '''This is supposed to say Hello to someone'''
    
#     message=f"{comp}! {greeting}, {name}"
#     click.echo(message)

# COMMAND 1//////////////
@click.command()
@click.argument('name_')
@click.argument('manager_')
def addsacco(name_, manager_):
    '''
    Adds a Sacco to the database
    Args:
        name_(str): The Sacco's nameo
        manager_(str): The manager of the Sacco
    '''
    
    session=Session()
    new_sacco=Sacco(name=name_, manager=manager_)
    session.add(new_sacco)
    
    session.commit()
    click.echo("Sacco Successfully added!")
    
# COMMAND 2 //////////////////
@click.command()
@click.argument('name_')
def deletesacco(name_):
    '''
    Deletes a Sacco from the database
    Args:
        name_(str): The Sacco's name
    '''
    session=Session()
    
    session.query(Sacco).filter(Sacco.name==name_).delete()
    
    session.commit()
    click.echo("Sacco Successfully deleted!")
    
# COMMAND 3 ///////////////
@click.command()
@click.argument('name_')
@click.argument('new_manager')
def changemanager(name_, new_manager):
    '''
    Changes the manager of a database
    Args:
        name_(str): The Sacco's name
        new_manager(str): New Manager's name
    '''
    session=Session()
    
    session.query(Sacco).filter(Sacco.name==name_).update({
                                        Sacco.manager: new_manager
                                                        })
    
    session.commit()
    click.echo("Manager Successfully changed!")
    
# COMMAND 4/////////////////////////////////SHUTTLE

@click.command()
@click.argument('plate_no')
def knowowner(plate_no):
    '''
    Returns the owner of the Vehicle
    Args:
        plate_no(str): The Vehicle's plate number
    '''
    session=Session()
    
    vehicle=session.query(Shuttle).filter(Shuttle.number_plate==plate_no).first()
    
    session.commit()
    click.echo(f"The owner is : {vehicle.its_owner.first_name} {vehicle.its_owner.last_name}.")
    
    
  # COMMAND 4/////////////////////////////////  
    
    # The type of vehicle
    
    
session.close()
if __name__ =="__main__":
    # main.add_command(greet)
    main.add_command(addsacco)
    main.add_command(deletesacco)
    main.add_command(changemanager)
    main.add_command(knowowner)
    
    
    main()