import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# file import function
def file_import(filename, truncateBefore = '1989-12-31'):
    output = pd.read_csv(filename, index_col = 0, parse_dates = True)    
    output.columns = [filename[-13:-4]]
    output.index.names = ['Date']
    output.index = [date+pd.tseries.offsets.MonthBegin(n=-1) if date.day!=1 else date for date in output.index ]
    output = output.truncate(truncateBefore)
    return output

# get target files: read in the yields
yield_02year = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_02y.csv')
yield_03year = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_03y.csv')
yield_05year = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_05y.csv')
yield_07year = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_07y.csv')
yield_10year = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_10y.csv')
yield_20year = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_20y.csv')
yield_30year = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_30y.csv')

yield_04week = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_04w.csv')
yield_13week = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_13w.csv')
yield_26week = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_26w.csv')
yield_52week = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/yield_52w.csv')

deficit = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/deficit.csv')
unemployment = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/unemployment.csv')
debtlimit = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/debtlimit.csv')
outstanding = pd.read_csv('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/outstanding.csv', index_col = 0, parse_dates = True)

# calculate the year over year inflation for CPI
# formula = CPI_today/CPI_1_year_ago * 100
cpi = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/CPI.csv','1989-08-31')
cpi=cpi.rename(columns = {'linda/CPI':'CPI'})
cpi.CPI[12:] = (cpi.CPI.values[12:]/cpi.CPI.values[0:len(cpi.CPI.values)-12]-1)*100 #yoy
cpi = cpi[cpi.index >= '1990-08-31']

# calculate the year over year inflation for GDP
gdp = file_import('C:/Users/563572/Documents/DataScienceClass/DAT3-students/linda/rgdp.csv','1989-06-30')
gdp=gdp.rename(columns = {'inda/rgdp':'rgdp'})

gdp.rgdp[4:] = (gdp.rgdp.values[4:]/gdp.rgdp.values[0:len(gdp.rgdp.values)-4]-1)*100 #yoy
gdp = gdp[gdp.index >= '1990-06-30']

# combine explanatory variables to form DataFrame
#learned concat
raw_data =  pd.concat([cpi,deficit,gdp,unemployment,debtlimit,outstanding['TotalOutstanding']], axis=1)
raw_data['prox2ceiling'] = raw_data.debtlimit
# obtain the debt ceiling date index (to calculate # months to debt ceiling later)
#cool use of map
nextceiling = [row for row in range(len(raw_data)) if row not in map(list, np.where(raw_data.debtlimit.isnull()))[0]]

# combine response variables
tsyYield = pd.concat([yield_04week,yield_13week,yield_26week,yield_52week,yield_02year,yield_03year,yield_05year,yield_07year,yield_10year,yield_20year,yield_30year], axis=1)
tsyYield = tsyYield.truncate('1990-8-31','2014-9-30')

# fill out missing data
# find how close the next debt limit is (# of months)
raw_data.prox2ceiling[raw_data.index[np.where(raw_data['prox2ceiling'].isnull()==0)]] = nextceiling
raw_data.prox2ceiling[-1] = 302
# the last element in df is sep2014, which is 6 months away from mar2015...
#since the length of the array is 296, the mar2015 debt ceiling limit corresponds to day 302
raw_data.prox2ceiling = raw_data.prox2ceiling.fillna(method='backfill') - range(len(raw_data.prox2ceiling))
#subtract the index of each day from the index of the next debt ceiling to get # of months from next debt ceiling

raw_data.debtlimit = raw_data.debtlimit.fillna(method='pad') #debt limit nan's should be padded
raw_data = raw_data.interpolate() #the rest of the nan variables can be interpolated
raw_data = raw_data.truncate('1990-8-31','2014-9-30') #filter series to desired dates
###############################################################################

# see debt ceiling effects - using masked arrays   
# note to self:tsyYield format = tsyYield['yield_04w']
linesDisconnect = [] #create this variable to disconnect all the '0 prox2ceilings'
for i in range(len(raw_data)-2):
    if (raw_data.prox2ceiling[i] + raw_data.prox2ceiling[i+1] + raw_data.prox2ceiling[i+2] == 1) or (raw_data.prox2ceiling[i] + raw_data.prox2ceiling[i+1] == 0):
        linesDisconnect.append(i)

# plot function for prox2ceiling: every 0 represents a debt ceiling month
def ceilingPlot(raw_data,tsyYield):   
    plt.scatter(raw_data['prox2ceiling'], tsyYield, c = np.arange(len(raw_data)), s = 20, alpha = 0.8, linewidth=0.5)
    ma1 = np.ma.masked_array(tsyYield, mask=raw_data['prox2ceiling']==0)
    ma2mask=raw_data['prox2ceiling']>1
    ma2mask[linesDisconnect] = True
    ma2 = np.ma.masked_array(tsyYield, mask = ma2mask)
    
    plt.plot(raw_data['prox2ceiling'],ma1,'k',alpha=0.75)
    plt.plot(raw_data['prox2ceiling'],ma2,'k',alpha=0.75)
    plt.title(tsyYield.name[6:])

# plot prox2ceiling vs different types of yields
plt.figure()
plt.suptitle('proximity to the debt ceiling vs treasury yields')
plt.subplot(3,4,1)
ceilingPlot(raw_data,tsyYield['yield_04w'])
plt.subplot(3,4,2)
ceilingPlot(raw_data,tsyYield['yield_13w'])
plt.subplot(3,4,3)
ceilingPlot(raw_data,tsyYield['yield_26w'])
plt.subplot(3,4,4)
ceilingPlot(raw_data,tsyYield['yield_52w'])
plt.subplot(3,4,5)
ceilingPlot(raw_data,tsyYield['yield_02y'])
plt.subplot(3,4,6)
ceilingPlot(raw_data,tsyYield['yield_03y'])
plt.subplot(3,4,7)
ceilingPlot(raw_data,tsyYield['yield_05y'])
plt.subplot(3,4,8)
ceilingPlot(raw_data,tsyYield['yield_07y'])
plt.subplot(3,4,9)
plt.ylabel('yield')
plt.xlabel('# of months to the next debt ceiling')
ceilingPlot(raw_data,tsyYield['yield_10y'])
plt.subplot(3,4,10)
ceilingPlot(raw_data,tsyYield['yield_20y'])
plt.subplot(3,4,11)
ceilingPlot(raw_data,tsyYield['yield_30y'])
###############################################################################

# fit linear regression
import statsmodels.formula.api as smf
import statsmodels.api as sm

#######IMPORTANT - HERE IS WHERE YOU CAN CHANGE THE RESPONSE VARIABLE######
yieldType = 'yield_04w'
yieldType = 'yield_13w'
yieldType = 'yield_10y'
yieldType = 'yield_30y'
####################################

# pick which yield to use
full_data = pd.concat([tsyYield[yieldType],raw_data],axis=1)
full_data.columns.values[0] = 'tyield'
full_data_index = pd.notnull(full_data.tyield)
full_data = full_data[full_data_index]

# scatter matrix
cols = ['tyield','CPI','deficit','rgdp','unemployment','TotalOutstanding','prox2ceiling'] 
pd.scatter_matrix(full_data[full_data.columns])

# Correlation coefficient matrix
corr_matrix = np.corrcoef(full_data[cols].T)
sm.graphics.plot_corr(corr_matrix, xnames=cols)

est = smf.ols(formula='tyield ~ CPI + deficit + rgdp + unemployment + TotalOutstanding + prox2ceiling', data=full_data).fit()
est.summary()
# result = strong multicollinearity

est = smf.ols(formula='tyield ~ deficit:unemployment + deficit:TotalOutstanding + deficit + rgdp + unemployment + TotalOutstanding + prox2ceiling', data=full_data).fit()
est.summary()
# based on scatter matrix, add interaction terms

est = smf.ols(formula='tyield ~ deficit:unemployment + deficit + rgdp + unemployment', data=full_data).fit()
est.summary()
# based on previous summary, get rid of variables with p value < 0.05

#predict using model and plot vs actual observations
plt.figure()
plt.scatter(full_data.index,est.predict(raw_data[full_data_index]),c='r',alpha=0.75)
plt.scatter(full_data.index,full_data.tyield)
plt.title(yieldType)
plt.xlabel('Date')
plt.ylabel(yieldType)
plt.show()
###############################################################################

#try regression tree model
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn import grid_search
#from sklearn.cross_validation import train_test_split

# Create a feature vector
features = full_data.columns.values[1:]

# check out a simple decision tree first: depth = 2
clf = DecisionTreeRegressor(max_depth=2,min_samples_leaf=5)
clf.fit(full_data.values[:,1:], full_data.tyield)
pred_y = clf.predict(full_data.values[:,1:])

# Create a dot file to visulaize the tree
fileName = yieldType+'.dot'
with open(fileName, 'w') as f:
    f = tree.export_graphviz(clf, out_file=f, feature_names=features, close=True)

# try out depth = 5
clf_5 = DecisionTreeRegressor(max_depth=5,min_samples_leaf=5)
clf_5.fit(full_data.values[:,1:], full_data.tyield)
pred_y_5 = clf_5.predict(full_data.values[:,1:])

#get the most important features from this tree
clf_5.feature_importances_
# Create a dot file to visulaize the tree
fileName2 = yieldType + '_5.dot'
with open(fileName2, 'w') as f:
    f = tree.export_graphviz(clf_5, out_file=f, feature_names=features, close=True)

# Now compare the depth of the decision tree
clf = tree.DecisionTreeClassifier(random_state=5, min_samples_leaf=5)
depth_range = range(1, 15)
param_grid = dict(max_depth=depth_range)
grid = grid_search.GridSearchCV(clf, param_grid, cv=5, scoring='mean_squared_error')
grid.fit(full_data.values[:,1:], full_data.tyield)

# Check out the scores of the grid search
grid_mean_scores = [result[1] for result in grid.grid_scores_]
    #note that this is always negative!!!
    #greater_is_better ...
    #Whether score_func is a score function (default), meaning high is good, 
    #or a loss function, meaning low is good. In the latter case, the scorer 
    #object will sign-flip the outcome of the score_func.

# Plot the results of the grid search
plt.figure()
plt.plot(depth_range, grid_mean_scores)
plt.hold(True)
plt.plot(grid.best_params_['max_depth'], grid.best_score_, 'ro', markersize=12, markeredgewidth=1.5,
         markerfacecolor='None', markeredgecolor='r')
plt.title("cross validation score (MSE) for regression tree")
plt.xlabel("depth")
plt.ylabel('negative MSE')
plt.grid(True)

# plot a tree that's over fitting
clf_9 = tree.DecisionTreeClassifier(random_state=9, min_samples_leaf=5)
clf_9.fit(full_data.values[:,1:], full_data.tyield)
pred_y_9 = clf_9.predict(full_data.values[:,1:])

# plot the different decision trees based on depth: clearly depth = 5 is the winner
plt.figure()
plt.scatter(full_data.index, full_data.tyield, c="k", label="actual yields")
plt.plot(full_data.index,pred_y,c='r', label="max depth 2",linewidth=1)
plt.plot(full_data.index,pred_y_5,c='b',label = 'max depth 5',linewidth=2)
plt.plot(full_data.index,pred_y_9,c='g', label="max depth: 9",linewidth=1)
plt.xlabel("Date")
plt.ylabel(yieldType)
plt.title("Decision Tree Regression")
plt.legend()



