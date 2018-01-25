#!/usr/bin/python
# -*- coding: utf-8 -*-

import getopt
import logging
import sys
import json
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
Session = sessionmaker()


class Record(Base):
    __tablename__ = 'record'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('record.id'))
    entry_time = Column(DateTime)
    sys = Column(Integer)
    dia = Column(Integer)
    pulse = Column(Integer)
    capture_type_id = Column(Integer, ForeignKey('capture_type.id'))
    capture_type = relationship('CaptureType')
    note = Column(String)
    sub_records = relationship('Record')

    def __repr__(self):
        return "{Record: {id: %d; capture_type_id: %d}}" % (self.id, self.parent_id)


class CaptureType(Base):
    __tablename__ = 'capture_type'

    id = Column(Integer, primary_key=True)
    description = Column(String)

    def __init__(self, description="New Capture Type"):
        self.description = description
        print(self.description)

    def __repr__(self):
        return "CaptureType: {id: {}; description: {}}" % (self.id if self.id is not None else "_None_", self.description)

    def json_string(self):
        if self.id is None:
            return '{id: none, description: "%s"}' % self.description
        else:
            return '{id: %s, description: "%s"}' % (self.id, self.description)
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

def init_db(engine):
    print("create db schema...")
    Base.metadata.create_all(engine)


def persist_record(session, data):
    session.add(data)
    session.commit()


def get_db_engine(dbname):
    db_str = 'sqlite:///' + dbname
    engine = create_engine(db_str, echo=True)
    return engine


def get_db_session(engine):
    Session.configure(bind=engine)
    session = Session()
    return session


def get_new_session(dbname):
    db_str = 'sqlite:///' + dbname
    engine = create_engine(db_str, echo=True)
    Session.configure(bind=engine)
    session = Session()
    return session


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:i:d:t:", ["action=", "input=", "db=", 'table='])
    except getopt.GetoptError as err:
        # print help information and exit:
        logging.error(str(err))  # will print something like "option -a not recognized"
        sys.exit(2)
    input_filename = None
    dbname = None
    tablename = all
    for option, value in opts:
        if option in ("-a", "--action"):
            action = value
        elif option in ("-i", "--input"):
            input_filename = value
        elif option in ("-d", "--db"):
            dbname = value
        elif option in ("-t", "--table"):
            tablename = value
        else:
            assert False, "unhandled option"

    engine = get_db_engine(dbname)

    if action == 'loaddata':
        logging.info('NOT SUPORTED: load data in [%s] to db is [%s]' % (input_filename, dbname))

    if action == 'getall':
        logging.info('NOT SUPORTED: load data in [%s] to db is [%s]' % (input_filename, dbname))

    if action == 'create':
        logging.info('create db schema [%s]' % dbname)
        init_db(engine)

    logging.info('task done')


if __name__ == "__main__":
    main()
