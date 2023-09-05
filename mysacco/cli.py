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
# COMMAND /////////////////////////////////SHUTTLE

@click.command()
@click.argument('sacco_name')
def showsaccomembers(sacco_name):
    '''
    shows all sacco's members
    Args:
        sacco_name(str): The sacco's name
        

    '''
    session=Session()
    
    s_sacco=session.query(Sacco).filter(Sacco.name==sacco_name).first()
    members=s_sacco.all_members

    session.commit()
    click.echo("Here are the sacco's members:")
    if len(members)==0:
        click.echo("None")
    else:
        for each in members:
            click.echo(f"{each.first_name} {each.last_name}")
    
  # COMMAND ///////////////////////////////// 
  
  
@click.command()
@click.argument('sacco_name')
def showsaccovehicles(sacco_name):
    '''
    shows all sacco's members
    Args:
        sacco_name(str): The sacco's name
        

    '''
    session=Session()
    
    s_sacco=session.query(Sacco).filter(Sacco.name==sacco_name).first()
    s_vehicles=session.query(Shuttle).filter(Shuttle.sacco_id==s_sacco.id).all()

    session.commit()
    click.echo("Here are the sacco's vehicles:")
    if len(s_vehicles)==0:
        click.echo("None")
    else:
        for each in s_vehicles:
            click.echo(f"{each.number_plate}")
    
  # COMMAND ///////////////////////////////// 
  
  
@click.command()
def showallsaccos():
    '''
    Displays all the saccos and managers
    Args:
        No arguments
    '''
    session=Session()
    allsaccos=session.query(Sacco).all()

    session.commit()
    click.echo([f"Name: {each.name}  -  Manager: {each.manager}" for each in allsaccos])
# COMMAND /////////////////////////////////SHUTTLE



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
    
    
  # COMMAND 5/////////////////////////////////  
@click.command()
@click.argument('plate_no')
def showtype(plate_no):
    '''
    Returns the type of vehicle
    Args:
        plate_no(str): The Vehicle's plate number
    '''
    session=Session()
    
    vehicle=session.query(Shuttle).filter(Shuttle.number_plate==plate_no).first()
    
    session.commit()
    click.echo(f"The vehicle's type : {vehicle.type}")
    
# COMMAND ///////////////////////////////// 

@click.command()
@click.argument('the_type')
def showvehiclesoftype(the_type):
    '''
    Shows the vehicles of the input type
    Args:
        the_type(str): The Vehicle's type
    '''
    session=Session()
    
    vehicle=session.query(Shuttle).filter(Shuttle.type==the_type).all()
    
    session.commit()
    click.echo("Here are the vehicles of that type!")
    if len(vehicle)==0:
        click.echo("None")
    else:
        for each in vehicle:  
            click.echo(each.number_plate)
    
  # COMMAND /////////////////////////////////   
  
@click.command()
def showallvehicles():
    '''
    Shows all the vehicles and the owner
    Args:
        No argument
    '''
    session=Session()
    
    vehicles=session.query(Shuttle).all()
    
    session.commit()
    click.echo("Here are the vehicles and their owners")
    for each in vehicles:
        click.echo(f"Vehicle's plate no.: {each.number_plate}  Owner: {each.its_owner.first_name} {each.its_owner.last_name}")
    
# COMMAND ///////////////////////////////// 


@click.command()
@click.argument('plate_no')
def knowsacco(plate_no):
    '''
    Shows the sacco of the vehicle
    Args:
        plate_no(str): The Vehicle's plate number
    '''
    session=Session()
    
    vehicle=session.query(Shuttle).filter(Shuttle.number_plate==plate_no).first()
    
    session.commit()
    click.echo(f"Belongs to : {vehicle.its_sacco.name} sacco.")
    
  # COMMAND /////////////////////////////////   
  
@click.command()
@click.option('--plate_no',"-p")
@click.option('--firstname',"-f")
@click.option('--lastname',"-l")
def changeowner(plate_no,firstname, lastname):
    '''
    Changes the vehicles owner
    Args:
        plate_no(str): The Vehicle's plate number
        
    
    '''
    session=Session()
    
    vehicle=session.query(Shuttle).filter(Shuttle.number_plate==plate_no).first()
    owner_id1=vehicle.owner_id
    session.query(Member).filter(Member.id==owner_id1).update({
                                    Member.first_name: firstname,
                                    Member.last_name: lastname
                                        })
    session.commit()
    click.echo(f"Name of the owner changed successfully to {firstname} {lastname}!")
    
  # COMMAND ///////////////////////////////// 

@click.command()
@click.option('--plate_no',"-p")
@click.option('--firstname',"-f")
@click.option('--lastname',"-l")
def changeowner(plate_no,firstname, lastname):
    '''
    Changes the vehicles owner
    Args:
        plate_no(str): The Vehicle's plate number
        
    
    '''
    session=Session()
    
    vehicle=session.query(Shuttle).filter(Shuttle.number_plate==plate_no).first()
    owner_id1=vehicle.owner_id
    session.query(Member).filter(Member.id==owner_id1).update({
                                    Member.first_name: firstname,
                                    Member.last_name: lastname
                                        })
    session.commit()
    click.echo(f"Name of the owner changed successfully to {firstname} {lastname}!")
    
    
  # COMMAND ///////////////////////////////// 

@click.command()
def showallowners():
    '''
    Shows all the owners of vehicles
    Args:
        None
        
    
    '''
    session=Session()
    
    s_members=session.query(Member).all()
    session.commit()
    click.echo("Here are all the members: ")
    for each in s_members:
        click.echo(f"{each.first_name} {each.last_name}")
    
  # COMMAND ///////////////////////////////// 
  
session.close()
if __name__ =="__main__":
    # main.add_command(greet)
    main.add_command(addsacco)
    main.add_command(deletesacco)
    main.add_command(changemanager)
    main.add_command(showallsaccos)
    main.add_command(showsaccomembers)
    main.add_command(showsaccovehicles)
    
    main.add_command(showvehiclesoftype)
    main.add_command(showtype)
    main.add_command(knowsacco)
    main.add_command(knowowner)
    main.add_command(showallvehicles)
    main.add_command(changeowner)
    main.add_command(showallowners)
    # main.add_command(showallsaccos)
    # main.add_command(addsacco)
    # main.add_command(deletesacco)
    # main.add_command(changemanager)
    # main.add_command(knowowner)
    # main.add_command(showallsaccos)
    
    
    main()