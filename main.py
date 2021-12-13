# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')



def first_non_zero():
    # Use a breakpoint in the code line below to debug your script.
    df = pd.read_csv('data.csv')
    # print(df.to_string())
    pds = df['Precipation Rate']
    loc_list = []
    pre_value = 0.0
    for index, value in pds.items():
        # print(f" OUT Index : {index}, Value : {value}")
        if value == 0.0:
            if pre_value == 0.0:
                continue
            else:
                pre_value = 0.0
        elif pre_value == 0.0:
            # print(f"Index : {index}, Value : {value}")
            loc_list.append(index)
            pre_value = 1

    non_zero_pd = df.loc[loc_list]
    print(non_zero_pd.to_string)
    non_zero_pd.to_excel("output.xlsx")
    x =non_zero_pd.iloc[:,1]
    y= non_zero_pd.iloc[:,2]
    plt.plot(x, y, 'o', color='black');
    ax = plt.gca()
    # ax.set_xlim([xmin, xmax])
    ax.set_ylim([-1000, 5000])
    plt.show()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_non_zero()


