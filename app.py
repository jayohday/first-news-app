import csv
from flask import abort
from flask import Flask 
from flask import render_template
app = Flask(__name__)


def get_csv():
	csv_path = "static/la-riots-deaths.csv" 
	# telling it where the csv file is
	csv_file = open(csv_path, 'rb')
	# opening and reading the csv
	csv_obj = csv.DictReader(csv_file)
	# made a list of dictionaries
	csv_list = list(csv_obj)
	# gets list for iteration
	return csv_list


@app.route('/')
def index():
	template = "index.html"
	object_list = get_csv()
	return render_template(template, object_list=object_list)
	#returns index, data to function

@app.route('/<row_id>/')
def detail(row_id):
	template = "detail.html"
	object_list = get_csv()
	for row in object_list:
		if row["id"] == row_id:
		#if row in csv is same as row id (matches) then run the code
			return render_template(template, object=row)
	abort(404)

# If this script is run from the command line
if __name__ == "__main__":
	# firing up Flask test server
	app.run(debug=True, use_reloader=True)

