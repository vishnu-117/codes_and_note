test = {
        "Key1" : "1",
        "Key2" : {
                  "a" : "2",
                  "b" : "3",
                  "c" : {
                          "d" : {"x":{"y": "10"}},
                          "e" : "1"
                         }
                   }
             }


def flatten_dict(data, parent_key='', separator='.'):
    items = {}
    for key, value in data.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, separator))
        else:
            items[new_key] = value
    return items

print(flatten_dict(test))