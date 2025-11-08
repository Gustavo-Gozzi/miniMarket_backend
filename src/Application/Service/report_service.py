from src.Config.db import db
from src.Infrastructure.Model.Product_model import ReportModel
from src.Infrastructure.Model.Product_model import ProductModel
from src.Domain.Product import reportDomain
from datetime import date


class ReportService:
    @staticmethod
    def gerar_relatorio(data, idProduto):
        pass


    @staticmethod
    def pegar_registros_produtos(data, idProduto):

        try:
            ProductModel.query.filter(
                ReportModel.product_id == idProduto,
                ReportModel.sales_date == date(2025, 11, 8)
            ).all()
