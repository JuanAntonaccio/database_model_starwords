import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
import enum

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    pasword = Column(String(100), nullable=False)

class Tipos(enum.Enum):
    personaje = 1   
    planeta = 2

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    favorito_id = Column(Integer, nullable=False)
    tipo = Column(Enum(Tipos), nullable=False)

    def to_dict(self):
        return {}

class Personajes(Base):
    __tablename__='personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)
    mass = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)

class Planetas(Base):
    __tablename__='planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    rotation_period = Column(String(50), nullable=False)
    orbital_period = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')