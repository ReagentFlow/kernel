from datetime import datetime
from typing import NamedTuple
from pydantic import BaseModel
from enum import Enum


class StatusExpiration(Enum):
    FEW = 'RED'
    ORDER = 'YELLOW'
    MANY = 'GREEN'


class ContainerData(BaseModel):
    barcode_id: int
    container_id: int
    density: int
    name: str
    weight: int
    date: datetime


class Container(NamedTuple):
    key: int
    data: ContainerData
