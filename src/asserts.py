def checkType(param, againstType):
    assert type(param) == againstType

def checkOptionalType(param, againstType):
    assert param == None or type(param) == againstType

def checkDictType(param, keyType, valueType):
    assert type(param) == dict
    for key, value in param.iteritems():
        assert type(key) == keyType
        assert type(value) == valueType

def checkIterType(param, elemType):
    for elem in param:
        assert type(elem) == elemType

def checkCallable(param):
    assert callable(param)