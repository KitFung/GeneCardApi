from flask import Blueprint, abort
from flask_restful import Api, Resource
from genecardapi.db import db


ensembl2geneid_api = Blueprint('ensembl2geneid', __name__, url_prefix='/ensembl2geneid')
api_wrap = Api(ensembl2geneid_api)


class Ensembl2GeneidMapping(Resource):
    def get(self, ensembl_id):
        result = db.ensembl2geneid.find_one({'ensemblID': ensembl_id})
        if not result:
            return ('', 204)
        return {
            'ensembl_id': ensembl_id,
            'geneid': result['geneID']
        }


api_wrap.add_resource(Ensembl2GeneidMapping, '/<ensembl_id>')
