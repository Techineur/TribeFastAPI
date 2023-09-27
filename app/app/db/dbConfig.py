# Author Block
# -----------
# name: Tarun Neeraj
# email: tarun@techineur.com
# GitHub ID: frozenloser
# Description
# -----------
# This file contains the required config to connect to the database.
#


# Importing Modules
from sqlmodel import SQLModel, create_engine
from sqlmodel.pool import StaticPool
import sqlmodel

from app.config import config
from app.db import models

# Creating a database engine
engine = create_engine(
    config.DB_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

