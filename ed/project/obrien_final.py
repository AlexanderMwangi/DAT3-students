"""
Post class version on Tuesday

I woul

@author: ed
"""
#code dump
'''
chicagozip =(60018, 60068, 60176, 60601, 60602, 60603, 60604, 60605, 60606, 60607, 60608, 60609, 60610, 60611, 60612, 60613, 60614, 60615, 60616, 60617, 60618, 60619, 60620, 60621, 60622, 60623, 60624, 60625, 60626, 60628, 60630, 60631, 60632, 60634, 60636, 60637, 60639, 60640, 60641, 60642, 60643, 60644, 60645, 60646, 60647, 60649, 60651, 60652, 60653, 60654, 60655, 60656, 60657, 60659, 60660, 60661, 60706, 60707, 60714)
sanfranzip =(94102, 94103, 94104, 94105, 94107, 94108, 94109, 94110, 94111, 94112, 94114, 94115, 94116, 94117, 94118, 94121, 94122, 94123, 94124, 94127, 94129, 94130, 94131, 94132, 94133, 94134, 94158)
chicagowhd = df[df['zip_cd'].isin(chicagozip)]
sanfranwhd = df[df['zip_cd'].isin(sanfranzip)]
#nycwhdrecent['code'] = [int(str(number)[:2]) for number in nycwhdrecent.codeint]
#nycwhdrecent['code'] = [str(number) for number in nycwhdrecent.naic_cd]
#nycwhdrecent.to_csv('nycwhdrecent.csv')
#ifvio = nycwagematch.ifvio
# i dont think this worked
match_high = wagehealthhigh.sort('SCORE',ascending=False).groupby('CAMIS',as_index=False).first()


'''

'''
this is a headache

>>> d['types'] =[type(number) for number in d.naic_cd]

d.types.value_counts()
<type 'str'>      122857
<type 'int'>       48741
<type 'float'>     16407

d.viobin.sum()
d.viobin.count()
float(139969)/(188005)
0.7444961570171006 = percentage of investigated companies that have a violation

'''

#table is a list of lists, each list is a pair of whd violation case ids and CAMIS that is associated with the business

table = [['CAMIS','case_id'],
[40394258,1515394],
[40399581,1489871],
[40401937,1522535],
[40401999,1527083],
[40517120,1552692],
[40538855,1619661],
[40735858,1515388],
[40847763,1469380],
[40945325,1677927],
[40993070,1523225],
[41017367,1510498],
[41033036,1541206],
[41083081,1551236],
[41097853,1517566],
[41158858,1545635],
[41164934,1654525],
[41166360,1662529],
[41195033,1508684],
[41206905,1723178],
[41207580,1479464],
[41217194,1496159],
[41243693,1502600],
[41283963,1724318],
[41301284,1515335],
[41311804,1612837],
[41317827,1602570],
[41329984,1540191],
[41343526,1671150],
[41350160,1677932],
[41350166,1677930],
[41403341,1539188],
[41445381,1651198],
[41462542,1672843],
[41469761,1489875],
[41495492,1505056],
[41495495,1520884],
[41495497,1520840],
[41515807,1502711],
[41524804,1636320],
[41538720,1644060],
[41547596,1526124],
[41549978,1722690],
[41566403,1664461],
[41576290,1549403],
[41595313,1689945],
[41619148,1651180],
[41670013,1520037],
[41718993,1613215],
[50001202,1684849],
[50001511,1721409],
[50002595,1699720],
[50004422,1647210],
[50005253,1647211],
[50005611,1722704],
[50007158,1567443],
[50007421,1655794],
[50012482,1675719],
[50015114,1614590],
[50016840,1722704]]

#these are the zipcodes in NYC
nyczip= (10001, 10002, 10003, 10004, 10005, 10006, 10007, 10009, 10010, 10011, 10012, 10013, 10014, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029, 10030, 10031, 10032, 10033, 10034, 10035, 10036, 10037, 10038, 10039, 10040, 10044, 10048, 10065, 10069, 10075, 10111, 10115, 10128, 10280, 10281, 10282, 11201, 11203, 11204, 11205, 11206, 11207, 11208, 11209, 11210, 11211, 11212, 11213, 11214, 11215, 11216, 11217, 11218, 11219, 11220, 11221, 11222, 11223, 11224, 11225, 11226, 11228, 11229, 11230, 11231, 11232, 11233, 11234, 11235, 11236, 11237, 11238, 11239, 11251, 11001, 11004, 11005, 11040, 11096, 11101, 11102, 11103, 11104, 11105, 11106, 11109, 11354, 11355, 11356, 11357, 11358, 11359, 11360, 11361, 11362, 11363, 11364, 11365, 11366, 11367, 11368, 11369, 11371, 11372, 11373, 11374, 11375, 11377, 11378, 11379, 11385, 11411, 11412, 11413, 11414, 11415, 11416, 11417, 11418, 11419, 11420, 11421, 11422, 11423, 11426, 11427, 11428, 11429, 11430, 11432, 11433, 11434, 11435, 11436, 11451, 11691, 11692, 11694, 11697, 10451, 10452, 10453, 10454, 10455, 10456, 10457, 10458, 10459, 10460, 10461, 10462, 10465, 10466, 10467, 10468, 10469, 10470, 10471, 10472, 10473, 10474, 10475, 10301, 10302, 10303, 10304, 10305, 10306, 10307, 10308, 10309, 10310, 10312, 10314)
#years is a list of years the data set is focusing on
years = (2008,2009,20010,20011,2012,2013,2014)

#whdwithhealth is a list of case numbers that also have health inspections
whdwithhealth=(1515394,
1489871,
1522535,
1527083,
1552692,
1619661,
1515388,
1469380,
1677927,
1523225,
1510498,
1541206,
1551236,
1517566,
1545635,
1654525,
1662529,
1508684,
1723178,
1479464,
1496159,
1502600,
1724318,
1515335,
1612837,
1602570,
1540191,
1671150,
1677932,
1677930,
1539188,
1651198,
1672843,
1489875,
1505056,
1520884,
1520840,
1502711,
1636320,
1644060,
1526124,
1722690,
1664461,
1549403,
1689945,
1651180,
1520037,
1613215,
1684849,
1721409,
1699720,
1647210,
1647211,
1722704,
1567443,
1655794,
1675719,
1614590,
1722704)

#nychealthmatchlist is a list of CAMIS ids of businesses that have been inspected by WHD
nychealthmatchlist =(40394258,
40399581,
40401937,
40401999,
40517120,
40538855,
40735858,
40847763,
40945325,
40993070,
41017367,
41033036,
41083081,
41097853,
41158858,
41164934,
41166360,
41195033,
41206905,
41207580,
41217194,
41243693,
41283963,
41301284,
41311804,
41317827,
41329984,
41343526,
41350160,
41350166,
41403341,
41445381,
41462542,
41469761,
41495492,
41495495,
41495497,
41515807,
41524804,
41538720,
41547596,
41549978,
41566403,
41576290,
41595313,
41619148,
41670013,
41718993,
50001202,
50001511,
50002595,
50004422,
50005253,
50005611,
50007158,
50007421,
50012482,
50015114,
50016840)


# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 14:00:44 2014

@author: ed
"""

ST = [['st_cd','NM'],
['AL',1],
['AK',2],
['AZ',4],
['AR',5],
['CA',6],
['CO',8],
['CT',9],
['DE',10],
['DC',11],
['FL',12],
['GA',13],
['HI',15],
['ID',16],
['IL',17],
['IN',18],
['IA',19],
['KS',20],
['KY',21],
['LA',22],
['ME',23],
['MD',24],
['MA',25],
['MI',26],
['MN',27],
['MS',28],
['MO',29],
['MT',30],
['NE',31],
['NV',32],
['NH',33],
['NJ',34],
['NM',35],
['NY',36],
['NC',37],
['ND',38],
['OH',39],
['OK',40],
['OR',41],
['PA',42],
['RI',44],
['SC',45],
['SD',46],
['TN',47],
['TX',48],
['UT',49],
['VT',50],
['VA',51],
['WA',53],
['WV',54],
['WI',55],
['WY',56],
['AS',60]]

"""
data sources:

whd_whisard.csv 
from
http://ogesdw.dol.gov/views/data_catalogs.php


https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59
DOHMH_New_York_City_Restaurant_Inspection_Results.csv
"""
import pandas as pd
import numpy as np 
dfwage = pd.read_csv('whd_whisard.csv')

#dump score = nychealth[nychealth.columns[-5]]
#there are lots of NAN - I think it depends on the type of inspections 
#all zip codes in nyc



nycwhd=dfwage[dfwage['zip_cd'].isin(nyczip)]

nycwhd['Year'] = [int(date[:4]) for date in nycwhd.findings_end_date]



nycwhdrecent = nycwhd[nycwhd['Year'].isin(years)]
nycwhdrecent['clean_naic_cd'] = [str(number) for number in nycwhdrecent.naic_cd]
nycwhdrecent['food_naic_cd'] = [int(number[:2]) for number in nycwhdrecent.clean_naic_cd]

nycwhdrecent['isrest'] = nycwhdrecent.food_naic_cd==72
nycfood = nycwhdrecent[nycwhdrecent.isrest==True]

nycwhdrest = nycfood[nycfood.columns[0:14]]
nycwhdrest.to_csv('nycwhdrest.csv')

nycwagematch = nycwhdrest[nycwhdrest['case_id'].isin(whdwithhealth)]
nycwagematch['ifvio'] = nycwagematch.case_violtn_cnt>0
func = nycwagematch.bw_atp_amt/nycwagematch.ee_violtd_cnt
nycwagematch['avepay'] = func
nycwagematch['avepay'] = [str(number) for number in nycwagematch.avepay]






nycwagematch['amtperee']=[number/nycwagematch.ee_violtd_cnt for number in nycwagematch.bw_atp_amt]
for number in nycwagematch.bw_atp_amt:




dfhealth = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')

nychealthmatch = dfhealth[dfhealth['CAMIS'].isin(nychealthmatchlist)]

nychealthwkey = pd.merge(nychealthmatch,df,on='CAMIS')
nycjoin = pd.merge(nychealthwkey,nycwagematch,on='case_id')











grouped = nychealthmatch.groupby('CAMIS').SCORE.sum()
grouped = grouped.fillna(0)

grouped.to_csv('grouped.csv')
grouped = pd.read_csv('grouped.csv')

'''
camis_with_score = nychealthmatch[['CAMIS','SCORE']]

camis_with_score = match_high[['CAMIS','SCORE']]
case_with_vio = nycwagematch[['case_id','ifvio']]


headers = table.pop(0)
df = pd.DataFrame(table, columns =headers)
match = df

camis_with_score = nychealthmatch[['CAMIS','SCORE']]
case_with_vio = nycwagematch[['case_id','ifvio']]
healthwage = df
merge_step_1 = pd.merge(healthwage,case_with_vio,how='left',on='case_id')
merge_step_2 = pd.merge(merge_step_1,camis_with_score, on='CAMIS')
df1 = merge_step_2

df3['vio']= df3.ifvio.astype(int)
df3.to_csv('12092014.csv')

merge_step_1 = pd.merge(combine,case_with_vio,how='left',on='case_id')
'''
'''

The code below didnt really work
import csv
with open('nycwhdrecent.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]
header.append('food')

for item in data:
...     if item[-1] =='72':
...         item.append(1)
...     else:
...         item.append(0)
... 

f.close
df = pd.read_csv('nycwhdrecent.csv')
'''

'''
-make a new column just for the first two number of the nac_id

-filter for only businesses that have been inspected that have a code that starts
with 72, as those are the ones that are related to food prep, and have a high chance of also being inspected by the nyc DOH

-match those to the businesses in the DOHMH dataset

- create a binary "has violations" column

- create a binary "has wage violations"
    Many times businesses will be compliant in how they are paying people, but they do not follow
    the record keeping regulations ( keeping time sheets, keeping payroll records)  exactly as required by the law, and therefore technically violated the law. Inorder to find cases that have wage violations, this information is not useful.

-merge the two datasets.

- run other models on them, such as adaboast, or ensembling.

'''














#http://stackoverflow.com/questions/19936794/geocoding-a-list-of-addresses-from-a-csv-file
# create an address column that has street , number and zipcode.
#zip = nycwhd['zip_cd'].astype(str)
#nycwhd['zip'] = zip
#zip = nychealth['ZIPCODE'].astype(str)
#nychealth['ZIP'] = zip
#7223
#7223



#run ed.py
import csv
import re

with open('nycwhdrest.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]

add = [el[4].upper() for el in data]

add2 = [re.findall(r'[0-9A-Z]+', address) for address in add]

exclude = set(['ROOM', 'AVENUE', 'FLOOR', 'RD','ROAD','ST','STREET','BLVD','GROUND','SUITE','#','NY','AVE','DRIVE','DR','1ST','FIRST','2ND','SECOND','3RD','THIRD','4TH','FOURTH','5TH','FIFTH','6TH','SIXTH','7TH','SEVENTH','8TH','EIGHTH','9TH','NINETH','BLVD','BOULEVARD','PLACE','PWKY','PARKWAY','N','NORTH','E','EAST','S','SOUTH','W','WEST','APT','APARTMENT'])

add3 = []
for add_list in add2:
    temp_list = []    
    for el in add_list:
        if el not in exclude:
            temp_list.append(el)
    add3.append(temp_list)

nycwage = [' '.join(el) for el in add3]


##########
'''
Here I want to preprocess the DOHMH data.
There are several rows for each individual restaurant.
I want to get only one row per restaurante in the city, and the address of that unique restaurante.
'''
import pandas as pd
import numpy as np 
dfhealth = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')

df['all']= df['CAMIS'].map(str) + ' '+df['DBA']+' ' + df['STREET']+ ' '+df['ZIPCODE'].map(str)

'''
Here I am going to combine the camis column, building number, street column, and the zipcode column.
then i will create an array of unique values.
then i will make a table from that array.
then pass it throught he regex.
then try to merge the results.

plan B is to sort the whd rest data my zipcode, and then try to use the street to match it to the 
health data.
'''



import csv
import re
#DOHMH_New_York_City_Restaurant_Inspection_Results.csv

with open('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]

add = [el[-1].upper() for el in data]

add2 = [re.findall(r'[0-9A-Z]+', address) for address in add]

exclude = set(['ROOM', 'AVENUE', 'FLOOR', 'RD','ROAD','ST','STREET','BLVD','GROUND','SUITE','#','NY','AVE','DRIVE','DR','1ST','FIRST','2ND','SECOND','3RD','THIRD','4TH','FOURTH','5TH','FIFTH','6TH','SIXTH','7TH','SEVENTH','8TH','EIGHTH','9TH','NINETH','BLVD','BOULEVARD','PLACE','PWKY','PARKWAY','N','NORTH','E','EAST','S','SOUTH','W','WEST'])

add3 = []
for add_list in add2:
    temp_list = []    
    for el in add_list:
        if el not in exclude:
            temp_list.append(el)
    add3.append(temp_list)

nychadd = [' '.join(el) for el in add3]
#outputs are nycwage and nychadd
#return here continue
#then add those string columns back to the frames
#nycwhd['clean'] = nycwage+' '+nycwhd.zip_cd
#nychealth['clean'] = nychadd

nycwhdrest['ADDRESS'] = nycwage
nychealth['add'] = nychadd

nycwhd['clean'] = nycwhd['add']+' '+nycwhd['zip'] 
nychealth['clean'] = nychealth['add']+' '+nychealth['ZIP']

#then join the frames to eachother on those columns
healthwage = pd.merge(nychealth,nycwhd,how='left',on='clean')
#then sort by where violation count is not null
hwhd = healthwage[healthwage.case_violtn_cnt >=0]
#then group by CAMIS and score max
#hwhd = hwhd.groupby('CAMIS').SCORE.max()
'''
then save this to a csv for now
then plot this to see if there is coorelation between score and violation
go back to the ed.py, and the exclude by line, add things to that, 
see if that helps, if not see if adding that column to the zipcode column with one space
gets anything. then keep going. 
#find all the ncais codes in the hwhd dataset, then pass that back to the nycwhd dataset to see how many i missed.
codes = hwhd[hwhd.columns[-16]]
'''
40394258	1515394
40399581	1489871
40401937	1522535
40401999	1527083
40517120	1552692
40538855	1619661
40735858	1515388
40847763	1469380
40945325	1677927
40993070	1523225
41017367	1510498
41033036	1541206
41083081	1551236
41097853	1517566
41158858	1545635
41164934	1654525
41166360	1662529
41195033	1508684
41206905	1723178
41207580	1479464
41217194	1496159
41243693	1502600
41283963	1724318
41301284	1515335
41311804	1612837
41317827	1602570
41329984	1540191
41343526	1671150
41350160	1677932
41350166	1677930
41403341	1539188
41445381	1651198
41462542	1672843
41469761	1489875
41495492	1505056
41495495	1520884
41495497	1520840
41515807	1502711
41524804	1636320
41538720	1644060
41547596	1526124
41549978	1722690
41566403	1664461
41576290	1549403
41595313	1689945
41619148	1651180
41670013	1520037
41718993	1613215
50001202	1684849
50001511	1721409
50002595	1699720
50004422	1647210
50005253	1647211
50005611	1722704
50007158	1567443
50007421	1655794
50010219	x?
50012482	1675719
50015114	1614590
50016840	1722704

crosswalk = (('health','wage'),
(40394258,1515394),
(40399581,1489871),
(40401937,1522535),
(40401999,1527083),
(40517120,1552692),
(40538855,1619661),
(40735858,1515388),
(40847763,1469380),
(40945325,1677927),
(40993070,1523225),
(41017367,1510498),
(41033036,1541206),
(41083081,1551236),
(41097853,1517566),
(41158858,1545635),
(41164934,1654525),
(41166360,1662529),
(41195033,1508684),
(41206905,1723178),
(41207580,1479464),
(41217194,1496159),
(41243693,1502600),
(41283963,1724318),
(41301284,1515335),
(41311804,1612837),
(41317827,1602570),
(41329984,1540191),
(41343526,1671150),
(41350160,1677932),
(41350166,1677930),
(41403341,1539188),
(41445381,1651198),
(41462542,1672843),
(41469761,1489875),
(41495492,1505056),
(41495495,1520884),
(41495497,1520840),
(41515807,1502711),
(41524804,1636320),
(41538720,1644060),
(41547596,1526124),
(41549978,1722690),
(41566403,1664461),
(41576290,1549403),
(41595313,1689945),
(41619148,1651180),
(41670013,1520037),
(41718993,1613215),
(50001202,1684849),
(50001511,1721409),
(50002595,1699720),
(50004422,1647210),
(50005253,1647211),
(50005611,1722704),
(50007158,1567443),
(50007421,1655794),
(50012482,1675719),
(50015114,1614590),
(50016840,1722704))

whdwithhealth=(1515394,
1489871,
1522535,
1527083,
1552692,
1619661,
1515388,
1469380,
1677927,
1523225,
1510498,
1541206,
1551236,
1517566,
1545635,
1654525,
1662529,
1508684,
1723178,
1479464,
1496159,
1502600,
1724318,
1515335,
1612837,
1602570,
1540191,
1671150,
1677932,
1677930,
1539188,
1651198,
1672843,
1489875,
1505056,
1520884,
1520840,
1502711,
1636320,
1644060,
1526124,
1722690,
1664461,
1549403,
1689945,
1651180,
1520037,
1613215,
1684849,
1721409,
1699720,
1647210,
1647211,
1722704,
1567443,
1655794,
1675719,
1614590,
1722704)

nychealthmatch =(40394258,
40399581,
40401937,
40401999,
40517120,
40538855,
40735858,
40847763,
40945325,
40993070,
41017367,
41033036,
41083081,
41097853,
41158858,
41164934,
41166360,
41195033,
41206905,
41207580,
41217194,
41243693,
41283963,
41301284,
41311804,
41317827,
41329984,
41343526,
41350160,
41350166,
41403341,
41445381,
41462542,
41469761,
41495492,
41495495,
41495497,
41515807,
41524804,
41538720,
41547596,
41549978,
41566403,
41576290,
41595313,
41619148,
41670013,
41718993,
50001202,
50001511,
50002595,
50004422,
50005253,
50005611,
50007158,
50007421,
50012482,
50015114,
50016840)

nychealthwage = df[df['CAMIS'].isin(nychealthmatch)]

nycwhdmatch['ifvio'] = nycwhdmatch.case_violtn_cnt>0
ifvio = nycwagematch.ifvio

table = state
headers = table.pop(0)
df = pd.DataFrame(table, columns =headers)
match = df
'''' 
I now have a df with the restuarantes that have been investigated by the department of labor,
that includes the CAMIS number, which uniquely identifies the store, and the highest score it has recieved when being inspeceted
by the health deparment.

I also have a list of all the restuarantes that have been both inspected by NYC DOH and have been investigated, with the case number for the 
investigation of that restaurante, and a binary output of whether or not there were violations. 

Also, I have a list of all CAMIS numbers matched with thier investigation case number.

The next step is to bring in the camis highest score, and then the binary if they had violations or not, to the df of the matched CAMIS numbers with Investigation numbers

'''

camis_with_score = match_high[['CAMIS','SCORE']]
camis_with_score = match_high[['CAMIS','SCORE']]
case_with_vio = nycwagematch[['case_id','ifvio']]
healthwage = df
merge_step_1 = pd.merge(healthwage,case_with_vio,how='left',on='case_id')
merge_step_2 = pd.merge(merge_step_1,camis_with_score, on='CAMIS')
df1 = merge_step_2
df2 = df1.drop('vio',1)
df3 = df2.fillna({'SCORE':0})
df3['vio']= df3.ifvio.astype(int)
df3.to_csv('12092014.csv')

step1 = pd.DataFrame(step1)


step1 = nycjoin.groupby('CAMIS').SCORE.mean()
step1 = pd.DataFrame(step1)
step1['wagevio'] = nycjoin.groupby('CAMIS').apply(lambda x: x.ifvio.iloc[0])
step1.head()

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split




step1['resttype'] = nycjoin.groupby('CAMIS').apply(lambda x: x['CUISINE DESCRIPTION'].iloc[0])
step1[]

step1['wagevio'] = step1.wagevio.astype(int)
step1['bw_atp'] = nycjoin.groupby('CAMIS').apply(lambda x: x['bw_atp_amt'].iloc[0])
step1['eevio'] = nycjoin.groupby('CAMIS').apply(lambda x: x['ee_atp_cnt'].iloc[0])
step1['amtperee'] = step1.bw_atp/step1.eevio
step1['avebwtoee'] = [str(number) for number in step1['amtperee']]
step1.avebwtoee.replace(to_replace='inf',value='0',inplace=True)
step1['floatave'] = [float(number) for number in step1['avebwtoee']]
hmod = smf.ols(formula='floatave ~ SCORE ', data=step1).fit()
hmod = smf.ols(formula='floatave ~ SCORE ', data=step1).fit()
step1['highscore'] = nycjoin.groupby('CAMIS').apply(lambda x: x['SCORE'].max())
high = smf.ols(formula='floatave ~ highscore ', data=step1).fit()




wage = smf.logit('wagevio ~ SCORE + resttype', data=step1).fit()
wage.summary()
np.exp(wage.params.wage)

'''
nacid code processing
'''
or number in codelist:
    if type(number)==int:
   
dfwage.naic_cd.astype(str,copy=True)      
y = dfwage.naic_cd.tolist()
stringlist = dfwage.string.tolist()

dfwage['string']=dfwage.naic_cd.astype(str,copy=True)
x = [number.find('7') in x for x in stringlist]
pattern ='-'
x = dfwage.string.str.contains(pattern)
dfwage['x'] = x
cleandf = dfwage.loc[dfwage['x']==False]
clean = cleandf.fillna('0')

'''
decision tree attempt
'''


##ST defined at the top of the file with the other lists
table = ST
headers = table.pop(0)
df = pd.DataFrame(table, columns =headers)
#create a new column with the number representing the state
clean_state =pd.merge(clean,df,how='left',on='st_cd')
d = clean_state[['zip_cd','NM','indust','cash']]

d.NM.isnull().sum()
3133

d = d.fillna(0)

# Now, split the data into training and test sets
train, test = train_test_split(d,test_size=0.3, random_state=1)

# Create a decision tree classifier instance
clf = tree.DecisionTreeClassifier(random_state=1)

# Fit the decision tree classifier
clf.fit(train[:,1:], train[:,0])

# Create a feature vector
features = d.columns.values[1:]
clean['cash']=[1 if x > 0 else 0 for x in clean.bw_atp_amt]

# Create a dot file
with open("titanic.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f, feature_names=features, close=True)



