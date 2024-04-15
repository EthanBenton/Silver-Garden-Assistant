import numpy as np
import pandas
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os.path

"""
The purpose of this function is to convert from a .json format into a .html graph for use on the website
"""
class graphingTool:
    def __init__(self, data_source):
        """
        Base constructor of graphingTool
        Parameters define one direct path to a file to be accessed
        Args:
            self: the graphingTool object
            data_source: the full path to a json file from the current directory
        """
        self.dat = data_source #name of source file
        if(os.path.isfile(self.dat)):
            self.dframe = pandas.read_json(self.dat) #frame containing data from the .json
        else:
            print("Selected file does not exist in the same directory")
        self.export_name = 'user_interface/src/frontend/public/graphs/Graph.html'

    def set_export_name(self, input):
        """
        The input is a string
        Changes the name of the file created on export
        Args:
            self: the graphingTool object
            input: The name to be used for the exported file
        """
        self.export_name = 'user_interface/src/frontend/public/graphs/'+ input + '.html'

    def set_data_input(self, input):
        """
        The input must be .json
        Args:
            self: the graphingTool object
            input: The path to the json file being used to construct a graph
        """
        self.dat = input #name of source file
        self.dframe = pandas.read_json(self.dat) #frame containing data from the .json

    def get_export_name(self):
        """
        Returns the export name
        Args:
            self: the graphingTool object
        Yields:
            The name of the file being exported as a .html
        """
        return self.export_name
    
    def get_file_name(self):
        """
        Returns the path of the currently accessed file
        Args:
            self: the graphingTool object
        Yields:
            A full path to the currently utilized .json file
        """
        return self.dat #returns the name of the currently open file
    
    def get_data_frame(self):
        """
        Returns the dataframe of the open file
        Args:
            self: the graphingTool object
        Yields:
            A pandas dataframe object representing the data within the open .json file
        """
        return self.dframe #returns the dataframe of the currently open file
    
    def indexed_json_to_html(self, index, indey, indey2, title):
        """
        This function develops a graph with up to two values plotted simultaneously
        It reads from a .json as input, developing output in a .html file format
        Args:
            self: the graphingTool object
            index: the index indicating which column to use for the x-axis' data
            indey: the index indicating which column to use for the y-axis' data
            indey2: the index indicating which column to use for the second y-axis' data (-1 if no second y-axis is used)
            title: the title of the displayed graph
        """
        #Convert our input into three 1d arrays
        convert = self.dframe.values
        axisx = convert[:,index].flatten()
        axisy = convert[:,indey].flatten()
        
        namex = self.dframe.columns[index]
        namey = self.dframe.columns[indey]

        if(indey2 != -1): #third only if specified
            axisy2 = convert[:,indey2].flatten()
            namey2 = self.dframe.columns[indey2]
            
        
        #Create the figure
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        #Plot the first set of y-values
        fig.add_trace(go.Scatter(
            x=axisx,
            y=axisy,
            mode='markers',
            name = namey,
            connectgaps = False
        ),
        secondary_y=False
        )
        
        #Plot the second set of y-values ONLY if y2 != -1
        if(indey2 != -1):
            fig.add_trace(go.Scatter(
                x=axisx,
                y=axisy2,
                mode='markers',
                name = namey2,
                connectgaps=False
            ),
            secondary_y=True
            )
        
        #Include figure titles
        fig.update_xaxes(title_text=namex)
        fig.update_layout(title_text=title)
        fig.update_yaxes(title_text=namey,secondary_y=False)
        if(indey2 != -1):
            fig.update_yaxes(title_text=namey2,secondary_y=True)
        
        fig.write_html(self.export_name,auto_open=True)

def produce_from_json(input):
    """
    A simplification of main designed for use in a UI element.
    It only takes a file name of a json file as input.
    Args:
        input: The file path to a valid json file.
    """
    gr = graphingTool(input)
    #Trims the directory content and footer from the input name
    exportNam = (gr.dat[gr.dat.rfind('/')+1:gr.dat.find(".json")])
    #Adds in the export destination
    gr.set_export_name(exportNam)
    #Creates the graph
    #This currently assumes that our data is stored as {humidity, temp, timestamp}
    gr.indexed_json_to_html(2,1,0,exportNam)

def UI_button_interaction():
    """
    The event script that runs upon a button being pressed within a UI.
    It only targets a single json file for the initially generated data.
    """
    gr = graphingTool("user_interface/src/frontend/public/graphs/sensor_data.json") #Name can be changed accordingly to what needs graphing later.
    #Trims the directory content and footer from the input name
    exportNam = (gr.dat[gr.dat.rfind('/')+1:gr.dat.find(".json")])
    #Adds in the export destination
    gr.set_export_name(exportNam)
    #Creates the graph
    #This currently assumes that our data is stored as {humidity, temp, timestamp}
    gr.indexed_json_to_html(2,1,0,exportNam)
    


if __name__ == "__main__":
    """
    If run as main by the cli, the program will generate 
    a graph based on a user submitted path to a valid
    .json file and send it to 
    user_interface/src/frontend/public/graphs/
    with the same name as the json file specified.
    This graph will be displayed upon creation.
    """
    #example: data_processing_visualization/src/sensor_data.json
    fileNam = input('Enter .json file name.\n')
    produce_from_json(input=fileNam)