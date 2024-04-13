from scanner.scanner import barcode_scanner
from scales.scales_main import getting_weight
from fire_db.fire_db import FireDataBase
import uuid
from firebase_admin import credentials, firestore

from model import StatusExperation, Container, ContainerData
from src.constants import KEY, COLLECTION

if __name__ == "__main__":
    fire_db = FireDataBase(KEY)
    while (True):
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
                '''
                docs = fire_db.get(collection=COLLECTION)
                len_of_db = len(docs)+1
                data = ContainerData(name=str(key), weight=weight, barcode_id=key, container_id=len_of_db, density=0)
                containter = Container(key=key, data=data)
                '''
                fire_db.create(COLLECTION, containter)
        else:
            raise Exception("Error with scanning bar code")
