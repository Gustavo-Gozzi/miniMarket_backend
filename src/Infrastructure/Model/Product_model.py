from src.Config.db import db 

class ProductModel(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), nullable=False, default='Ativo')
    
    id_seller = db.Column(db.Integer, nullable=False)
    item = db.relationship("usuarios", backref="produtos")  

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "status": self.status,
            "id_seller": self.id_seller
        }