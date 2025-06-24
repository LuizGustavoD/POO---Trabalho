import json

class JSONEncoder:
    def __init__(self, indent=None):
        self.indent = indent

    def encode(self, obj):
        return json.dumps(obj, indent=self.indent)

class JSONDecoder:
    def __init__(self):
        pass

    def decode(self, json_string):
        return json.loads(json_string)