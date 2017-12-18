#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine('sqlite:///./bprecords.db')

Base = declarative_base()

class BPRecord(Base):
    __tablename__ = "bp_record"

    Id = Column(Integer, primary_key=True)
    EntryTime = Column(DateTime)
    Sys = Column(Integer)
    Dia = Column(Integer)
    Pulse = Column(Integer)

    Base.metadata.bind = engine
    Base.metadata.create_all()