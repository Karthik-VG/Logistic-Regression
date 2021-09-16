import os

class FolderLabels:
    def __init__(self,baselink):
        print("This folder will make change filter all the xl dataset which have extra rows of data in xl sheet")
        self.baselink = baselink


    def folder_names(self):
        folders = []
        for i in os.listdir(self.baselink):
            if os.path.splitext(i)[1] == "":
                folders.append(os.path.splitext(i)[0])
        return folders


    def create_folders(self,folder_name, sub_folders):

        self.folder_name = folder_name
        self.sub_folders = sub_folders
        if not os.path.exists(self.baselink + "//" + self.folder_name):
            os.mkdir(self.baselink + "//" + self.folder_name)
        os.chdir(self.baselink + "//" + self.folder_name)
        for i in self.sub_folders:
            if not os.path.exists(self.baselink + "//" + self.folder_name + "//" + i):
                os.mkdir(self.baselink + "//" + self.folder_name + "//" + i)



