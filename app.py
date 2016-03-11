from flask import Flask
# this is telling it to go to folder flask and import tool Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
	template = "index.html"
	return render_template(template)

if __name__ == "__main__":
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
    # If this thing is being booted up from the terminal, run this thing.
    # This will give us a barebones web server to work with.
    # The colon is super important!