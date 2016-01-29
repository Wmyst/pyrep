from tourcontroller import db
from sqlalchemy import Column, Integer, String


class Location(db.Model):
    __tablename__="location"
    loc_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    # date_start = db.Column(db.Date, nullable=False)
    # date_finish = db.Column(db.Date, nullable=False)
    # description = db.Column(db.String, nullable=False)
    # geo = db.Column(db.String)
    # im_path = db.Column(db.String)


    def __init__(self, name):  ## date_start, date_finish, description, geo, im_path):
        self.loc_id = loc_id
        self.name = name
        # self.date_start = date_start
        # self.date_finish = date_finish
        # self.description = description
        # self.geo = geo
        # self.im_path = im_path

    def __repr__(self):
        return '<Tour_stop {0}>.format(self.name)'