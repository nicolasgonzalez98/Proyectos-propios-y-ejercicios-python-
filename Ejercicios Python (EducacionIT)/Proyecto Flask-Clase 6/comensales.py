from flask import Flask,request,jsonify


comensales = []


app = Flask(__name__)

@app.route("/")
def test():
	return "Error, no se encuentra el servicio",404

@app.route("/restaurant", methods=['GET'])
def mostrar_comensales():
	return jsonify({"restaurant":comensales}),200

@app.route('/restaurant/<int:dato_id>', methods=['GET'])
def get_uno(dato_id):
	try:
		return jsonify(comensales[dato_id]),200
	except:
		return jsonify({"Mensaje":"Error, no se encuentra ese dato","id": dato_id}),404
	
@app.route('/restaurant', methods=['POST'])
def post_comensal():
	# POST request
	body=request.get_json()
	if "name" not in body:
		return jsonify({"Mensaje":"No hay campo nombre"}),400
	if "surname" not in body:
		return jsonify({"Mensaje":"No hay campo apellido"}),400
	comensales.append({"id":len(comensales),"nombre":body["name"],"apellido":body["surname"]})
	return jsonify({"Mensaje":"Agregado", "comensal":body}),201

@app.route('/restaurant/<int:dato_id>', methods=['PUT'])
def cambiar_dato(dato_id):
	dato=request.get_json()
	if "name" in dato:
		comensales[dato_id]["nombre"] = dato["name"]
		return jsonify({"Mensaje":"Modificado", "id":dato_id, "dato":dato}),201
	elif "surname" in dato:
		comensales[dato_id]["apellido"] = dato["surname"]
	return jsonify({"Mensaje":"Modificado", "id":dato_id, "dato":dato}),201	
		
@app.route('/restaurant/<int:dato_id>', methods=['PUT'])
def cambiar_apellido(dato_id):
	dato=request.get_json()
	if "surname" in dato:
		comensales[dato_id]["apellido"] = dato["surname"]
	return jsonify({"Mensaje":"Modificado", "id":dato_id, "dato":dato}),201

@app.route("/restaurant/<int:dato_id>", methods=["DELETE"])
def delete_comensal(dato_id):
	try:
		del comensales[dato_id]
		resize()
		return jsonify({"Mensaje": "Borrado","id":dato_id}), 204
	except:
		return jsonify({"Mensaje": "Error, no se encontro"}), 404

def resize():
	longitud=len(comensales)
	for i in range(longitud):
		comensales[i]['id']=i



app.run()




