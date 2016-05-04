import random
import numpy as np
from lxml import etree
##
## @brief      { class_description }
##
class Parameter:
    def __init__(self):
        self.velocity = 0
        self.minDistance = 0
        self.numObjects = 0
        self.numFrames = 0
    ##
    ## @brief      { Read parameter from XML and save to object attribute }
    ##
    ## @param      self      The object.
    ## @param      filename  The XML file name
    ##
    ## @return     { description_of_the_return_value }
    ##
    def readParametersFromXml(self, filename):

          
        try:
            tree = etree.parse(filename)
            root = tree.getroot()
      
            self.velocity = float(root.find('velocity').text)
            self.numObjects = int(root.find('num_objects').text)
            self.minDistance = float(root.find('min_distance').text)
            self.numFrames = int(root.find('num_frames').text)
        except Exception, e:
            import sys
            print "Unexpected error:", sys.exc_info()[0]
            raise

##
## @brief      { function_description }
##
## @param      params  The settings read from XML file
##
## @return     { List of objects position in 2D }
##
def initializePoints(params):
    try:
    
        # We create a grid of 25 x 4 points, then randomly choose the points from these 100 points 
        indices = random.sample(range(1, 100), params.numObjects)
        print "List of indices: ", indices
        
        # Convert indices to 2d position
        objPositions = np.zeros((len(indices), 2))
        for i in range(len(indices)):
            #convert to 2d index
            y_index = indices[i] / 25
            x_index = indices[i] % 25
            objPositions[i, 0] = x_index * 1.0 * params.minDistance
            objPositions[i, 1] = y_index * 1.0 * params.minDistance

        print "List of positions: ", objPositions
        return objPositions
    except Exception, e:
        raise e
##
## @brief      { function_description }
##
## @param      initPositions  The init positions
## @param      params         The params
##
## @return     { description_of_the_return_value }
##
def generateTrajectories(initPositions, params):
    try:

        velocity = np.array([params.velocity, 0])
        deltaTime = 1
        trajectories = etree.Element("trajectories")
        for j in range(params.numFrames):
            frame = etree.SubElement(trajectories, "frame", id=str(j))
            for i in range(len(initPositions)):

                # Propagate position along time
                nextPos = initPositions[i,:] + velocity * deltaTime * j

                # if object inside the observation area then output as measurement
                if (nextPos[0] >= params.minDistance * 25 and nextPos[0] < params.minDistance * 25 + 3 ):
                    obj = etree.SubElement(frame, "obj", id=str(i), x=str(nextPos[0]), y=str(nextPos[1]))
        tree = etree.ElementTree(trajectories)
        tree.write("trajectories.XML", pretty_print=True)
    except Exception, e:
        raise e