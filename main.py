from data_generator import Parameter
import data_generator
if __name__ == "__main__":
    params = Parameter()
    params.readParametersFromXml('country.xml')
    print params.velocity, params.numObjects, params.minDistance
    points = data_generator.initializePoints(params)
    data_generator.generateTrajectories(points, params)