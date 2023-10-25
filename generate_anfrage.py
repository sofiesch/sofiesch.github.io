import csv

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("generate_anfrage"),
    autoescape=select_autoescape()
)

template = env.get_template("anfrage.html")

with open("articles.csv") as f:
    articles = []
    for row in csv.DictReader(f):
        row["groessen"] = [s.strip() for s in row["groessen"].split("-")]
        articles.append(row)

# print(articles)

rendered = template.render(articles=articles)

with open("anfrage.html", "w") as f:
    f.write(rendered)
