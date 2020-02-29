import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for the catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'Name of the Wind',
     'author': 'Patrick Rothfuss',
     'year_published': '2007'},
    {'id': 1,
     'title': 'Way of Kings',
     'author': 'Brandon Sanderson',
     'published': '2010'},
    {'id': 2,
     'title': 'Dune',
     'author': 'Frank Herbert',
     'published': '1965'},
    {'id': 3,
     'title': 'nyeah',
     'author': 'eh',
     'published': '2019'}
]

# Main web page
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for getting data about Fantasy books.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args :
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()