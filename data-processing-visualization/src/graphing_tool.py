import numpy as np
import csv
import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas

"""
The purpose of this function is to convert from a .json format into a .csv format for the sake of graphing utilizing Seaborn
"""
class graphingTool:
    def __init__(self, data_source):
        """
        The input must be .json
        """
        self.dat = data_source #name of source file
        self.dframe = pandas.read_json(self.dat) #frame containing data from the .json

    def set_data_input(self, input):
        """
        The input must be .json
        """
        self.dat = input #name of source file
        self.dframe = pandas.read_json(self.dat) #frame containing data from the .json

    def get_file_name(self):
        return self.dat #returns the name of the currently open file
    
    def get_data_frame(self):
        return self.dframe #returns the dataframe of the currently open file
    
    def simple_graph(self, inx, iny, namex, namey, title):
        """
        Develops a simple line graph
        inx - the input list of x values
        iny - the input list of y values
        namex - name used for x axis
        namey - name used for y axis
        title - name used for graph title
        """
        plt.plot(inx, iny)
        plt.xlabel(namex)
        plt.ylabel(namey)        
        plt.title(title)
        plt.xticks(list(range(min(inx),len(inx)+1)))
        plt.yticks(list(range(min(iny),len(iny)+1)))
        plt.show()

    def indexed_graph(self, dex, dey, namex, namey, title):
        """
        Develop a line graph using the data within data_source
        dex - index for x values
        dey - index for y values
        namex - name of x axis
        namey - name of y axis
        title - name for graph title
        """
        sns.lineplot(data=self.dframe,x=self.dframe.columns[dex],y=self.dframe.columns[dey])
        plt.xlabel(namex)
        plt.ylabel(namey)
        plt.title(title)
        plt.show()

    def indexed_graph_double(self, dex, dey, dey2, namex, namey, namey2, title):
        """
        Same functionality as indexed_graph, only accepting two y-values to be graphed now
        dex - index for x
        dey - index for y1
        dey2 - index for y2
        namex - name of x axis
        namey - name of first y
        namey2 - name of second y
        title - title of the graph
        """
        
        convert = self.dframe.values
        axisx = convert[:,dex]
        axisy = convert[:,dey]
        axisy2 = convert[:,dey2]

        #Temperature in red
        plt.plot(axisx,axisy,label=self.dframe.columns[dey],color='red')
        plt.tick_params(axis='y',labelcolor='red')
        plt.xlabel(namex)
        plt.ylabel(namey,color='red')
        plt.title(title)
        temp=axisy.min()
        temp2=axisy.max()
        plt.yticks(list(range(int(temp),int(temp2)+2)))
        
        #Switch to second y
        plt.twinx()
        
        #Humidity in blue
        plt.plot(axisx,axisy2,label=self.dframe.columns[dey2],color='blue')
        plt.tick_params(axis='y',labelcolor='blue')
        plt.ylabel(namey2,color='blue')
        temp=axisy2.min()
        temp2=axisy2.max()
        plt.yticks(list(range(int(temp),int(temp2)+2)))
        plt.tight_layout()
        plt.legend()
        plt.show()

if __name__ == "__main__":
    """
    This exists for demonstration purposes
    More will be added in future.
    """
    demo = graphingTool("sensor_data.json")
    # x = [1,2,3,4,5,6,7,8,9,10]
    # y = [10,9,8,7,6,5,4,3,2,1]
    # demo.simple_graph(x,y,"X-values","Y-values","Testing Graph")
    # demo.indexed_graph(0,1,"Timestamp","Temperature","TITLE")
    demo.indexed_graph_double(0,1,2,"Timestamp","Temperature (C)","Humidity (%)","Generated Raw Data")