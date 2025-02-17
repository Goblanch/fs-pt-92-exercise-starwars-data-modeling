import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, Integer, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    email: Mapped[str] = mapped_column(String(80), nullable=False)
    
    favorites = relationship('Favorites', backref='user', lazy=True)


class Person(Base):
    __tablename__ = 'Person'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    gender: Mapped[str] = mapped_column(String(20), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(20), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    eye_color: Mapped[str] = mapped_column(String(20), nullable=True)
    mass: Mapped[int] = mapped_column(Integer, nullable=True)

    favorites = relationship('Favorites', backref='person', lazy=True)

    def to_dict(self):
        return {}
    
class Planet(Base):
    __tablename__ = "Planet"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    climate: Mapped[str] = mapped_column(String(30), nullable=False)
    terrain: Mapped[str] = mapped_column(String(30), nullable=False)
    gravity: Mapped[int] = mapped_column(Integer, nullable=False)
    diameter: Mapped[int] = mapped_column(Integer, nullable=False)
    orbital_period: Mapped[int] = mapped_column(Integer, nullable=False)
    rotation_period: Mapped[int] = mapped_column(Integer, nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)

    favorites = relationship('Favorites', backref='planet', lazy=True)

class Favorites(Base):
    __tablename__ = "Favorites"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    associated_user: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    people_id: Mapped[int] = mapped_column(Integer, ForeignKey('person.id'), nullable=True)
    planet_id: Mapped[int] = mapped_column(Integer, ForeignKey('planet.id'), nullable=True)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
