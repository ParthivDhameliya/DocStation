from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Registration(Base):
    __tablename__ = "registrations"

    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    patientPrefix = Column(String)
    firstName = Column(String)
    middleName = Column(String)
    lastName = Column(String)
    preferredName = Column(String)
    email = Column(String, unique=True)
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
    currentDate = Column(Date, default=datetime.now())

    # owner = relationship("Users", back_populates="todos")


class Guardian(Base):
    __tablename__ = "guardians"

    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    prefixGuardian = Column(String)
    firstName = Column(String)
    middleName = Column(String)
    lastName = Column(String)
    preferredName = Column(String)
    contactNumber = Column(Integer)
    sameAddressAsAbove = Column(Boolean)
    street = Column(String)
    apt = Column(Integer)
    city = Column(String)
    province = Column(String)
    postalCode = Column(String)
    country = Column(String)
    patient_id = Column(Integer, ForeignKey("registrations.id"))
