import re

with open("schemas/openapi.yaml", "r") as f:
    text = f.read()

replacements = [
    ("'401'", "'Error401'"),
    ("'429'", "'Error429'"),
    ("responses/401", "responses/Error401"),
    ("responses/429", "responses/Error429"),
]

for old, new in replacements:
    text = text.replace(old, new)

with open("schemas/openapi.yaml", "w") as f:
    f.write(text)
