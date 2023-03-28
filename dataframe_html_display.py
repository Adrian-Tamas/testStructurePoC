from jinja2 import Environment, FileSystemLoader
import csv
from faker import Faker
from pandas import pandas

faker = Faker()

env = Environment(loader=FileSystemLoader('resources'))

# field names
fields = []
for _ in range(30):
    fields.append(faker.word())

# data rows as dictionary objects
mydict = []
for _ in range(20):
    data = {}
    for column in fields:
        data[column] = faker.word()
    mydict.append(data)

with open('data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(mydict)

df = pandas.read_csv("data.csv")
data = df.to_dict("records")
headers = df.columns.values.tolist()


parameters = {
    "header": headers,
    "data": data
}
if __name__ == '__main__':
    env.get_template("dataframe_template.html", globals=parameters).stream(name='foo').dump('df.html')
