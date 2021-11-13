from app.models import Data
from app.db import Session, Base, engine
import csv


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

with open("example_batch_records.csv", 'r') as fileName:
    reader = csv.reader(fileName, delimiter=",")
    for row in reader:
        batch_number_in = row[0]
        submitted_at_in = row[1]
        nodes_used_in = row[2]
        # print(batch_number, submitted_at, nodes_used)
        db.add_all([
            Data(batch_number=batch_number_in, submitted_at=submitted_at_in, nodes_used=nodes_used_in)
        ])



# db.add_all([
#     Data(batch_number=1, submitted_at='2018-02-28T00:00:01+00:00', nodes_used=2054)
# ])

db.commit()