# python setup.py build && python3 -m pip install -e . --no-deps

import ujson

print(ujson.dumps([{"key": "value"}, 81, True, None, {"test": None}], drop_none=True))
print(ujson.dumps([{"key": "value"}, 81, True, None, {"test": None}], drop_none=False))
