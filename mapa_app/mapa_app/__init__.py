from flask import Flask, render_template, abort
app = Flask(__name__)

class Places:
    def __init__(self, key, name, lat, lng):
        self.key = key
        self.name = name
        self.lat = lat
        self.lng = lng

places = (
    Places('eafit', 'EAFIT University', 6.1995533,-75.5815287),
    Places('oviedo', 'Mall Oviedo', 6.1992862,-75.5773183),
    Places('santa-fe', 'Mall Santa Fe', 6.1957749,-75.5758811),
    Places('poli', 'Politecnico Jaime Isaza Cadavid', 6.211742,-75.5791694),
    Places('lleras', 'Lleras park', 6.2089867,-75.5701454),
    Places('tesoro', 'Mall El tesoro', 6.1976386,-75.5610185)
)

places_by_key = {place.key: place for place in places}

@app.route("/")
def index():
    return render_template('index.html', places=places)

@app.route("/<place_code>")
def show_place(place_code):
    place = places_by_key.get(place_code)
    if place:
        return render_template('map.html', place=place)
    else:
        abort(404)
if __name__ == "__main__":
    app.run(debug=True)
