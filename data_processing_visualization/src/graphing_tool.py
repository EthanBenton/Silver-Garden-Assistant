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
        self.export_name = 'user_interface/src/frontend/public/graphs/'+ input + '.html'

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
        This function develops a graph with up to two values plotted simultaneously
        It reads from a .json as input, developing output in a .html file format
        index - index for x1
        indey - index for y1
        indey2 - index for y2
        title - graph title
        """
        #Convert our input into three 1d arrays
        convert = self.dframe.values
        axisx = convert[:,index]
        axisy = convert[:,indey]
        namex = self.dframe.columns[index]
        namey = self.dframe.columns[indey]
        if(indey2 != -1): #third only if specified
            axisy2 = convert[:,indey2]
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

        #Plot the second set of y-values ONLY if y2 != -1
        if(indey2 != -1):
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
        if(indey2 != -1):
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




#if __name__ == "__main__":
 #   """
  #  This exists for demonstration purposes
   # More will be added in future.
    #"""
#    fileNam = input('Enter .json file name.\n')
#    demo = graphingTool(fileNam)
 #   exportNam = (demo.dat[demo.dat.rfind('/')+1:demo.dat.find(".json")])
  #  demo.set_export_name(exportNam)
#    x = int(input('Enter x index.\n'))
 #   y = int(input('Enter y index.\n'))
  #  y2 = int(input('Enter second y-index (-1 if unused)\n'))
   # demo.indexed_json_to_html(x,y,y2,exportNam)



    #TODO: using plotly, export as .html for use on the website.