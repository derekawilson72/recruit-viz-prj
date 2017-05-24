


class sampleDataFrame():
    n=10000  #sample size
    plot_columns=[ u'race_code','gender', u'education_id', \
                       u'income',u'economic_stability', \
                       u'home_owner',u'state', u'is_smoker']  ## set sample columns
    conversion_columns=[ u'race_code','gender','home_owner',\
                             u'state','is_smoker']  ##list the columns that need converting to a numerical value


    def column_conversion(self,conversion_columns,df2):
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

    def convertLabels(self, axs,pos):
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


    def loadSample(self, df):
        df2=df[:n][plot_columns]  ##extract the sample dataframe
        df2, conversion_params=column_conversion(self.conversion_columns,df2)  #convert the columns to numeric values
