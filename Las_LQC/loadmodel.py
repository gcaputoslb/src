def loadmodel(path):
    model = joblib.load(path)
    return model