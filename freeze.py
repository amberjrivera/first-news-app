from flask_frozen import Freezer
from app import app, fetch_csv
freezer = Freezer(app)

@freezer.register_generator
def detail():
    for row in fetch_csv("./static/la-riots-deaths.csv"):
        yield {'row_id': row['id']}

if __name__ == '__main__':
    freezer.freeze()