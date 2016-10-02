from flask import Blueprint, abort
from flask_restful import Api, Resource
from genecardapi.db import db


idmapping_api = Blueprint('ensembl2geneid', __name__, url_prefix='/idMapping')
api_wrap = Api(idmapping_api)


class Ensembl2GeneidMapping(Resource):
    def get(self, ensembl_id):
        result = db.ensembl2geneid.find_one({'ensemblID': ensembl_id})
        if not result:
            return ('', 204)
        return {
            'ensemblID': ensembl_id,
            'geneID': result['geneID']
        }


class Ensembl2GeneidMappings(Resource):
    def get(self, ensembl_ids):
        eids = ensembl_ids.split(',')
        records = [db.ensembl2geneid.find_one({'ensemblID': x}) for x in eids]
        result = filter(lambda x: x is not None, records)
        return [{
            'ensemblID': x['ensemblID'],
            'geneID': x['geneID']
            } for x in result]


api_wrap.add_resource(Ensembl2GeneidMapping, '/ensembl2geneid/<ensembl_id>')
api_wrap.add_resource(Ensembl2GeneidMappings, '/ensembl2geneids/<ensembl_ids>')