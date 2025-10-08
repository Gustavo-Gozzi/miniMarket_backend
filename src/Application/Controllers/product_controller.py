from flask import request, jsonify, make_response
from src.Application.Service.product_service import ProductService
from datetime import timedelta
import re

class ProductController:
    @staticmethod
    def register_user():
        try:
            data = request.get_json()
            
            if not data:
                return make_response(jsonify({"erro": "Dados JSON são obrigatórios"}), 400)
            
            dados_obrigatorios = ["name", "price", "quantity", "id_seller"]
            info_faltantes = [item for item in dados_obrigatorios if item not in data]
            
            if info_faltantes:
                return make_response(
                    jsonify({"erro": f"Estão faltando os seguintes campos: {info_faltantes}"}), 
                    400
                )
            
            result, status_code = ProductService.create_user(**data)
            
            if status_code != 201:
                return make_response(jsonify(result), status_code)
            
            return make_response(jsonify({
                "mensagem": "Produto criado com sucesso",
                "produto": result.to_dict()
            }), 201)
            
        except Exception as e:
            return make_response(jsonify({"erro": "Erro interno do servidor"}), 500)
    
    @staticmethod
    def get_user(user_id):
        """Busca usuário por ID"""
        try:
            result, status_code = UserService.get_user_by_id(user_id)
            return make_response(jsonify(result), status_code)
        except Exception as e:
            return make_response(jsonify({"erro": "Erro interno do servidor"}), 500)
    
    @staticmethod
    def update_user(user_id):
        try:
            data = request.get_json()
            
            if not data:
                return make_response(jsonify({"erro": "Dados JSON são obrigatórios"}), 400)
            
            result, status_code = UserService.update_user(user_id, **data)
            return make_response(jsonify(result), status_code)
            
        except Exception as e:
            return make_response(jsonify({"erro": "Erro interno do servidor"}), 500)
    
    @staticmethod
    def delete_user(user_id):
        try:
            result, status_code = UserService.delete_user(user_id)
            return make_response(jsonify(result), status_code)
        except Exception as e:
            return make_response(jsonify({"erro": "Erro interno do servidor"}), 500)