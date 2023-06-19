import pandas as pd

colorcoding = pd.read_csv("C:/Users/aio439/Box/Aws python test/all image colors.csv")
labelcoding = pd.read_csv("C:/Users/aio439/Box/Aws python test/aws_label_images.csv")
roomambiance = pd.read_csv("C:/Users/aio439/Box/Aws python test/room ambiances.csv")
hexcode = pd.read_csv("C:/Users/aio439/Box/Aws python test/abababaa.csv")

# Get unique values of num
FileID = labelcoding['FileName'].unique()

# Create a dictionary to store the data for each row
data = {}
for FileName in FileID:
     # Initialize the row with the num value
    row = {'FileName': FileName}

    # Check if the num value is in each table and add the corresponding values
    if FileName in roomambiance['FileName'].values:
        for Room in roomambiance['Room'].unique():
            count = roomambiance.loc[(roomambiance['FileName'] == FileName) & (roomambiance['Room'] == Room), 'Room'].size
            row[Room] = count if count > 0 else False
        for Ambiance in roomambiance['Ambiance'].unique():
            count = roomambiance.loc[(roomambiance['FileName'] == FileName) & (roomambiance['Ambiance'] == Ambiance), 'Ambiance'].size
            row[Ambiance] = count if count > 0 else False
        for Dimension in roomambiance['Dimension'].unique():
            count = roomambiance.loc[(roomambiance['FileName'] == FileName) & (roomambiance['Dimension'] == Dimension), 'Dimension'].size
            row[Dimension] = count if count > 0 else False
    if FileName in labelcoding['FileName'].values:
        for Name in labelcoding['Name'].unique():
            count = labelcoding.loc[(labelcoding['FileName'] == FileName) & (labelcoding['Name'] == Name), 'Name'].size
            row[Name] = count if count > 0 else False
    if FileName in colorcoding['FileName'].values:
        for Color in colorcoding['Color'].unique():
            count = colorcoding.loc[(colorcoding['FileName'] == FileName) & (colorcoding['Color'] == Color), 'Color'].size
            row[Color] = count if count > 0 else False
    if FileName in hexcode['FileName'].values:
        for BG1 in hexcode['BG1'].unique():
            count = hexcode.loc[(hexcode['FileName'] == FileName) & (hexcode['BG1'] == BG1), 'BG1'].size
            row[BG1] = count if count > 0 else False
        for BG2 in hexcode['BG2'].unique():
            count = hexcode.loc[(hexcode['FileName'] == FileName) & (hexcode['BG2'] == BG2), 'BG2'].size
            row[BG2] = count if count > 0 else False
        for BG3 in hexcode['BG3'].unique():
            count = hexcode.loc[(hexcode['FileName'] == FileName) & (hexcode['BG3'] == BG3), 'BG3'].size
            row[BG3] = count if count > 0 else False
        for BG4 in hexcode['BG4'].unique():
            count = hexcode.loc[(hexcode['FileName'] == FileName) & (hexcode['BG4'] == BG4), 'BG4'].size
            row[BG4] = count if count > 0 else False
        for BG5 in hexcode['BG5'].unique():
            count = hexcode.loc[(hexcode['FileName'] == FileName) & (hexcode['BG5'] == BG5), 'BG5'].size
            row[BG5] = count if count > 0 else False
        

    # Add the row to the dictionary
    data[FileName] = row

# Convert the dictionary to a DataFrame and save it to a CSV file
LSATEST = pd.DataFrame.from_dict(data, orient='index')
LSATEST.to_csv('modified_label_space_affect.csv', index=False)


