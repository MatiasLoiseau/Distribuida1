from suds.client import Client as SudsClient

url = 'http://127.0.0.1:5000/soap/someservice?wsdl'
client = SudsClient(url=url, cache=None)


r = client.service.agregarEstudiante(dni=123456789, legajo=3, nombreEst='pepe')
print r

o = client.service.obtenerEstudiante(dni=123456789)
print o

#r = client.service.echo(str='hello world', cnt=3)
#print r
