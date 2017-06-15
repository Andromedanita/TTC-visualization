yus = ['downsview','wilson','yorkdale','lawrence west','glencairn','eglinton west','st clair west','dupont','spadina','st george','museum',"queen's park",'st patrick','osgoode','st andrew','union','king','queen','dundas','college','wellesley','bloor','rosedale','summerhill','st clair','davisville','eglinton','lawrence','york mills','sheppard','north york centre','finch']
bd = ['kipling','islington','royal york','old mill','jane','runnymede','high park','keele','dundas west','lansdowne','dufferin','ossington','christie','bathurst','spadina','st george','bay','yonge','sherbourne','castle frank','broadview','chester','pape','donlands','greenwood','coxwell','woodbine','main street','victoria park','warden','kennedy']
interchange = ['spadina','st george','bloor','yonge'] # bloor-yonge is just one interchange, but it has different names on each line

NS_sep = 1
EW_sep = 1

turn = yus.index('union')
US_posy = np.arange(0,(turn)*NS_sep,NS_sep)[::-1]
US_posx = -EW_sep*np.ones(len(US_posy))
Y_posy = np.arange(0,(len(yus)-turn-1)*NS_sep,NS_sep)
Y_posx = EW_sep*np.ones(len(Y_posy))
NS_posy = np.concatenate((US_posy,-NS_sep*np.ones(1)))
NS_posy = np.concatenate((NS_posy,Y_posy))
NS_posx = np.concatenate((US_posx,np.zeros(1)))
NS_posx = np.concatenate((NS_posx,Y_posx))
NS_posy[0:(yus.index('spadina')+1)] -= NS_sep
NS_posx[0:(yus.index('spadina')+1)] -= EW_sep

EW_posx = np.arange(0,len(bd)*EW_sep,EW_sep)
EW_posy = np.zeros(len(EW_posx)) + (NS_posy[yus.index('spadina')])
EW_posx -= EW_posx[bd.index('bay')]


plt.figure(figsize=(30,15))
plt.plot(EW_posx,EW_posy,'o',color='g',markersize=10)
plt.plot(NS_posx,NS_posy,'o',color='gold',markersize=10)
plt.xticks([])
plt.yticks([])




