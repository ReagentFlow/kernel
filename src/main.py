from scanner import barcode_scanner
from scales import getting_weight
from fire_db import FireDataBase
from models import Container, ContainerData
from constants import KEY, COLLECTION


if __name__ == "__main__":
    database = FireDataBase(KEY)
    while True:
        key = barcode_scanner()
        if key:
            weight = getting_weight()
            data = ContainerData(name=str(key), weight=weight, barcode_id=key, container_id=0, density=0)
            container = Container(key=key, data=data)
            doc = database.get(str(key), COLLECTION)
            if doc:
                database.update(COLLECTION, container)
                print('update')
            else:
                container_id = len(database.list(collection=COLLECTION)) + 1
                data = ContainerData(name=str(key), weight=weight, barcode_id=key, container_id=container_id,
                                     density=0)
                container = Container(key=key, data=data)
                database.create(COLLECTION, container)
                print('create')
        else:
            print("Видимо вы считали QR код, а не штрих код!")
