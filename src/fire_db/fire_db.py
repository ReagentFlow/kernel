import firebase_admin
from firebase_admin import credentials, firestore
from src.models import Container


class FireDataBase:
    def __init__(self, file: str):
        self.cred = credentials.Certificate(file)
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def create(self, collection: str, container: Container):
        doc = self.db.collection(f"{collection}").document(f"{container[0]}")
        doc.set(container[1].model_dump(mode="json"))

    def update(self, collection: str, container: Container):
        doc_ref = self.db.collection(f"{collection}").document(f"{container[0]}")
        data = container[1].model_dump(exclude={'name', 'container_id', 'date'})
        doc_ref.update(data)

    def get(self, id: str, collection: str = "/"):
        doc_ref = self.db.collection(f'{collection}').document(id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
            #print(doc.id, doc.get('name'), doc.to_dict())
        return None

    def list(self, collection: str):
        doc_ref = self.db.collection(f'{collection}')
        return doc_ref.get()

    def delete(self):
        pass

    def existed(self, container: Container):
        return self.db.collection(f"")
