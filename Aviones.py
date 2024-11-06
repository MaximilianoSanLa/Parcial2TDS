import PIL.Image
from flask import Flask, render_template,request
import PIL
vuelos=[[1,"Avianca","Nacional","3000 COP"],[2,"Copa","Internacional","3324000 COP"],[6,"American Airlines","Internacional","33000 COP"],[24,"VuelosAlgo","Nacional","4000 COP"],[120,"VuelosNorte","Nacional","100000 COP"]]
app = Flask(__name__)

@app.route('/')
def Aviones():
    lugar=1
    idAvion = request.args.get('idAvion')
    if(idAvion==None or idAvion==""):
        return render_template("notfound.html")
    idAvion= int(idAvion)
    if(idAvion==0):
        lugar=0
    for i in range(1,idAvion+1):
        lugar=lugar*i
    encontrado=False
    for i in vuelos:
        if(i[0]==lugar):
            nombre=i[1]
            tipo=i[2]
            precio=i[3]
            encontrado=True
    if(encontrado==False):
        return render_template("notfound.html")

    return render_template("aviones.html",idAvion=idAvion,precio=precio,nombre=nombre,tipo=tipo)

if __name__ == '__main__':
    app.run()