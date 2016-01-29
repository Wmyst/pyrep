from tourcontroller import db
from models import Location

db.create_all()
db.session.add(Location("Hill House")
db.session.commit()