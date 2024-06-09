import re

with open("schemas/openapi.yaml", "r") as f:
    text = f.read()

text = text.replace("400Response", "Response400")

with open("schemas/openapi.yaml", "w") as f:
    f.write(text)
