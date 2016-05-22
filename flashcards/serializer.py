import json

def serialize(data):
    """
    Serialize a dictionary object to a String.

    :param data: dictionnary object

    :returns: str representation of the serialized dictionary.
    """
    return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

def deserialize(dataStr):
    """
    Deserialize a string into a dictionnary object.

    :param dataStr: str representation of a dictionary

    :returns: dict object.
    """
    return json.loads(dataStr)
