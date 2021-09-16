import FolderLabels
import pandas as pd
import os

class combination:
    def __init__(self,baselink):
        """This module will help to make cominbe the data"""
        self.baselink = baselink


    def combine_data(self,folder):
        self.folder = folder
        f=FolderLabels.FolderLabels(self.baselink)
        folders = f.folder_names()
        folders.remove(self.folder)
        temp = pd.DataFrame()
        for i in folders:
            files = os.listdir(self.baselink + "\\" + i)
            # print(i)
            for j in files:
                df = pd.read_csv(self.baselink + "\\" + self.folder + "\\" + i + "\\" + j, sep=',', error_bad_lines=False)
                temp = pd.concat([temp, df], axis=0, ignore_index=True)
                # print(j)
        temp.to_csv(self.baselink + "\\" + "combineddata.csv", index=False)
        print("Files created successfully")