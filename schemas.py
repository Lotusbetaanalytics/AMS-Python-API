from datetime import datetime
from typing import List
from pydantic import BaseModel


class BaseAttendanceHistory(BaseModel):
  email: str
  user_id: int
  location_id: int | None = None
  image: str | None = None
  qr_code: str | None = None
  is_active: bool = True

  class Config:
    orm_mode = True
    allow_population_by_field_name = True
    arbitrary_types_allowed = True

class AttendanceHistory(BaseAttendanceHistory):
  id: int | None = None
  # id: str | None = None
  phone: str | None = None
  # image: str | None = None
  image_encoding: str | None = None
  face_encoding: str | None = None
  # qr_code: str | None = None
  qr_code_content: str | None = None
  is_signed_in: bool = False
  is_signed_out: bool = False
  is_active: bool = True
  created_at: datetime | None = None
  updated_at: datetime | None = None


class ListAttendanceHistoryResponse(BaseModel):
  status: str
  count: int
  data: List[AttendanceHistory]


class AttendanceHistoryResponse(BaseModel):
  status: str
  data: AttendanceHistory



class BaseUser(BaseModel):
  first_name: str
  last_name: str
  email: str
  image: str | None = None
  location_id: int | None = None

  class Config:
    orm_mode = True
    allow_population_by_field_name = True
    arbitrary_types_allowed = True


class CreateUser(BaseUser):
  password: str | None = None

class User(BaseUser):
  id: int | None = None
  # id: str | None = None
  hashed_password: str | None = None
  phone: str | None = None
  image_encoding: str | None = None
  face_encoding: str | None = None
  qr_code: str | None = None
  qr_code_content: str | None = None
  is_active: bool = True
  created_at: datetime | None = None
  updated_at: datetime | None = None
  attendance_history: List[AttendanceHistory] | None = []


class ListUserResponse(BaseModel):
  status: str
  count: int
  data: List[User]


class UserResponse(BaseModel):
  status: str
  data: User
  b64_qr_code: str | None = None


class UserLogin(BaseModel):
  email: str
  password: str



class BaseLocation(BaseModel):
  name: str
  address: str
  description: str | None = None
  phone: str | None = None
  is_active: bool = True

  class Config:
    orm_mode = True
    allow_population_by_field_name = True
    arbitrary_types_allowed = True


class Location(BaseLocation):
  id: int | None = None
  # id: str | None = None
  created_at: datetime | None = None
  updated_at: datetime | None = None
  attendance_history: List[AttendanceHistory] | None = []
  # users: User | None = None
  users: List[User] | None = []


class ListLocationResponse(BaseModel):
  status: str
  count: int
  data: List[Location]


class LocationResponse(BaseModel):
  status: str
  data: Location
