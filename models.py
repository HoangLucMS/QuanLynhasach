from sqlalchemy import Column, String, Integer
from quanlynhasach import  db, app

class









if __name__ = '__main__':
    with app.app_context():
        db.create_all()