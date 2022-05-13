# Dependencies: Flask
# (pip install Flask)

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'my_store',
        'items': [
            {
                'name': 'chocolate',
                'price': 120
            }
        ]
    }
]

@app.route('/stores/<string:name>')
def get_store(name):

    print("INPUT " + name)

    for store in stores:
        if store["name"] == name:
            return jsonify(store)

    return jsonify({"message": "no store named {} found".format(name)})

app.run(port=8000)
