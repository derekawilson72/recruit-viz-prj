import sqlite3
import pandas as pd
import pandas.tools.rplot as rplot
from numpy import unique

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.mlab import find

DB_FILE = "../recruit.db"

try:
    connection = sqlite3.connect(DB_FILE)
    query = "select * from customer"
    df_customer = pd.read_sql(query, connection)
    # print(df_customer.head())
    # df_customer["income"].plot.hist(bins=50)
    # plt.show()
    # c.execute(query)
    # for row in c.fetchall():
    #     print(row)
except Exception as e:
    print("Unexpected error:", e)
else:
    connection.close()

##get columns
columns=df_customer.columns

df_customer.is_smoker=map(lambda x: {True:1, False:0}[x=='1'],df_customer.is_smoker) ##fix the is smoker column to 0 or 1.  
##if column value is '1', change to 1, else 0
df_customer.economic_stability=map(lambda x: int(x),df_customer.economic_stability )##convert economic stability to integer




def column_conversion(conversion_columns,df2):
    """
    This function will convert columns to a numerical index value so that they will plot in the scatter matrix.
    """
    conversion_params=[]
    for col in conversion_columns:
        unq_values=unique(df2[col])##get unique column values
        inx_values=range(len(unq_values))  ##set these columns to an index
        conversion_params.append([unq_values, inx_values])
        l1=lambda r: find(unq_values==r)[0]  ##locate the unique value by reverse lookup of referenced value
        df2[col]=map(l1, df2[col])  #convert the value of the column to its index value

    return df2, conversion_params

def convertLabels(axs,pos):
    """
    After converting the columns to numerical values, this function will label the axes according to the original values to appear more sensible and discernable.
    """
    j=-1
    for k in range(len(plot_columns)):
        ax=axs[k]
        colName=plot_columns[k]
        if colName in conversion_columns:
            print colName
            j=j+1 
            unq_values,index_values=conversion_params[j]
            if pos=='x':
                ax.set_xticks(index_values)
                ax.set_xticklabels(unq_values,rotation='horizontal')
            if pos=='y':
                ax.set_yticks(index_values)
                ax.set_yticklabels(unq_values,rotation='horizontal')



n=1000  #sample size
plot_columns=[ u'race_code','gender', u'education_id', u'income',u'economic_stability', u'home_owner',u'state', u'is_smoker']  ## set sample columns
conversion_columns=[ u'race_code','gender','home_owner',u'state','is_smoker']  ##list the columns that need converting to a numerical value
df2=df_customer[:n][plot_columns]  ##extract the sample dataframe

df2, conversion_params=column_conversion(conversion_columns,df2)  #convert the columns to numeric values

sm1=pd.tools.plotting.scatter_matrix(df2, alpha=0.2, figsize=(6, 6), diagonal='kde') ##scatter matrix plot

bot_axs=sm1[-1]  ##get bottom axes on plot that contain the xlabels
lft_axs=sm1[:,0]##get leftmost axes on plot that contain the ylabels

convertLabels(bot_axs,pos='x')
convertLabels(lft_axs,pos='y')  #convert the labels to text values

###Plotting Scatter Matrix....
fig1=plt.gcf()
fig1.canvas.set_window_title('scatter matrix 1')  #set window title
fig1.suptitle('Scatter Matrix 1') #set plot title
fig1.canvas.draw()
fig1.show()


