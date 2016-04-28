#Class to store pameter
class Parameter:
    def __init__(self):
        self.velocity = 0
        self.minDistance = 0
        self.numObjects = 0
# 
def readFromXml(filename):
    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    root = tree.getroot()
    
    velocity = float(root.find('velocity').text)
    numObjects = int(root.find('num_objects').text)
    minDistance = float(root.find('min_distance').text)

    result = Parameter()
    result.velocity = velocity
    result.minDistance = minDistance
    result.numObjects = numObjects

    return result

if __name__ == "__main__":
    params = readFromXml('country.xml')
    print params.velocity, params.numObjects, params.minDistance


