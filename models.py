import pymongo
from mongo_db import db


User = db['User']
Location = db['Location']
AttendanceHistory = db['AttendanceHistory']
Settings = db['Settings']


User.create_index([('first_name', "text"), ('last_name', "text"), ('email', "text")], name='text_index')
# User.drop_indexes()
# print({"user_indexes": User.index_information()})
Location.create_index([('name', "text"), ('address', "text"), ('description', "text")], name='text_index')
Settings.create_index([('opens', "text"), ('closes', "text"), ('open_days', "text")], name='text_index')
AttendanceHistory.create_index([('email', "text"), ('user_id', "text")], name='text_index')


# # from ..config.database import Base
# from sqlite_database import Base # for sqlite db
# # from database import Base # for postgres db
# from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, Integer, Text, Float, JSON
# from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
# from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL, GUID_DEFAULT_SQLITE
# from json import dumps


# class User(Base):
#   __tablename__ = 'users'
#   id = Column(Integer, primary_key=True, index=True)
#   # id = Column(GUID, primary_key=True, index=True, default=GUID_DEFAULT_SQLITE) # for sqlite db
#   # id = Column(GUID, primary_key=True, default=GUID_SERVER_DEFAULT_POSTGRESQL) # for postgres db
#   first_name = Column(String, nullable=False, index=True)
#   last_name = Column(String, nullable=False, index=True)
#   email = Column(String, nullable=False, unique=True, index=True)
#   hashed_password = Column(String, nullable=True)
#   phone = Column(String, nullable=True)
#   image = Column(String, nullable=True)
#   image_encoding = Column(Text, nullable=True)
#   face_encoding = Column(Text, nullable=True)
#   qr_code = Column(String, nullable=True)
#   qr_code_content = Column(Text, nullable=True)
#   qr_code_b64 = Column(Text, nullable=True)
#   # location_id = Column(GUID, ForeignKey("locations.id"))
#   location_id = Column(Integer, ForeignKey("locations.id"), nullable=True)
#   is_active = Column(Boolean, nullable=False, default=True) # for sqlite db
#   is_admin = Column(Boolean, nullable=False, default=False) # for sqlite db
#   # is_active = Column(Boolean, nullable=False, server_default='True') # for postgres db
#   created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
#   updated_at = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())
#   reset_password_token = Column(String, nullable=True)
#   reset_token_expire = Column(TIMESTAMP(timezone=True), nullable=True)

#   attendance_history = relationship("AttendanceHistory", back_populates="user")
#   location = relationship("Location", back_populates="users")


# class Location(Base):
#   __tablename__ = 'locations'
#   id = Column(Integer, primary_key=True, index=True)
#   # id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE) # for sqlite db
#   # id = Column(GUID, primary_key=True, default=GUID_SERVER_DEFAULT_POSTGRESQL) # for postgres db
#   name = Column(String, nullable=False, index=True)
#   address = Column(String, nullable=False, index=True)
#   description = Column(String, nullable=True)
#   phone = Column(String, nullable=True)
#   longitude = Column(Float, nullable=True)
#   latitude = Column(Float, nullable=True)
#   radius = Column(Float, nullable=True)
#   is_active = Column(Boolean, nullable=False, default=True) # for sqlite db
#   # is_active = Column(Boolean, nullable=False, server_default='True') # for postgres db
#   created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
#   updated_at = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())

#   attendance_history = relationship("AttendanceHistory", back_populates="location")
#   users = relationship("User", back_populates="location")



# class AttendanceHistory(Base):
#   __tablename__ = 'attendance_history'
#   id = Column(Integer, primary_key=True, index=True)
#   # id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE) # for sqlite db
#   # id = Column(GUID, primary_key=True, default=GUID_SERVER_DEFAULT_POSTGRESQL) # for postgres db
#   email = Column(String, nullable=False, index=True)
#   # user_id = Column(GUID, ForeignKey("users.id"))
#   user_id = Column(Integer, ForeignKey("users.id"))
#   # location_id = Column(GUID, ForeignKey("locations.id"))
#   location_id = Column(Integer, ForeignKey("locations.id"), nullable=True)
#   image = Column(String, nullable=True)
#   image_encoding = Column(Text, nullable=True)
#   face_encoding = Column(Text, nullable=True)
#   qr_code = Column(String, nullable=True)
#   qr_code_content = Column(Text, nullable=True)
#   qr_code_b64 = Column(Text, nullable=True)
#   is_signed_in = Column(Boolean, nullable=False, default=False) # for sqlite db
#   is_signed_out = Column(Boolean, nullable=False, default=False) # for sqlite db
#   is_active = Column(Boolean, nullable=False, default=True) # for sqlite db
#   # is_signed_in = Column(Boolean, nullable=False, server_default='False') # for postgres db
#   # is_signed_out = Column(Boolean, nullable=False, server_default='False') # for postgres db
#   # is_active = Column(Boolean, nullable=False, server_default='True') # for postgres db
#   created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
#   updated_at = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())

#   user = relationship("User", back_populates="attendance_history")
#   location = relationship("Location", back_populates="attendance_history")


# class Settings(Base):
#   __tablename__ = 'settings'
#   id = Column(Integer, primary_key=True, index=True)
#   # id = Column(GUID, primary_key=True, index=True, default=GUID_DEFAULT_SQLITE) # for sqlite db
#   # id = Column(GUID, primary_key=True, default=GUID_SERVER_DEFAULT_POSTGRESQL) # for postgres db
#   use_facial_recognition = Column(Boolean, nullable=False, default=True) # for sqlite db
#   use_qr_code = Column(Boolean, nullable=False, default=True) # for sqlite db
#   use_location = Column(Boolean, nullable=False, default=False) # for sqlite db
#   is_active = Column(Boolean, nullable=False, default=True) # for sqlite db
#   opens = Column(String, nullable=True, default="8:00")
#   closes = Column(String, nullable=True, default="16:00")
#   open_days = Column(JSON, nullable=True, default=dumps(["mon", "tue", "wed", "thur", "fri"]))
#   # is_active = Column(Boolean, nullable=False, server_default='True') # for postgres db
#   created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
#   updated_at = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())
