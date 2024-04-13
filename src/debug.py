from fire_db.fire_db import FireDataBase
from models import Container, ContainerData
from constants import KEY, COLLECTION

if __name__ == "__main__":
    fire_db = FireDataBase(KEY)
    docs = fire_db.list(collection=COLLECTION)
    key = 'none'
    container_id = len(docs)+1
    data = ContainerData(name=str(key), weight=weight, barcode_id=key, container_id=len_of_db, density=0)
    containter = Container(key=key, data=data)
    #fire_db.create(COLLECTION, containter)
