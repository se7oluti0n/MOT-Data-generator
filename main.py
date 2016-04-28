from data_generator import Parameter

if __name__ == "__main__":
    params = Parameter()
    params.readParametersFromXml('country.xml')
    print params.velocity, params.numObjects, params.minDistance