"""                                                                                                                   Simple REST API in Python
"""

__author__     = "Jan Kogut"
__copyright__  = "Jan Kogut"
__license__    = "MIT"
__version__    = "0.0.1"
__maintainer__ = "Jan Kogut"
__status__     = "Beta"


from flask import Flask, request, jsonify, abort
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import simplejson as json

#####################
app = Flask(__name__)

engine = create_engine('mysql://root:password@mariadb-service/titanic', echo=True)
Base = declarative_base(engine)


class Titanic(Base):
    """ Titanic Base object """
    
    __tablename__ = 'titanic'
    __table_args__ = {'autoload':True}


## Initialise session    
def loadSession():
    """
    ---> Init session for given Base 
    <--- Return session
    """
    
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


## API STATUS
@app.route("/api/status", methods = ['GET'])
def getStatus():
    """
    ---> Check API Status
    <--- Return JSON with API_status
    """
    
    result = {'API_status':'OK'}
    return jsonify(result)


## GET passengers
@app.route("/api/v1/passengers", methods = ['GET'])
def getPassengers():
    """
    ---> Select all passengers
    <--- Return JSON with passengerId and Name
    """

    result = dict(session.query(Titanic.Name,Titanic.Id).all())
    return jsonify(result)


## GET survivedStatus
@app.route("/api/v1/passengers/survived/<int:survivedStatus>", methods = ['GET'])
def getSurvivedStatus(survivedStatus):
    """
    ---> Select survived passengers depending on status 0 or 1
    <--- Return encoded list as a JSON payload with passengers data
    """

    filterQuery = session.query(Titanic).filter(Titanic.Survived==survivedStatus).all()
    survivedList = []
    for i in filterQuery:
        survivedList.append({ x: getattr(i, x) for x in Titanic.__table__.columns.keys() })

    # using json.dumps from simplejson to fix
    # TypeError: Decimal('22.00') is not JSON serializable 
    return json.dumps(survivedList)


## POST add new passenger
@app.route("/api/v1/passengers/new", methods = ['POST'])
def insertNewPassenger():
    """
    ---> Add new passenger from JSON payload
    <--- Return added JSON payload with response code 
    """

    payload = request.json
    if not payload or not 'Name' in payload:
        abort(400)

    newPass = Titanic(**payload)
    session.add(newPass)
    session.flush()
    session.commit()  
    return jsonify(payload),201


## PUT 
@app.route("/api/v1/passengers/update/<int:passengerId>", methods = ['PUT'])
def updatePassenger(passengerId):
    """
    ---> Update data of existing passenger
    <--- Return updated JSON payload with response code
    """
    pass

## DELETE
@app.route("/api/v1/passengers/delete/<int:passengerId>", methods = ['DELETE'])
def deletePasseneger(passengerId):
    """
    ---> Delete existing passenger
    <--- Return deleted response code 
    """

    if len(session.query(Titanic).filter(Titanic.Id==passengerId).all()) == 0:
        result = {passengerId:"NOT EXISTS"}
        return jsonify(result),400
    
    delQuery = session.query(Titanic).filter(Titanic.Id==passengerId)
    delQuery.delete()
    delQuery.session.commit()
    result = {passengerId:"DELETED"}
    return jsonify(result),200

if __name__ == "__main__":
    session = loadSession()
    app.run(host="0.0.0.0", port=int("5002"), debug=True)
