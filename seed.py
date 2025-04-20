from sqlalchemy.orm import Session
from database import engine
import models as m


m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

# with Session(bind=engine) as session:
#     p1 = m.Product(product_name="Milk")
#     session.add(p1)
#     p2 = m.Product(product_name="Bread")
#     session.add(p2)
#     plt1 = m.Planet(planet_name="Земля", planet_mass=5.9, planet_diameter=12756)
#     session.add(plt1)
#     plt2 = m.Planet(planet_name="Венера", planet_mass=4.87, planet_diameter=12104)
#     session.add(plt2)
#     plt3 = m.Planet(planet_name="Марс", planet_mass=6.39, planet_diameter=6779)
#     session.add(plt3)
#     session.commit()

