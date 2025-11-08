class reportDomain: 
    def __init__(self, name, productId, productQtySold, productUnicPrice, sellerId):
        self.name = name
        self.productId = productId
        self.productQtySold = productQtySold
        self.productUnicPrice = productUnicPrice
        self.sellerId = sellerId
        self.totalSold = (self.productQtySold * self.productUnicPrice) if self.productQtySold and self.productUnicPrice else None


    def to_dict(self):
        return {
            "name": self.name,
            "idProduto": self.productId,
            "qtyProduct":  self.productQtySold,
            "uniquePrice":    self.productUnicPrice,
            "sellerId": self.sellerId

        }