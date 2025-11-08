from src.Config.db import db 

class ReportModel(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    productQtySold = db.Column(db.Integer, nullable=False)
    productUnicPrice = db.Column(db.Float(5,2), nullable=False)
    totalSold = db.Column(db.Integer, nullable=False)
    reportDate = db.Column(db.Date, nullable=False)
    
    id_seller = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    seller = db.relationship("UserModel", backref="reports") 

    productId = db.Column(db.String(100), db.ForeignKey('produtos.id'), nullable=False)
    product = db.relationship("UserModel", backref="reports") 


    def to_dict(self):
        return {
            "name": self.name,
            "idProduto": self.productId,
            "qtyProduct":  self.productQtySold,
            "uniquePrice":    self.productUnicPrice,
            "sellerId": self.id_seller

        }