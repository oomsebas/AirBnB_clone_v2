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
from models.engine.file_storage import DBStorage
import os


class test_dbStorage(unittest.TestCase):
    """Tests for db storage mode"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != db,
                     "only test for db storage, not file storage")
    def test_doc(self):
        """Test docstrings"""
        self.assertIsNotNone(DBStorage.__doc__)
