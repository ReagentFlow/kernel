from scanner import barcode_scanner
from scales import getting_weight
from fire_db import FireDataBase
from models import Container, ContainerData
from constants import KEY, COLLECTION


def _updating() -> None:
    data = ContainerData(name=str(key), weight=weight, barcode_id=key, container_id=0, density=0)
    containter = Container(key=key, data=data)
    database.update(COLLECTION, containter)


def _creating() -> None:
    containter_id = len(database.list(collection=COLLECTION)) + 1
    data = ContainerData(name=str(key), weight=weight, barcode_id=key, container_id=containter_id,
                         density=0)
    containter = Container(key=key, data=data)
    database.create(COLLECTION, containter)


if __name__ == "__main__":
    database = FireDataBase(KEY)
    while True:
        key = barcode_scanner()
        if key:
            weight = getting_weight()

            if database.get(str(key), COLLECTION):
                _updating()
                print('update')
            else:
                _creating()
                print('create')
        else:
            raise Exception("Error with scanning bar code")
