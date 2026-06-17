# Contains the patient class and all of the functions (from PatientClassAndFunctions_2024-08-20-v1) in one place,
# with all of the function names the same as they were before. However, directory 
# specification will still need to take place in each individual file as of the current setup.

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import os

class patient:
    def __init__(self, filepath, input_fileName, lengthPtID):
        ptID = input_fileName[:lengthPtID]
        self.ptID = ptID
        self.fileName = input_fileName
        #find the demographics in one of two sheets
        # directory = os.getcwd()
        file_adds = filepath + '/' + input_fileName
        file = pd.ExcelFile(file_adds)
        sheet_Names = file.sheet_names
        if 'redcap' in sheet_Names:
            #do the thing for getting patient info
            #check what the labels are for the RedCap data
            df = pd.read_excel(input_fileName, sheet_name= 'redcap')
            self.ptDemographics = df
            self.survival = df.at[0,"Survival Time (Months)"]
            self.age = df.at[0,"age"] 
            self.sex = df.at[0,"sex"]
            self.ecog = df.at[0,"ecog"]
            self.cci = df.at[0,"comorbidity_cci"] 
            self.primarytumor = df.at[0, "tumor_type"] #1, Esophagogastric | 2, HCC | 3, Biliary Tract | 4, Pancreatic | 5, Colorectal | 6, Anal | 7, NET | 8, Other GI cancer
            self.primaryhisto = df.at[0, "tumor_histology"]
            self.primarytumorEnrollment = df.at[0, "primary_tumor"] #binary for presence at time of enrollment
            self.dateDx = df.at[0, "date_of_diagnosis"]
            self.stagedx = df.at[0, "stage_initial_diagnosis"]
            self.stageEnrollment = df.at[0, "stage_enrollment"]

            #for metastasis location at enrollment 
            self.metEnrollmentLiver = df.at[0, "site_of_metastasis___1"]
            self.metEnrollmentLung = df.at[0, "site_of_metastasis___2"]
            self.metEnrollmentPeritoneum = df.at[0, "site_of_metastasis___3"]
            self.metEnrollmentBone = df.at[0, "site_of_metastasis___4"]
            self.metEnrollmentLymphNode = df.at[0, "site_of_metastasis___5"]
            self.metEnrollmentOther = df.at[0, "site_of_metastasis___6"]

            #create a label for the presence of mets at enrollment


        else: print("no patient identifying information")

        #now iterate through the list of sheets to import the patient data 
        #pull the full list of data on all labs and lab results
        if 'Labs' in sheet_Names:
            self.labsData = pd.read_excel(input_fileName, sheet_name= 'Labs')
        else: self.labsData = False

        #treatments recieved
        if 'txRecieved' in sheet_Names:
            self.txsData = pd.read_excel(input_fileName, sheet_name= 'txRecieved')
        else: self.txsData = False
        
        #particular cancer treatment types spreadsheets
        if 'ChemoTx' in sheet_Names:
            self.ChemoTx = pd.read_excel(input_fileName, sheet_name= 'ChemoTx')
        else: self.ChemoTx = False

        if 'HemeTx' in sheet_Names:
            self.HemeTx = pd.read_excel(input_fileName, sheet_name= 'Hematologic Tx')
        else: self.HemeTx = False

        if 'ImmunoTx' in sheet_Names:
            self.ImmunoTx = pd.read_excel(input_fileName, sheet_name= 'Immuno Tx')
        else: self.ImmunoTx = False

        if 'RadTx' in sheet_Names:
            self.RadTx = pd.read_excel(input_fileName, sheet_name= 'Radiation Tx')
        else: self.RadTx = False

        if 'OtherTx' in sheet_Names:
            self.OtherTx = pd.read_excel(input_fileName, sheet_name = 'Other Tx')
        else: self.OtherTx = False

        #collect methlyation signatures and NSR information
        if 'MethylationSignature' in sheet_Names:
            self.methylationSignatures = pd.read_excel(input_fileName, sheet_name= 'MethylationSignature')
        else: self.methylationSignatures = False

        if 'NSR' in sheet_Names:
            self.NSR = pd.read_excel(input_fileName, sheet_name= 'NSR')
        else: self.NSR = False



# End of patient class

#update this class to reflect the information for the ovarian datasetz

# class patient:
#     def __init__(self, filepath, input_fileName):
#         ptID = input_fileName.replace(".xlsx", "")
#         self.ptID = ptID
#         self.fileName = input_fileName
#         #find the demographics in one of two sheets
#         # directory = os.getcwd()
#         file_adds = filepath + '/' + input_fileName
#         file = pd.ExcelFile(file_adds, engine="openpyxl")
#         sheet_Names = file.sheet_names

#         #now iterate through the list of sheets to import the patient data 
#         if 'Labs' in sheet_Names:
#             self.labsData = pd.read_excel(input_fileName, sheet_name= 'Labs')
#         else: self.labsData = False
        
#         if 'Smoking_Alc_Hx' in sheet_Names:
#             self.smokingAlcHx = pd.read_excel(input_fileName, sheet_name= 'Smoking_Alc_Hx')
#         else: self.smokingAlcHx = False

#         if 'CCI' in sheet_Names:
#             self.CCI = pd.read_excel(input_fileName, sheet_name= 'CCI')
#         else: self.CCI = False

#         if 'Demographics' in sheet_Names:
#             self.demographicData = pd.read_excel(input_fileName, sheet_name= 'Demographics')
#         else: self.CCI = False

#         if 'diagnoses' in sheet_Names:
#             self.diagnosisData = pd.read_excel(input_fileName, sheet_name= 'diagnoses')
#             # column 0: tissue type
#             # column 1: begnin date (XXXX-XX-XX)
#             # column 2: malignant date (XXXX-XX-XX)
#         else: self.diagnosisData = False

#         #to create a callable list of treatments recieved for which we have data
#         # need to change for the different chemo types in the ovarian cancer dataset
#         # maybe new individual sheets on the patient excel?
       
#         tx_sheets = ['PACLitaxel_Interval', 'CARBOplatin_Interval', 'gemcitabine_Interval', 'DOXOrubicin liposome_Interval', 'topotecan_Interval', 'megestrol_Interval']
#         # might need to add window to the suffix
#         treatmentTypesRecieved = [] 
#         self.txDataFrames = {}
        
#         for possible in tx_sheets:
#             if possible in sheet_Names:
#                 df = pd.read_excel(input_fileName, sheet_name= possible)
#                 self.txDataFrames[possible] = df
#                 treatmentTypesRecieved.append(possible)
#         self.txRecieved = treatmentTypesRecieved

#     def diagnosis_type(self, tumor_type=1):
#         # tumor types: benign (1), malignant (2)
#         # column 0: tissue type
#         columns =  [self.diagnosisData.columns[0], self.diagnosisData[tumor_type]]

#         self.diagnosisData = self.diagnosisData[columns]


# FilterList function
def FilterList(list, keyWords_primary, keyWords_secondary = ["Empty"], omit = ["Empty"]):
    #store the filtered result
    filteredList = []

    if keyWords_secondary == ["Empty"]:
        for c in list: #loop the columns
            for buzz in keyWords_primary: #loop the key words
                if buzz in c: #if the column contains the key word
                    filteredList.append(c) #add the column to the list
                    break #do not continue testing primary key words for this column
    
    else: 
        for c in list: #loop the columns
            for buzz in keyWords_primary: #loop the key words
                if buzz in c: #if the column contains the key word
                    for secondary in keyWords_secondary:
                        if secondary in c:
                            filteredList.append(c) #add the column to the list
                            break #has been added to list based on passing the secondary 
                        else:
                            pass
                    break #do not continue to check primary key words for this column
                else:
                    pass
                
    if omit != ["Empty"]: 
        for x in omit: 
            for a in filteredList:
                if x in a:
                    filteredList.remove(a)
    
    #by iterating through the column names first, we keep the order of the columns

    return filteredList 

#createBinary function
def createBinary(df, listOfLabs, timeColumn): 
    #list of labs needs to match exactly.  
    # Filter the dataframe before inputting
    #for boolean
    df_toBool = df[listOfLabs]
    df_bool = df_toBool.notna()
    df_asint = df_bool.astype(int)
    #add column back for time 
    df_asint.insert(0, timeColumn, df[timeColumn])
    return df_asint

# createBinarySum
def createBinarySum(df, listOfLabs, timeColumn, defaxis):
    #list of labs needs to match exactly.  
    # Filter the dataframe before inputting
    #for boolean
    df_toBool = df[listOfLabs]
    df_bool = df_toBool.notna()
    df_asint = df_bool.astype(int)
    #add column back for time 
    # df_asint.insert(0, timeColumn, df[timeColumn])
    #sum across the row
    #defaxis = 0 means the columns are preserved 
    #defaxis =1 means the rows are preserved
    df_new_sum = df_asint.sum(axis = defaxis)
    return df_new_sum

#get list of patients from directory 
def GetListOfPatientsFromDirectory (directory, fileExtension, fileCommon, lengthID):
    #get the directory 
    listFileNames = os.listdir(directory)
    outputList = []
    #loop through list of fileNames: 
    for file in listFileNames:
        #id if the file is patient data
        if fileCommon in file and file.endswith(fileExtension):
            #trim the file name to the pt ID
            ptID = file[:lengthID]
            outputList.append(ptID)
    return outputList

def GetListofPTfiles(directory, fileExtension, fileCommon):
    listFileNames = os.listdir(directory)
    outListFiles = []
    #loop through file names
    for file in listFileNames:
        if fileCommon in file and file.endswith(fileExtension):
            outListFiles.append(file)
    return outListFiles

#get amyloid status dictionary inputs, sort ptIDs to lists based on amyloid status 
def getListSortedByAmyloid(amyloidDictionary, listPositive, listNegative, listOther,
                           statusPositive = "yes", statusNegative = "no"):
    for pt in amyloidDictionary.keys():
        status = amyloidDictionary[pt]
        if status == statusPositive:
            listPositive.append(pt)
        elif status == statusNegative:
            listNegative.append(pt)
        else:
            listOther.append(pt)
    #does not check for double listed patient IDs
    
#function for masking a dataframe 
def patientSectionOfFrame(start_frame, column_toMask, ptID):
    #ptID is a row parameter in the column_toMask
    df_use = start_frame #copy of the frame

    #first check if sheet has the column of interest
    data_top = list(start_frame.columns) #returns the headers as a list

    #determine of the sheet contains the column of interest
    if data_top.count(column_toMask) > 0: 
        #if true, now find if the patient is present
        searchForPt = start_frame[column_toMask].str.startswith(ptID).sum() #returns the number of instances of the patient
        if searchForPt > 0:
            #patient is present 
            #mask the data for the patient
            df_clean = df_use.dropna(subset= [column_toMask]) #removing NA 
            mask = df_clean[column_toMask].str.startswith(ptID) #masking for the rows where the patient has data
            df_sub_tosave = df_clean[mask] #output dataframe filtered for the patient
            return df_sub_tosave
        else:
            #the patient isn't present
            # return print("The patient " + ptID + " is not in " + sheet_name)
            pass
    else:
        #the column of interest isn't present
        # return print("The column " + column_toMask + " is not in the sheet " + sheet_name)
        pass

#make folder path for data
def makeFolderPathForData(parent_dir, folderName_header, folderName_common, folderName_suffix):
    #makes a new directory for your files
    #returns the folder name for use in other functions
    folderName = folderName_header + folderName_common + folderName_suffix
    path = os.path.join(parent_dir,folderName)
    if not os.path.exists(path):
        os.mkdir(path)
    return folderName

#to excel function
def outputToExcel(df_data, fileName_header, fileName_Common, fileName_suffix,
                  parent_dir, folderName, sheetName):
    fileName = fileName_header + fileName_Common + fileName_suffix
    outfile_extension = '.xlsx'
    outfile_boxplts = fileName + outfile_extension
    path_out= os.path.join(parent_dir, folderName, outfile_boxplts)

    if os.path.exists(path_out):
            #if old sheet
            with pd.ExcelWriter(path_out, mode = 'a', if_sheet_exists = 'overlay') as writer:
                    df_data.to_excel(writer, sheet_name = sheetName, index = True)
    else: 
            #new sheet
            with pd.ExcelWriter(path_out) as writer:
                    df_data.to_excel(writer, sheet_name = sheetName, index = True) #if new sheet

def outputFiguresPath(fileName_header, fileName_mid, fileName_suff, parent_dir, folderName, fileExtension = '.tif'):
        fileName_header = str(fileName_header)
        fileName_mid = str(fileName_mid)
        fileName_suff = str(fileName_suff)

        #cleaning the input to prevent addition of / to the directory
        fileName_header = fileName_header.replace("/", "-")
        fileName_mid = fileName_mid.replace("/", "-")
        fileName_suff = fileName_suff.replace("/", "-")

        fileName = fileName_header + fileName_mid +fileName_suff
        out_filename = fileName + fileExtension
        new_filepath = os.path.join(parent_dir, folderName, out_filename)
        #the output path can be used to save the figure
        return new_filepath
        # plt.savefig(new_filepath, bbox_inches = 'tight')