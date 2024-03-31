import numpy as np
import csv
import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os.path

"""
The purpose of this function is to convert from a .json format into a .html graph for use on the website
"""
class graphingTool:
    def __init__(self, data_source):
        """
        The input must be .json
        """
        self.dat = data_source #name of source file
        if(os.path.isfile(self.dat)):
            self.dframe = pandas.read_json(self.dat) #frame containing data from the .json
        else:
            print("Selected file does not exist in the same directory")
        self.rounding_value = 0
        self.averaging = False
        self.export_name = 'Graph.html'

    def set_export_name(self, input):
        """
        The input is a string
        Changes the name of the file created on export
        """
        self.export_name = input + '.html'

    def set_data_input(self, input):
        """
        The input must be .json
        """
        self.dat = input #name of source file
        self.dframe = pandas.read_json(self.dat) #frame containing data from the .json

    def get_export_name(self):
        return self.export_name
    
    def get_file_name(self):
        return self.dat #returns the name of the currently open file
    
    def get_data_frame(self):
        return self.dframe #returns the dataframe of the currently open file
    
    def set_average_amount(self, total):
        """
        Sets the averaging type for use in other functions.
        Inputting a total of 0 or less sets averaging to False, turning off the feature.
        Inputting a total of 1 or higher sets averaging to True, turning on the feature.
        total - the overarching total for which data points are averaged.
        Averages are calculated over the value specified in total for the entire dataset.
        """
        self.rounding_value = total
        if total > 0:
            self.averaging = True
        else:
            self.averaging = False
        #This function will be of use in determining if to find an average for points in time when graphing.
        #TODO Update graphing functions to utilize the data from set_average_type in developing graphs.

    def indexed_json_to_html(self, index, indey, indey2, title):
        """
        This function serves a similar purpose to indexed_graph_double, except the output is an HTML file, for usage on the project website.
        index - index for x1
        indey - index for y1
        indey2 - index for y2
        namex - name for x1
        namey - name for y1
        namey2 - name for y2
        title - graph title
        """
        #Convert our input into three 1d arrays
        convert = self.dframe.values
        axisx = convert[:,index]
        axisy = convert[:,indey]
        axisy2 = convert[:,indey2]
        namex = self.dframe.columns[index]
        namey = self.dframe.columns[indey]
        namey2 = self.dframe.columns[indey2]

        #Create the figure
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        #Plot the first set of y-values
        fig.add_trace(go.Scatter(
            x=axisx,
            y=axisy,
            name = namey,
            connectgaps = True
        ),
        secondary_y=False
        )

        #Plot the second set of y-values
        fig.add_trace(go.Scatter(
            x=axisx,
            y=axisy2,
            name = namey2,
            connectgaps=True
        ),
        secondary_y=True
        )
        
        #Include figure titles
        fig.update_xaxes(title_text=namex)
        fig.update_layout(title_text=title)
        fig.update_yaxes(title_text=namey,secondary_y=False)
        fig.update_yaxes(title_text=namey2,secondary_y=True)



        #This section of code was directly inspired from
        #https://plotly.com/python/dropdowns/
        #TODO: It needs to be fixed :(
        # fig.update_layout(
        #     updatemenus=[
        #         dict(
        #             active=0,
        #             buttons=list([
        #                 dict(label="None",
        #                      method="update",
        #                      args=[{"visible: [True, True]"}]),
        #                 dict(label=namey,
        #                      method="update",
        #                      args=[{"visible: [True, False]"}]),
        #                 dict(label=namey2,
        #                      method="update",
        #                      args=[{"visible: [False, True]"}])
        #             ])
        #         )
        #     ]
        # )
        #End citation

        fig.write_html(self.export_name,auto_open=True)




if __name__ == "__main__":
    """
    This exists for demonstration purposes
    More will be added in future.
    """
    fileNam = input('Enter .json file name.\n')
    demo = graphingTool(fileNam)
    exportNam = input('Enter Graph Title.\n')
    demo.set_export_name(exportNam)
    demo.indexed_json_to_html(0,1,2,exportNam)



    #TODO: using plotly, export as .html for use on the website.