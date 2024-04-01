from fire_db.connection import get_ref
from model import Container


def create(container: Container):
    ref = get_ref(container.key)
    print(container.data.model_dump(mode='json'))
    ref.set(container.data.model_dump(mode='json'))


def update():
    pass


def get():
    ref = get_ref()
    return ref.get()


def delete():
    pass
