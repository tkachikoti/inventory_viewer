"""This module creates the data for the database. It is called by the
create_app function inside the app directory __init__.py module soon
after a connection with the database is established. This module 
imports the database object and GoblinCakeSales model from the models
module located in the app directory.
"""

from .models import db
from .models import GoblinCakeSales

def create_data_after_db_init():
    """This function creates the data for the database."""
    db.session.add(GoblinCakeSales(product='Hobgoblin', product_type='Cake', price_per=4, units_sold=388, quarter=1))
    db.session.add(GoblinCakeSales(product='Green Goblin', product_type='Cake', price_per=4, units_sold=312, quarter=1))
    db.session.add(GoblinCakeSales(product='Forest Sprite', product_type='Canned Drink', price_per=0.8, units_sold=97, quarter=1))
    db.session.add(GoblinCakeSales(product='Redcap', product_type='Cake', price_per=3.5, units_sold=605, quarter=1))
    db.session.add(GoblinCakeSales(product='Imp', product_type='Cake', price_per=2, units_sold=162, quarter=1))

    db.session.add(GoblinCakeSales(product='Hobgoblin', product_type='Cake', price_per=4, units_sold=482, quarter=2))
    db.session.add(GoblinCakeSales(product='Green Goblin', product_type='Cake', price_per=4, units_sold=312, quarter=2))
    db.session.add(GoblinCakeSales(product='Forest Sprite', product_type='Canned Drink', price_per=0.8, units_sold=123, quarter=2))
    db.session.add(GoblinCakeSales(product='Redcap', product_type='Cake', price_per=4, units_sold=401, quarter=2))
    db.session.add(GoblinCakeSales(product='Imp', product_type='Cake', price_per=1.5, units_sold=540, quarter=2))
    db.session.add(GoblinCakeSales(product='Filthy Hobbit', product_type='Cookie', price_per=1, units_sold=325, quarter=2))

    db.session.add(GoblinCakeSales(product='Hobgoblin', product_type='Cake', price_per=4, units_sold=389, quarter=3))
    db.session.add(GoblinCakeSales(product='Green Goblin', product_type='Cake', price_per=4, units_sold=302, quarter=3))
    db.session.add(GoblinCakeSales(product='Forest Sprite', product_type='Canned Drink', price_per=0.8, units_sold=168, quarter=3))
    db.session.add(GoblinCakeSales(product='Redcap', product_type='Cake', price_per=4, units_sold=433, quarter=3))
    db.session.add(GoblinCakeSales(product='Imp', product_type='Cake', price_per=2, units_sold=486, quarter=3))
    db.session.add(GoblinCakeSales(product='Filthy Hobbit', product_type='Cookie', price_per=1, units_sold=164, quarter=3))
    db.session.add(GoblinCakeSales(product='Wretched Elf', product_type='Cookie', price_per=1, units_sold=212, quarter=3))
    db.session.add(GoblinCakeSales(product='Foul Dwarf', product_type='Cookie', price_per=1, units_sold=168, quarter=3))
    db.session.add(GoblinCakeSales(product='Vile Human', product_type='Cookie',price_per=1, units_sold=92, quarter=3))

    db.session.add(GoblinCakeSales(product='Hobgoblin', product_type='Cake', price_per=4, units_sold=369, quarter=4))
    db.session.add(GoblinCakeSales(product='Green Goblin', product_type='Cake',price_per= 4, units_sold=333, quarter=4))
    db.session.add(GoblinCakeSales(product='Forest Sprite', product_type='Canned Drink', price_per=0.8, units_sold=168, quarter=4))
    db.session.add(GoblinCakeSales(product='Redcap', product_type='Cake', price_per=4, units_sold=462, quarter=4))
    db.session.add(GoblinCakeSales(product='Imp', product_type='Cake',price_per=2, units_sold=501, quarter=4))
    db.session.add(GoblinCakeSales(product='Filthy Hobbit', product_type='Cookie', price_per=1, units_sold=125, quarter=4))
    db.session.add(GoblinCakeSales(product='Wretched Elf', product_type='Cookie', price_per=1, units_sold=201, quarter=4))
    db.session.add(GoblinCakeSales(product='Foul Dwarf', product_type='Cookie', price_per=1, units_sold=162, quarter=4))
    db.session.add(GoblinCakeSales(product='Vile Human', product_type='Cookie', price_per=1, units_sold=143, quarter=4))
    db.session.add(GoblinCakeSales(product='Wizard Spit', product_type='Hot Drink', price_per=3.5, units_sold=455, quarter=4))
    db.session.add(GoblinCakeSales(product='Brownie', product_type='Cake', price_per=1.5, units_sold=666, quarter=4))

    db.session.commit()
