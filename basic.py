def unzipFF(fname):
    '''
    Input:
        fname - String format. File path to a target zip folder to be unzipped

    Output:
        Returns the unzipped contents of the folder.
    '''
    # Library
    from zipfile import ZipFile

    z = ZipFile(fname, 'r')
    z.printdir() # To print all the contents of the zip file
    z.extractall()
    z.close()

def bothShape(df1, df2):
    '''
    Inputs:
        df1 - Training Dataset
        df2 - Testing Dataset

    Outputs:
        Returns the shaoes of the Training and Testing Datasets
    '''
    # Print Statements
    print(f'The shape of the Training dataset is {df1.shape}')
    print(f'The shape of the Predicting dataset is {df2.shape}')

def intialPrep(df):
    '''
    Input:
        df - Dataframe on which initial checks (checking for Duplicated rows, lower casing the 
        variable names)

    Output:
        Returns a Dataframe with no duplicated rows and variable names lower cased.
    '''
    # Variable Lower-casing
    df.columns = df.columns.str.lower()

    # Conditional
    if df.duplicated().sum() != 0:
        print('Shape of the dataset before deleting the duplicated rows', df.shape)
        print('Number of duplicated rows in the dataset', df.duplicated().sum())
        df = df.drop_duplicates(inplace=True)
        print('Shape of the dataset after deleting the duplicated rows', df.shape)
    else:
        print('There are no Duplicated Rows in the dataset!')

    return df.head()

def missVarList(df):
    '''
    Input:
        df - Passed dataframe as an input. Determines the predictors with missing values and also 
            calculates the percentage of missing values in each predictor.

    Output:
        Returns a list containing only the variables with missing values.
    '''
    # Libraries
    import numpy as np

    # Empty lists and dictionary
    miss_var_list = []
    non_miss_var_list = []
    mv_dict = dict()

    # Loop
    for ind, row in enumerate(df.isnull().sum()):
        if row != 0:
            miss_var_list.append(df.columns[ind])
            mv_dict.update({df.columns[ind]: np.round((row / len(df)) * 100, 2)})
        else:
            non_miss_var_list.append(df.columns[ind])

    # Printing the list
    if len(non_miss_var_list) == len(df):
        print('Congratulations!!! There are no Missing Values in the DataFrame')
    else:
        print(f'Number of Columns with Missing Values:\n {len(miss_var_list)}\n')
        print(f'Variables with Missing Values with their Percentage are:\n {mv_dict}\n')

    return miss_var_list

def commMissVar(df1, df2):
    '''
    Inputs:
        df1 - Training Dataframe
        df2 - Testing Dataframe

    Outputs:
        Checks the presence of common variables with missing variables in both Train and Test dataframe
    '''
    # Conditions
    if len(missVarList(df1)) == 0 and len(missVarList(df2)) == 0:
        print('Congratulations!!!, There are no variables with missing values in both the datasets.')

    else:

        if len(missVarList(df1)) == 0 and len(missVarList(df2)) != 0:
            print('The first dataset does not contain any variables with Missing Variables')
            print('The second dataset does contain variables with Missing Variables')
            missVarList(df2)

        elif len(missVarList(df1)) != 0 and len(missVarList(df2)) == 0:
            print('The second dataset does not contain any variables with Missing Variables')
            print('The first dataset does contain variables with Missing Variables')
            missVarList(df1)

        else:
            if missVarList(df1) == missVarList(df2):
                print('Both the datasets hold common variables with Missing Values')
            elif missVarList(df1) != missVarList(df2):
                print('Both the datasets have different variables with Missing Values')

def row_nullCount(df, thresh=1):
    '''
    Function that returns the row number(s) and the number of missing values present in it for the 
    given dataframe.

    Inputs:
        df - Dataframe in consideration
        thesh - NUmber of missing values in the row that needs to be considered as a threshold

    Output:
        Returns a dictionary containing indices and their corresponding row null values.
    '''
    # Empty dictionary for holding the row numbers and the corresponding sum of null values
    null_count = {}

    # Loop to determine the pairs
    for i in range(len(df)):
        if sum(df.iloc[[i]].isnull().sum()) >= thresh:
            row_sum = sum(df.iloc[[i]].isnull().sum())
            null_count.update({i: row_sum})
        else:
            pass

    # Dropping the rows updated in the dictionary, from the dataframe
    df = df.drop(index=[k for k in null_count.keys()], inplace=True)

    return df

