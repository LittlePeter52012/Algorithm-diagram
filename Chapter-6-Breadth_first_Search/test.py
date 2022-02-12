#TAG1 图的实现

from gc import garbage


graph = {}
graph["you"] = [
    "alice", "bob", "claire"
]

print(graph)

# Bigger graph
graph = {}
graph["you"] = ["allice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = [] 

print(graph["you"])