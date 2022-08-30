from flask import Flask, request
import pickle
import json
from flask_cors import CORS, cross_origin

app = Flask (__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return "Index"

@app.route("/classifier", methods=['GET'])
@cross_origin()
def cargar_datos():

    shift = int (request.args.get("shift"))
        
    dict = {}
    dict["Distritos"] = []
    ubicacion = [
    [[ '39.27661605536491', '-77.36178051557392'], [ '39.046618427592755', '-77.19036938063084']], 
    [[ '39.042994904620896', '-77.40015697738'],[ '38.81569437157346', '-77.20445140991414']],
    [['38.93706452409136', '-77.19959243324198'], ['38.74519712307339', '-77.03543774705309']],
    [['39.21493129030198', '-77.1862937034288'], ['39.04875148207457', '-77.0002937034288' ]],
    [['39.047196714867695', '-77.20466382373023'], [ '38.93996891590835', '-76.8909919408635']],
    [['39.320096714867695', '-77.19066382373023'], [ '39.21796891590835', '-76.8909919408635']],
    [['38.817196714867695', '-77.49466382373023'], [ '38.73996891590835', '-77.1999919408635']]
    ]

    with open('Model_clasifier_violence.bin','rb') as file:
        model = pickle.load(file)
        
    for i in range (7):
        isViolent = bool(model.predict([[shift,i]])[0][1]) 
        dict["Distritos"].append(
            {
                'Distrito':'Distrito '+str(i+1),
                "Violento":isViolent,
                'Nombre':'Distrito '+str(i+1),
                'Ubicacion':ubicacion[i]
            }
        )
              
    print(dict)
    return json.dumps(dict)

if __name__== '__main__':
    app.run(debug=True) 
    