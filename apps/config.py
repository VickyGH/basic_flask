import os
from dataclasses import dataclass
from os.path import abspath, dirname, join

basedir = abspath(dirname(__file__))
DB = join(basedir, "database.db")

@dataclass
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@dataclass
class LocalConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask"


@dataclass
class StagingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask"


config = {
    "LOCAL" : LocalConfig,
    "STAGING" : StagingConfig,
}