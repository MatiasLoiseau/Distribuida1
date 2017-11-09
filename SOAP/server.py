from flask import Flask
from flask_spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable
from sqlalchemy import Integer as SQLInteger
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
spyne = Spyne(app)

engine = create_engine('sqlite:///testDB.db')

Base = declarative_base()

class Estudiante(Base):
    __tablename__ = 'estudiante'
    dni = Column(SQLInteger, primary_key=True)
    legajo = Column(SQLInteger)
    nombre = Column(String)

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
session = session()

class SomeSoapService(spyne.Service):
    __service_url_path__ = '/soap/someservice'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    @spyne.srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def echo(str, cnt):
        for i in range(cnt):
            yield str

    @spyne.srpc(Integer, Integer, Unicode)
    def agregarEstudiante(dni, legajo, nombreEst):
		est = Estudiante(dni=dni, legajo=legajo, nombre=nombreEst)
		session.add(est)
		session.commit()

    @spyne.srpc(Integer, _returns=Iterable(Unicode))
    def obtenerEstudiante(dni):
    	estudiante = session.query(Estudiante).all();
    	for x in estudiante:
    		print x.dni
    		print x.legajo
    		print x.nombre
    	session.commit()
    		

if __name__ == '__main__':
    app.run(host = '127.0.0.1')