import csv
import numpy            as np
import matplotlib.pylab as plt
from   delay_code       import stations

plt.ion()

# opening the data file
with open('/Users/anita/Documents/Renee_presentation_course/ttc-vis/data/delay_codes_2014-2017.csv', 'rU') as csvfile:
    reader      = csv.reader(csvfile)
    delay_list  = list(reader)

delay_array   = np.array(delay_list)

# columns of data 
delay_date    = delay_array[:,0]
delay_time    = delay_array[:,1]
delay_day     = delay_array[:,2]
delay_station = delay_array[:,3]
delay_code    = delay_array[:,4]
delay_min_del = delay_array[:,5]
delay_min_gap = delay_array[:,6]
delay_bound   = delay_array[:,7]
delay_line    = delay_array[:,8]
delay_veh     = delay_array[:,9]

# extracting year values from file (b/c those are stored as strings)
years = []
for i in range(len(delay_date)):
    years.append(delay_date[i][0:4])
years = np.array(years)


# Delay code categories
train      = ['EUBO','EUAC','EUDO','EUTRD','MUODC','MUSAN','PUOPO','PUSCR','TUDOE','TUSET','TUST']
employee   = ['EUME','EUOE','MUCL','MUESA','MUIE','MULD','MUNOA','MUTD','MUWR','SUAE','TUCC','TUMVS','TUNIP','TUNOA','TUOPO','TUOS','TUS','TUSC','TUSUP']
signals    = ['PUCSC','PUCSS','PUSI','PUSIS','PUSNT','PUSO','PUSSW','PUSTS','PUSWZ','PUTSC']
track      = ['EUHV','EULT','EULV','PUTD','PUTDN','PUTR','PUTS','PUTSM','PUTTC','PUTTP','PUTWZ']
station    = ['PUMEL','PUMO','PUMST','SUCOL','SUEAS']
other_mech = ['EUAL','EUCH','EUCO','EUNEA','EUNT','EUO','EUOPO','EUPI','EUSC','EUTL','EUTM','EUTR','EUVA','EUVE','EUYRD','MUEC','MUFM','PUSCA','PUSRA','PUSTP','PUTCD','PUTNT','PUTO','PUTOE','TUKEY']
passenger  = ['MUD','MUDD','MUI','MUIR','MUIRS','MUIS','MUPAA','MUPR1','SUAP','SUBT','SUDP','SUG','SUO','SUPOL','SUROB','SUSA','SUSP','SUUT']
weather    = ['MUWEA','PUTIS']
misc       = ['MUGD','MUO','MULPA','MUPLB','MUPLC','MUSC','MUTO','PUSEA','TUML','TUO']


# determines which category the delay in each station in 2015 belongs to and 
# returns the number of occurance of each delay category
def comp_stacked_bar(station_name):
    # station name can be part pf the full name
    cat_train    = []
    cat_employee = []
    cat_signals  = []
    cat_track    = []
    cat_station  = []
    cat_other    = []
    cat_pass     = []
    cat_weather  = []
    cat_misc     = []

    vals_station = []
    
    # to find the values for the given station
    stations(station_name, vals_station)
    
    # finding all rows that belong to year 2015
    indx_station = np.where(years[vals_station] == '2015')

    # categorizing the delay codes
    for i in range(np.shape(indx_station[0])[0]):
        if delay_code[indx_station][i] in train:
            cat_train.append(delay_code[indx_station][i])
        elif delay_code[indx_station][i] in employee:
            cat_employee.append(delay_code[indx_station][i])
        elif delay_code[indx_station][i] in signals:
            cat_signals.append(delay_code[indx_station][i])
        elif delay_code[indx_station][i] in track:
            cat_track.append(delay_code[indx_station][i])
        elif delay_code[indx_station][i] in station:
            cat_station.append(delay_code[indx_station][i])
        elif delay_code[indx_station][i] in other_mech:
            cat_other.append(delay_code[indx_station][i])
        elif delay_code[indx_station][i] in passenger:
            cat_pass.append(delay_code[indx_station][i])
        elif delay_code[indx_station][i] in weather:
            cat_weather.append(delay_code[indx_station][i])
        elif delay_code[indx_station][i] in misc:
            cat_misc.append(delay_code[indx_station][i])
            
    return np.shape(cat_train)[0], np.shape(cat_employee)[0], np.shape(cat_signals)[0], np.shape(cat_track)[0], np.shape(cat_station)[0], np.shape(cat_other)[0], np.shape(cat_pass)[0], np.shape(cat_weather)[0], np.shape(cat_misc)[0]

# function to plot stacked bars for each station
def plot_stacked_bar(num):
    # num = location of the bar plot on x axis (usually should increment by 1)
    val_sum = 0  # this is the new starting point for the next bar plot (the start point would be the top of previous bar)
    plt.bar(num, bloor_train, align='center', color='#d53e4f', label="train")
    val_sum += bloor_train

    # the colors are color-blind friendly
    plt.bar(num, bloor_employee, bottom=val_sum, align='center', color='#f46d43', label="employee")
    val_sum+= bloor_employee

    plt.bar(num, bloor_signals, bottom=val_sum, align='center', color='#fdae61',label="signals")
    val_sum+= bloor_signals

    plt.bar(num, bloor_track, bottom=val_sum, align='center', color='#fee08b', label="track")
    val_sum+= bloor_track

    plt.bar(num, bloor_station, bottom=val_sum, align='center', color='#ffffbf', label="station")
    val_sum+= bloor_station

    plt.bar(num, bloor_other, bottom=val_sum, align='center', color='#e6f598', label="other")
    val_sum+= bloor_other

    plt.bar(num, bloor_pass, bottom=val_sum, align='center', color='#abdda4', label="passenger")
    val_sum+= bloor_pass

    plt.bar(num, bloor_weather, bottom=val_sum, align='center', color='#66c2a5', label="weather")
    val_sum+= bloor_weather

    plt.bar(num, bloor_misc, bottom=val_sum, align='center', color='#3288bd', label="misc")
    val_sum+= bloor_misc



bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("FINCH")
plot_stacked_bar(1)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("NORTH YORK")
plot_stacked_bar(2)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("SHEPPARD")
plot_stacked_bar(3)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("YORKM")
plot_stacked_bar(4)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("LAWRENCE")
plot_stacked_bar(5)


bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("EGLINTON")
plot_stacked_bar(6)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("DAVIS")
plot_stacked_bar(7)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("ST CLAIR STATION")
plot_stacked_bar(8)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("SUMMERHILL")
plot_stacked_bar(9)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("ROSEDALE")
plot_stacked_bar(10)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("BLOOR")
plot_stacked_bar(11)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("WELLESLEY")
plot_stacked_bar(12)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("COLLEGE")
plot_stacked_bar(13)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("DUNDAS")
plot_stacked_bar(14)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("QUEEN")
plot_stacked_bar(15)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("KING")
plot_stacked_bar(16)

bloor_train, bloor_employee, bloor_signals, bloor_track, bloor_station, bloor_other, bloor_pass, bloor_weather, bloor_misc = comp_stacked_bar("UNION")
plot_stacked_bar(17)


plt.legend(("train","employee","signals","track","station","other","passenger","weather","misc"),bbox_to_anchor=(1., 1.), prop={'size':12})
station_names = ['Finch', 'North York', 'Sheppard', 'Yorkmills', 'Lawrence', 'Eglinton','Daviseville','St Claire','Summerhill', 'Rosedale', 'Bloor','wellesley','College','Dundas','Queen', 'King', 'Union']

centers = np.arange(1,18,1)
plt.xticks(centers, station_names, rotation='vertical', fontsize=15)
plt.title("Delay Causes at each station in 2015")
