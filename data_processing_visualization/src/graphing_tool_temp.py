import os
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os.path
import pandas


class graphingTool:
    def __init__(self, data_source):
        """
        Initializes the graphingTool with a specified JSON data source.
        :param data_source: string, the file path to the JSON data source.
        """
        self.dat = data_source  # Path to the JSON data file.
        if(os.path.isfile(self.dat)):
            self.dframe = pandas.read_json(self.dat) #frame containing data from the .json
        else:
            print("Selected file does not exist in the same directory")  # pandas DataFrame initialized as None.
        self.rounding_value = 0  # Placeholder for rounding values, unused initially.
        self.averaging = False  # Flag to determine if averaging is used.
        self.export_name = 'Graph.html'  # Default export name for the generated graph.

        try:
            if os.path.isfile(self.dat):
                self.dframe = pd.read_json(self.dat)  # Load data from JSON file into DataFrame.
            else:
                raise ValueError(f"File {self.dat} does not exist")  # Raise an error if file does not exist.
        except Exception as e:
            print(f"Initialization failed: {e}")
            raise

    def set_export_name(self, input):
        """
        Sets the name of the file to which the graph will be exported.
        :param input: string, base name for the export file.
        """
        # self.export_name = 'user_interface/src/frontend/public/graphs/'+ input + '.html'
        self.export_name = f'D:/ODU/Spring 2024/CS411W/Silver-Garden-Assistant/user_interface/src/frontend/public/graphs/sensor_data.html'

    def set_data_input(self, input):
        """
        Updates the data source and reloads the data from a new JSON file.
        :param input: string, the file path to the new JSON data source.
        """
        self.dat = input
        try:
            self.dframe = pd.read_json(self.dat)  # Attempt to reload data from the new source.
        except Exception as e:
            print(f"Failed to reload data: {e}")
            self.dframe = pd.DataFrame()  # Set to an empty DataFrame on failure.

    def get_export_name(self):
        """
        Returns the current export name of the graph file.
        :return: string, the export file name.
        """
        return self.export_name
    
    def get_file_name(self):
        """
        Returns the file name of the current data source.
        :return: string, the data source file name.
        """
        return self.dat
    
    def get_data_frame(self):
        """
        Returns the DataFrame containing the loaded data.
        :return: DataFrame, the loaded data.
        """
        return self.dframe
    
    def set_average_amount(self, total):
        """
        Sets the averaging amount and determines whether averaging is active.
        :param total: int, specifies the total over which to average; sets averaging to False if <= 0.
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
    Generates a graph from a JSON file.
    :param input: string, the file path to the JSON data source.
    """
    gr = graphingTool(input)
    #Trims the directory content and footer from the input name
    exportNam = os.path.basename(input).replace('.json', '')
     #Adds in the export destination
    gr.set_export_name(exportNam)
    #Creates the graph
    #This currently assumes that our data is stored as {humidity, temp, timestamp}
    gr.indexed_json_to_html(2, 1, 0, exportNam)


def UI_button_interaction():
    """
    Handles the event triggered by a user interaction, such as a button press, to generate a graph.
    Uses a predefined JSON file path and generates a graph accordingly.
    """
    json_file_path = "D:/ODU/Spring 2024/CS411W/Silver-Garden-Assistant/user_interface/src/flask/data/sensor_data.json"  # Adjust this path as necessary
    gr = graphingTool(json_file_path)
    exportNam = (gr.dat[gr.dat.rfind('/')+1:gr.dat.find(".json")])
    gr.set_export_name(exportNam)
    #Creates the graph
    #This currently assumes that our data is stored as {humidity, temp, timestamp}
    gr.indexed_json_to_html(2,1,0,exportNam)

    


# if __name__ == "__main__":
#     """
#     This exists for demonstration purposes
#     """
#     fileNam = input('Enter .json file name.\n')
#     produce_from_json(input=fileNam)



#     #TODO: using plotly, export as .html for use on the website.