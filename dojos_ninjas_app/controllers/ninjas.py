from crypt import methods
from dojos_ninjas_app import app
from dojos_ninjas_app.models.ninja import Ninja
from dojos_ninjas_app.models.dojo import Dojo
from flask import render_template, redirect, request

@app.route("/ninjas")
def formulario_ninja():
    todos_dojos = Dojo.todos_dojos()
    return render_template('ninjas.html', todos_dojos=todos_dojos)


@app.route("/crearninja", methods=['POST'])
def crearninja():
    id_ninja = Ninja.crearninja(request.form)
    data = {
        "id":id_ninja
    }
    un_ninja = Ninja.obtener_un_ninja(data)
    print(un_ninja, "QUE CONTIENE LA VARIABLE un_ninja ?")
    return redirect(f'/dojos/{un_ninja.dojo_id}')