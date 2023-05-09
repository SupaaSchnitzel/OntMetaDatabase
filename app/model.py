from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql

db = SQLAlchemy()

#Ontology Model Sqlalchemy
class Ontology(db.Model):
    ''' Sqlalchemy Model for the Ontology database
    '''
    __tablename__ = 'ontology'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    languages = db.Column(postgresql.ARRAY(db.String()))
    ont_languages = db.Column(db.String())
    sourcecode = db.Column(db.String())
    access = db.Column(db.String())
    license = db.Column(db.String())
    used_upper = db.Column(db.String())
    funding = db.Column(postgresql.ARRAY(db.String()))
    gov_inst = db.Column(db.String())
    maintenance = db.Column(db.String())
    release = db.Column(db.String())
    citations = db.Column(db.Integer())
    scope = db.Column(db.String())
    desc_size = db.Column(db.String())
    desc_quality = db.Column(db.String())
    no_terms = db.Column(postgresql.ARRAY(db.String()))
    used_ont = db.Column(postgresql.ARRAY(db.String()))
    creation = db.Column(db.String())
    analysis = db.Column(db.String())
    modularity = db.Column(db.String())
    extensability = db.Column(db.String())
    validation = db.Column(db.String())
    ac_score = db.Column(db.Float())
    gov_score = db.Column(db.Float())
    bp_score = db.Column(db.Float())
    pi_score = db.Column(db.Float())

    def __repr__(self):
        return f"<Ontology {self.name}>"
    
