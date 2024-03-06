from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    patientPrefix = Column(String)
    firstName = Column(String)
    middleName = Column(String)
    preferredName = Column(String)
    lastName = Column(String)
    email = Column(String, unique=True, index=True)
    mobile = Column(Integer)
    homeNumber = Column(Integer)
    birthDate = Column(Date)
    age = Column(Integer)
    sex = Column(String)
    healthCareNumber = Column(Integer)
    street = Column(String)
    apt = Column(Integer)
    city = Column(String)
    province = Column(String)
    postalCode = Column(String)
    country = Column(String)
    school_employer = Column(String)
    relation = Column(String)
    emergencyContactName = Column(String)
    emergencyContactEmail = Column(String)
    emergencyContactNumber = Column(Integer)
    contactNumber = Column(Integer)

    # owner = relationship("Users", back_populates="todos")














