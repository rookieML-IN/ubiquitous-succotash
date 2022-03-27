def plot_barCharts(inpData, cols_toPlot):
    '''
    Inputs:
        inpData - Dataset in consideration
        cols_toPlot - Categorical Columns to be Represented

    Outputs:
        Returns Bar plots of the desired columns in subplot format.
    '''
    # Library
    import matplotlib.pyplot as plt

    # Defining SubPlots
    fig, sub_plot = plt.subplots(nrows=1, ncols=len(cols_toPlot), figsize=(30, 10))
    fig.suptitle('Bar charts of: ' + str(cols_toPlot))

    # Loop to Plot
    for colName, plotNumber in zip(cols_toPlot, range(len(cols_toPlot))):
        inpData.groupby(colName).size().plot(kind='bar', ax=sub_plot[plotNumber])

def varCat(df, u_thresh):
    '''
    Function that would categorize variables on the basis of number of unique values present in
    the variable.

    Inputs:
        df - Dataset in consideration
        u_thresh - Threshold value of number of unique values for categorizing

    Outputs:
        Returns 3 lists containing names of the variables of the desired variable types (Quantitative, Categorical, Qualitative)
    '''
    # Empty Lists
    q_col = []  # list containing quantitative Variables
    c_col = []  # List containing categorical variables
    pref_drop = []  # List containing variables to be dropped from the dataset 

    # Loop
    for col_name in df.columns:
        if df[str(col_name)].nunique() <= u_thresh:
            c_col.append(str(col_name))
        elif df[str(col_name)].nunique() == len(df):
            pref_drop.append(str(col_name))
        else:
            q_col.append(str(col_name))

    return q_col, c_col, pref_drop

