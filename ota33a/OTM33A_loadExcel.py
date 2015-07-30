import numpy as np
import xlrd
def load_excel(filename,n1=0,gasCalibration=1.):
    '''
        This function was created to read in the example data from an excel file.
        
        Ideally when using this program, the user will create their own small script
        to properly read in their data.
        '''
    workbook = xlrd.open_workbook(filename) # load Excel file
    sheet = workbook.sheet_by_index(0) # use the first sheet in the file
    
    # create time array
    tmp = np.array([sheet.cell_value(row,0) for row in range(1+n1,sheet.nrows)])
    time = []
    for j in range(len(tmp)):
        time.append(xlrd.xldate_as_tuple(tmp[j],workbook.datemode))
    time = np.ma.array(time,mask=False)

    #grab all the other variables
    tracer = np.ma.array([sheet.cell_value(row,1) for row in range(n1+1,sheet.nrows)],mask=False)
    ch4 = np.ma.array([sheet.cell_value(row,2) for row in range(n1+1,sheet.nrows)],mask=False)/gasCalibration
    
    lat = np.ma.array([sheet.cell_value(row,3) for row in range(1,sheet.nrows-n1)],mask=False)
    lon = np.ma.array([sheet.cell_value(row,4) for row in range(1,sheet.nrows-n1)],mask=False)
    ws3 = np.ma.array([sheet.cell_value(row,5) for row in range(1,sheet.nrows-n1)],mask=False)
    wd3 = np.ma.array([sheet.cell_value(row,6) for row in range(1,sheet.nrows-n1)],mask=False)
    ws2 = np.ma.array([sheet.cell_value(row,7) for row in range(1,sheet.nrows-n1)],mask=False)
    wd2 = np.ma.array([sheet.cell_value(row,8) for row in range(1,sheet.nrows-n1)],mask=False)
    temp =np.ma.array([sheet.cell_value(row,9) for row in range(1,sheet.nrows-n1)],mask=False)+273.15
    pres =np.ma.array([sheet.cell_value(row,11) for row in range(1,sheet.nrows-n1)],mask=False)/1013.25
    ws3z =np.ma.array([sheet.cell_value(row,12) for row in range(1,sheet.nrows-n1)],mask=False)
    ws3y =np.ma.array([sheet.cell_value(row,14) for row in range(1,sheet.nrows-n1)],mask=False)
    ws3x =np.ma.array([sheet.cell_value(row,13) for row in range(1,sheet.nrows-n1)],mask=False)
    ws3t =np.ma.array([sheet.cell_value(row,15) for row in range(1,sheet.nrows-n1)],mask=False)
    
    return ch4,ws3,wd3,ws2,wd2,temp,pres,ws3z,ws3y,ws3x

def load_excel_old(filename):
    '''
        This function was created to read in the example data from an excel file.
        
        Ideally when using this program, the user will create their own small script
        to properly read in their data.
        '''
    n1=12 # Remove sampling time deplay of concetration and Sonic
    
    workbook = xlrd.open_workbook(filename) # load Excel file
    sheet = workbook.sheet_by_index(0) # use the first sheet in the file
    
    # create time array
    tmp = np.array([sheet.cell_value(row,0) for row in range(1+n1,sheet.nrows)])
    time = []
    for j in range(len(tmp)):
        time.append(xlrd.xldate_as_tuple(tmp[j],workbook.datemode))
    time = np.ma.array(time,mask=False)

    #grab all the other variables
    tracer = np.ma.array([sheet.cell_value(row,1) for row in range(n1+1,sheet.nrows)],mask=False)
    ch4 = np.ma.array([sheet.cell_value(row,2) for row in range(n1+1,sheet.nrows)],mask=False)
    
    lat = np.ma.array([sheet.cell_value(row,3) for row in range(1,sheet.nrows-n1)],mask=False)
    lon = np.ma.array([sheet.cell_value(row,4) for row in range(1,sheet.nrows-n1)],mask=False)
    ws3 = np.ma.array([sheet.cell_value(row,5) for row in range(1,sheet.nrows-n1)],mask=False)
    wd3 = np.ma.array([sheet.cell_value(row,6) for row in range(1,sheet.nrows-n1)],mask=False)
    ws2 = np.ma.array([sheet.cell_value(row,7) for row in range(1,sheet.nrows-n1)],mask=False)
    wd2 = np.ma.array([sheet.cell_value(row,8) for row in range(1,sheet.nrows-n1)],mask=False)
    temp =np.ma.array([sheet.cell_value(row,9) for row in range(1,sheet.nrows-n1)],mask=False)+273.15
    pres =np.ma.array([sheet.cell_value(row,11) for row in range(1,sheet.nrows-n1)],mask=False)/1013.25
    ws3z =np.ma.array([sheet.cell_value(row,12) for row in range(1,sheet.nrows-n1)],mask=False)
    ws3y =np.ma.array([sheet.cell_value(row,14) for row in range(1,sheet.nrows-n1)],mask=False)
    ws3x =np.ma.array([sheet.cell_value(row,13) for row in range(1,sheet.nrows-n1)],mask=False)
    ws3t =np.ma.array([sheet.cell_value(row,15) for row in range(1,sheet.nrows-n1)],mask=False)
    
    return ch4,ws3,wd3,ws2,wd2,temp,pres,ws3z,ws3y,ws3x,time



def load_csv(filename,n1=0,gasCalibration=1.):
    '''
        This function was created to read in the example data from an excel file.
        
        Ideally when using this program, the user will create their own small script
        to properly read in their data.
        '''
    
    tracer, ch4, lat, lon,ws3,wd3,ws2,wd2,temp,pres,ws3z,ws3y,ws3x,ws3t =  np.loadtxt(filename,delimiter=',',skiprows=1,comments='#',unpack=True,usecols = (1,2,3,4,5,6,7,8,9,11,12,13,14,15))
    
    n2 = len(ch4) - n1
    
    temp += 273.15
    pres /= 1013.25
    
    ch4 = np.ma.array(ch4[n1:])
    tracer = np.ma.array(tracer[n1:])
    
    lat = np.ma.array(lat[:n2])
    lon = np.ma.array(lon[:n2])
    ws3 = np.ma.array(ws3[:n2])
    wd3 = np.ma.array(wd3[:n2])
    ws2 = np.ma.array(ws2[:n2])
    wd2 = np.ma.array(wd2[:n2])
    temp = np.ma.array(temp[:n2])
    pres = np.ma.array(pres[:n2])
    ws3z = np.ma.array(ws3z[:n2])
    ws3y = np.ma.array(ws3y[:n2])
    ws3x = np.ma.array(ws3x[:n2])
    ws3t = np.ma.array(ws3t[:n2])
    
    return ch4,ws3,wd3,ws2,wd2,temp,pres,ws3z,ws3y,ws3x
