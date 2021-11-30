
# Main file of the program

import webScrape as ws
from googleapiclient.discovery import build
import csv
import pandas as pd

import os
class csv_generator:
    def __init__(self, c_name) -> None:
        self.client_name = c_name
        self.currentPATH = self.get_current_path()
        self.joinedPATH  = self.joinPath()
        
    
    
    def get_current_path():
        return os.path.dirname(os.path.abspath(__file__))
    def joinPath():
        return os.path.join(self.currentPATH, 'csv_data')
    
api_key = 'AIzaSyBJixTpGuWue17mPX1Ia_O7vUcrcvcOdMs'
channel_unique_id = ["UCAaZm4GcWqDg8358LIx3kmw"]    #this is the world of boxing
channel_name = "David Dobrik"   #if channel unique id is unknown
input_list = ["UCBfqzdKPe_CzDqo1qj2_GSw", 'Srkcycles']
# check if input text is in record of unique id or channel name. if not find the unique id

record = pd.read_csv('record.csv')
record_dict = record.set_index('Name')['Unique ID'].to_dict()

print(record_dict)
for i in input_list:
    if i in record_dict:
        print(f"NAME yes {i} is in record")
    elif i in record_dict.values():
        print(f"UNIQUEID yes {i} is in record")
    
    #if it is not in record_dict add them in
    else:
        


