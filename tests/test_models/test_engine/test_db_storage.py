#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.db_storage import DBStorage
import os
import MySQLdb


tbl_cls = {"states": State, "cities": City, "places": Place,
           "amenities": Amenity, "users": User, "reviews": Review}


class test_dbStorage(unittest.TestCase):
    """Tests for db storage mode"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != "db",
                     "only test for db storage, not file storage")
    def test_doc(self):
        """Test docstrings"""
        self.assertIsNotNone(DBStorage.__doc__)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != "db",
                     "only test for db storage, not file storage")
    def test_all(self):
        """Test all method"""
        d = storage.all()
        self.assertTrue(type(d), dict)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != "db",
                     "only test for db storage, not file storage")
    def test_new(self):
        """Test new method"""
        db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                             passwd=os.getenv('HBNB_MYSQL_PWD'),
                             db=os.getenv('HBNB_MYSQL_DB'))
        cur = db.cursor()
        for tbl in tbl_cls:
            rows = cur.execute("SELECT COUNT(*) FROM {}".format(tbl))
            obj1 = tbl_cls[tbl]()
            storage.new(obj1)
            rows_final = cur.execute("SELECT COUNT(*) FROM {}".format(tbl))
            self.assertTrue(rows + 1, rows_final)
        cur.close()
        db.close()
