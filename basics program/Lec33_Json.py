import json

data='{"hello":1,"how":2,"yoy":3}'

# -----------json.load convert string to dictinary----------
text=json.loads(data)
print(text["hello"])
print(data)

# -------json.dumps convert dictinary or string in to javascript running program----

data2={"fruits":("mango","apple"),
        "vegetables":["pataoato","tomato"]}

text2=json.dumps(data2)
print(text2)