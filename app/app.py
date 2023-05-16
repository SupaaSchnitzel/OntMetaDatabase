from flask import Flask, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from webargs import fields
from webargs.flaskparser import use_args, parser, abort
from model import db, Ontology
from flask_cors import CORS, cross_origin
from flask_swagger_ui import get_swaggerui_blueprint


#Database Information
UNAME = 'postgres'
PWD = 'postgres'
HOST = 'db'
PORT =  '5432'
DBNAME = 'postgres'
#INIT FLASK
app = Flask(__name__)
#INIT SQLALchemy
app.config['SQLALCHEMY_DATABASE_URI'] =f"postgresql://{UNAME}:{PWD}@{HOST}:{PORT}/{DBNAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#INIT SWAGGERUI
swaggerui_blueprint = get_swaggerui_blueprint(
    '/api/v1/docs',
    '/static/swagger.json',
    config={
        'app_name': "OntMetaDatabase"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix='/api/v1/docs')
#Init apu, database and cors
api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

    

def init_database(self):
    """Initializes the empty database

    """
    db.create_all()

#Marshmallow Arguments    
user_args = {
    "id": fields.Int(metadata={'location':'query'}),
    "name": fields.Str(metadata={'location':'query'}),
    "languages": fields.List(fields.Str(), metadata={'location':'query'}),
    "ont_languages": fields.Str(metadata={'location':'query'}),
    "sourcecode": fields.Str(metadata={'location':'query'}),
    "access": fields.Str(metadata={'location':'query'}),
    "license": fields.Str(metadata={'location':'query'}),
    "used_upper": fields.Str(metadata={'location':'query'}),
    "funding": fields.List(fields.Str(), metadata={'location':'query'}),
    "gov_inst": fields.Str(metadata={'location':'query'}),
    "maintenance": fields.Str(metadata={'location':'query'}),
    "release": fields.Str(metadata={'location':'query'}),
    "citations": fields.Int(metadata={'location':'query'}),
    "scope": fields.Str(metadata={'location':'query'}),
    "desc_size": fields.Str(metadata={'location':'query'}),
    "desc_quality": fields.Str(metadata={'location':'query'}),
    "no_terms": fields.List(fields.Str(), metadata={'location':'query'}),
    "used_ont": fields.List(fields.Str(), metadata={'location':'query'}),
    "creation": fields.Str(metadata={'location':'query'}),
    "analysis": fields.Str(metadata={'location':'query'}),
    "modularity": fields.Str(metadata={'location':'query'}),
    "extensability": fields.Str(metadata={'location':'query'}),
    "validation": fields.Str(metadata={'location':'query'}),
    "ac_score": fields.Float(metadata={'location':'query'}),
    "gov_score": fields.Float(metadata={'location':'query'}),
    "bp_score": fields.Float(metadata={'location':'query'}),
    "pi_score": fields.Float(metadata={'location':'query'}),
}
user_args_2 = {"name": fields.List(fields.Str(), metadata={'location':'query'}),}

#Dict needed for queries
ontbib = {
    'name': Ontology.name,
    'languages': Ontology.languages,
    'ont_languages':Ontology.ont_languages,
    'sourcecode':Ontology.sourcecode,
    'access':Ontology.access,
    'license':Ontology.license,
    'used_upper':Ontology.used_upper,
    'funding':Ontology.funding,
    'gov_inst':Ontology.gov_inst,
    'maintenance':Ontology.maintenance,
    'release':Ontology.release,
    'citations':Ontology.citations,
    'scope':Ontology.scope,
    'desc_size':Ontology.desc_size,
    'desc_quality':Ontology.desc_quality,
    'no_terms':Ontology.no_terms,
    'used_ont':Ontology.used_ont,
    'creation':Ontology.creation,
    'analysis':Ontology.analysis,
    'modularity':Ontology.modularity,
    'extensability':Ontology.extensability,
    'validation':Ontology.validation,
    'ac_score':Ontology.ac_score,
    'gov_score':Ontology.gov_score,
    'bp_score':Ontology.bp_score,
    'pi_score':Ontology.pi_score,
}
#list needed for queries
ontlists = ["languages","funding","no_terms","used_ont",]

#flask restfull for ontologies
class Ont(Resource):
    """
    Flask class for the ont endpoint
    """

    def results(self, ontologies):
        """
        Helper function that aggregates the results

        Parameters:
        ----------
        ontologies
            A list of ontologies that are to be returned
        """
        results = [
                {
                    "name": ont.name,
                    "languages": ont.languages,
                    "ont_languages": ont.ont_languages,
                    "sourcecode": ont.sourcecode,
                    "access": ont.access,
                    "license": ont.license,
                    "used_upper": ont.used_upper,
                    "funding": ont.funding,
                    "gov_inst": ont.gov_inst,
                    "maintenance": ont.maintenance,
                    "release": ont.release,
                    "citations": ont.citations,
                    "scope": ont.scope,
                    "desc_size": ont.desc_size,
                    "desc_quality": ont.desc_quality,
                    "no_terms": ont.no_terms,
                    "used_ont": ont.used_ont,
                    "creation": ont.creation,
                    "analysis": ont.analysis,
                    "modularity": ont.modularity,
                    "extensability": ont.extensability,
                    "validation": ont.validation,
                    "ac_score": ont.ac_score,
                    "gov_score": ont.gov_score,
                    "bp_score": ont.bp_score,
                    "pi_score": ont.pi_score
                } for ont in ontologies]
        return {"count": len(results), "onts": results}

    @use_args(user_args, location='querystring')
    def get(self, args):
        """
        Get function of the endpoint

        Parameters:
        ----------
        args
            A list of arguments to be parsed
        """
        if 'id' in args.keys():
            onts = [Ontology.query.get(args['id']).one()]
        elif args:
            for i, arg in enumerate(args):
                if args[arg] != "":
                    if i == 0:
                        if arg in ontlists:
                            onts =  Ontology.query.filter(ontbib[arg].contains(args[arg]))
                        else:
                            onts =  Ontology.query.filter(ontbib[arg]==args[arg])
                    else:
                        if arg in ontlists:
                            onts =  onts.filter(ontbib[arg].contains(args[arg]))
                        else:
                            onts = onts.filter(ontbib[arg]==args[arg])
            onts = onts.all()
        else: 
            onts = Ontology.query.all()
        return self.results(onts)
    
    def post(self):
        """
        Post function of the endpoint

        Parameters:
        ----------
        args
            A list of arguments to be parsed
        """
        if request.is_json:
            data = request.get_json()
            new_ont = Ontology(name=data['name'], languages = data['languages'], ont_languages= data['ont_languages'],sourcecode= data['sourcecode'], access= data['access'], license= data['license'],
                  used_upper= data['used_upper'], funding= data['funding'], gov_inst= data['gov_inst'],maintenance= data['maintenance'], release= data['release'], citations= data['citations'],
                  scope= data['scope'], desc_size= data['desc_size'], desc_quality= data['desc_quality'],no_terms= data['no_terms'], used_ont= data['used_ont'], creation= data['creation'], analysis= data['analysis'],
                  modularity= data['modularity'], extensability= data['extensability'], validation= data['validation'],ac_score= data['ac_score'],gov_score= data['gov_score'],
                  bp_score= data['bp_score'], pi_score= data['pi_score'])
            db.session.add(new_ont)
            db.session.commit()
            return {"message": f"ont {new_ont.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
    
    @use_args(user_args, location='querystring')    
    def delete(self, args):
        """
        Delete Function of the endpoint
        
        Parameters:
        ----------
        args
            A list of arguments to be parsed
        """
        if args['id']:
            Ontology.query.filter_by(id=args['id']).delete()
            db.session.commit()
            return {"message": f"ont {args['id']} has been deleted successfully."}
        else:
            return {"message": f"ont {args['id']} invalid or missing"}
        
class Names(Resource):
    """
        Flask class for the names endpoint

    """

    def results(self, ontologies):
        """
        Helper function that aggregates the results as a json

        Parameters:
        ----------
        ontologies
            A list of ontologies to be returned
        """
        results = [ont.name for ont in ontologies]
        return {"count": len(results), "onts": results}

    @use_args(user_args, location='querystring')
    def get(self, args):
        """
        Get function of the endpoint

        Returns:
            _type_: _description_
        """
        if 'id' in args.keys():
            id =args['id']
            onts = [Ontology.query.filter_by(id=id).one()]
        elif args:
            for i, arg in enumerate(args):
                if args[arg] != "":
                    if i == 0:
                        if arg in ontlists:
                            onts =  Ontology.query.filter(ontbib[arg].contains(args[arg]))
                        else:
                            onts =  Ontology.query.filter(ontbib[arg]==args[arg])
                    else:
                        if arg in ontlists:
                            onts =  onts.filter(ontbib[arg].contains(args[arg]))
                        else:
                            onts = onts.filter(ontbib[arg]==args[arg])
            onts = onts.all()
        else: 
            onts = Ontology.query.all()
        return self.results(onts)
    
    

class Possible(Resource):
    """
    Flask class for the possible Endpoint

    Returns:
        _type_: _description_
    """
    def update_dict(self,dict,key,value):
        """Helper function that updates a dictionary

        Parameters:
            dict (_type_): Dictionary to be updated
            key (_type_): Key to do the update on
            value (_type_): Value for the key
        """
        if key in dict:
            if isinstance(value,list):
                dict[key]+=(value)
            else:
                dict[key].append(value)
        else:
            if isinstance(value,list):
                dict[key] = value
            else:
                dict[key] = [value]
        dict[key] = list( dict.fromkeys(dict[key]))

    def process(self, ontologies, ret):
        """Helper function

        Args:
            ontologies (_type_): _description_
            ret (_type_): _description_
        """
        for ont in ontologies:
            self.update_dict(ret, 'languages', ont.languages)
            self.update_dict(ret, 'ont_languages', ont.ont_languages)
            self.update_dict(ret, 'sourcecode', ont.sourcecode)
            self.update_dict(ret, 'access', ont.access)
            self.update_dict(ret, 'license', ont.license)
            self.update_dict(ret, 'used_upper', ont.used_upper)
            self.update_dict(ret, 'funding', ont.funding)
            self.update_dict(ret, 'gov_inst', ont.gov_inst)
            self.update_dict(ret, 'maintenance', ont.maintenance)
            self.update_dict(ret, 'release', ont.release)
            self.update_dict(ret, 'citations', ont.citations)
            self.update_dict(ret, 'scope', ont.scope)
            self.update_dict(ret, 'desc_size', ont.desc_size)
            self.update_dict(ret, 'desc_quality', ont.desc_quality)
            self.update_dict(ret, 'no_terms', ont.no_terms)
            self.update_dict(ret, 'used_ont', ont.used_ont)
            self.update_dict(ret, 'creation', ont.creation)
            self.update_dict(ret, 'analysis', ont.analysis)
            self.update_dict(ret, 'modularity', ont.modularity)
            self.update_dict(ret, 'extensability', ont.extensability)
            self.update_dict(ret, 'validation', ont.validation)
            self.update_dict(ret, 'ac_score', ont.ac_score)
            self.update_dict(ret, 'gov_score', ont.gov_score)
            self.update_dict(ret, 'bp_score', ont.bp_score)
            self.update_dict(ret, 'pi_score', ont.pi_score)

    @cross_origin()
    @use_args(user_args_2, location='querystring')
    def get(self, args):
        """Get Function of the Endpoint

        Args:
            args (_type_): _description_

        Returns:
            _type_: _description_
        """
        ret={}
        if args:
            
            for i, arg in enumerate(args):
                if args[arg] != "": 
                    for name in args[arg]:
                        ontologies = Ontology.query.filter(ontbib[arg]==name).all()
                        self.process(ontologies, ret)
        else:
            ontologies = Ontology.query.all()
            self.process(ontologies, ret)
        return [ret]
    
    def post(self):
        return {"error": "The post request is not possible at this endpoint"}
    
    def delete(self, args):
        return {"error": "The delete request is not possible at this endpoint"}


#Add endpoints
api.add_resource(Ont, '/ont/')
api.add_resource(Names, '/names/')
api.add_resource(Possible, '/possible/')


@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    """
    webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.

    """
    abort(error_status_code, errors=err.messages)  

if __name__ == '__main__':
    with app.app_context():
        print('Creating DB')
        db.create_all()
        print('Created')