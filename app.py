import csv
from flask import Flask
from flask import abort
# this is telling it to go to folder flask and import tool Flask
from flask import render_template
app = Flask(__name__)

def fetch_csv(csv_path):
	csv_file = open(csv_path, "rb")
	csv_obj = csv.DictReader(csv_file)
		# returns a dictionary (headers)
	csv_list = list(csv_obj)
	return csv_list


@app.route("/")
def index():
	template = "index.html"
	object_list = fetch_csv("./static/la-riots-deaths.csv")
		#the list of data returned by the csv
	return render_template(template, object_list=object_list)

@app.route("/<row_id>/")
def detail(row_id):
	template = 'detail.html'
	object_list = fetch_csv("./static/la-riots-deaths.csv")
	for row in object_list: 
		if row['id'] == row_id:
			return render_template(template, object=row)
	abort(404)

if __name__ == "__main__":
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
    # If this thing is being booted up from the terminal, run this thing.
    # This will give us a barebones web server to work with.
    # The colon is super important!