import pandas as pd
import os
from FolderLabels import *

class Filterdata:
    def __init__(self,basepath, duplicate):
        """This function filters all the files present inside folders and saving in new folder with filtered data"""
        self.basepath = basepath
        self.duplicate = duplicate

    def clean_files(self):

        fol=FolderLabels(self.basepath)
        folders = fol.folder_names()
        folders.remove(self.duplicate)
        for i in folders:
            files = os.listdir(self.basepath + "\\" + i)
            # print(i)
            for j in files:
                df = pd.read_csv(self.basepath + "\\" + i + "\\" + j, skiprows=4, sep=',', error_bad_lines=False)
                df["class"] = i
                df.to_csv(self.basepath + "\\" + self.duplicate + "\\" + i + "\\" + j, index=False)
                # print(j)
        print("Files created successfully")