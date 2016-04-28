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
        import xml.etree.ElementTree as ET
          
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
      
            self.velocity = float(root.find('velocity').text)
            self.minDistance = int(root.find('num_objects').text)
            self.numObjects = float(root.find('min_distance').text)
            self.numFrames = int(root.find('num_frames').text)
        except Exception, e:
            import sys
            print "Unexpected error:", sys.exc_info()[0]
            raise
        else:
            pass
        finally:
            pass





