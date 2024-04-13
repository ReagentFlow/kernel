from scanner import barcode_scanner
from scales import getting_weight
from fire_db import FireDataBase
import uuid
from firebase_admin import credentials, firestore

from models import Container, ContainerData
from constants import KEY, COLLECTION

if __name__ == "__main__":
    fire_db = FireDataBase(KEY)
    while True:
        key = barcode_scanner()
        print(key)
        if key:
            weight = getting_weight()
            data = ContainerData(name=str(key), weight=weight, barcode_id=key, container_id=0, density=0)
            containter = Container(key=key, data=data)
            doc = fire_db.get(str(key), COLLECTION)
            if doc:
                fire_db.update(COLLECTION, containter)
            else:
                containter_id = len(fire_db.list(collection=COLLECTION))+1
                data = ContainerData(name=str(key), weight=weight, barcode_id=key, container_id=containter_id, density=0)
                containter = Container(key=key, data=data)
                fire_db.create(COLLECTION, containter)
        else:
            raise Exception("Error with scanning bar code")
