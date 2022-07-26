#!/usr/bin/python3
"""Module defines database storage engine for hbnb application"""

from os import getenv
from sqlalchemy import create_engine

class DBStorage:
    """this class creates engine and manages database storage of hbnb models"""
    # private class attributes
    __engine = None
    __session = None

    # publc instance methods
    def __init__(self):
        """Instantiates engine and connects it to hbnb database"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user,
                                                                           pwd,
                                                                           host,
                                                                           db),
                                      pool_pre_ping=True)
        env = getenv('HBNB_ENV')
        if env == 'test':  # drop all tables if working in test environment
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """queries current db session with option to filter by cls"""
        # create tuple of classes to easily find out if filter option in use
        classes = (User, State, City, Amenitty, Place, Review)
        objdict = {}  # method needs to return a dictionary
        filterdic = {}  # dictionary to return a filtered query's results
        if cls is None:
            pass

    def close(self):
        """call remove method on the private __session attr"""
        self.__session.remove()
