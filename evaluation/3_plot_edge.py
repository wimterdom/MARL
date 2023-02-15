#!/usr/bin/env python3
from datetime import datetime, date
import pandas as pd
import matplotlib.pyplot as plt
import sys

if(len(sys.argv) < 2):
    print("[usage] python3 plot_edge_cov.py [src1_plotdata_path] [label_1] [src2_plotdata_path] [label_2] [src3_plotdata_path] [label_3] [out_dir_path] [output_name] [title]")
else:
    input_1 = str(sys.argv[1])
    label_1 = str(sys.argv[2])
    input_2 = str(sys.argv[3])
    label_2 = str(sys.argv[4])
    input_3 = str(sys.argv[5])
    label_3 = str(sys.argv[6])
    output_name = '/' + str(sys.argv[8]) + '.png'
    out_dir = str(sys.argv[7]) + output_name
    title_name = str(sys.argv[9])
    

    # input data source
    df = pd.read_csv(input_1, header=None, index_col=None)
    df2 = pd.read_csv(input_2, header=None, index_col=None)
    df3 = pd.read_csv(input_3, header=None, index_col=None)

    # variable type defintion
    final_time_1 = []
    final_time_2 = []
    final_time_3 = []
    edge_1 = []
    edge_2 = []
    edge_3 = []

    #print(df[0][1])
    
    '''
    # variable type defination
    unix_time_1 = []
    unix_time_2 = []
    realtime_1 = []
    realtime_2 = []
    

    ## unix timestamp convert to datetime
    for i in range(1, df.shape[0]):
        unix_time_1.append(df[0][i])
    
    for i in range(1, df2.shape[0]):
        unix_time_2.append(df2[0][i])

    for i in range(0, len(unix_time_1)):
        unix_1 = datetime.fromtimestamp(int(unix_time_1[i]))
        realtime_1.append(str(unix_1))

    for i in range(0, len(unix_time_2)):
        unix_2 = datetime.fromtimestamp(int(unix_time_2[i]))
        realtime_2.append(str(unix_2))
    
    #print(len(realtime_1))
    
    # compute the different of time
    time_1 = realtime_1[0]
    time_3 = realtime_2[0]
    time1_struct = datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S")
    time3_struct = datetime.strptime(time_3, "%Y-%m-%d %H:%M:%S")
    final_time_1.append(0)
    final_time_2.append(0)

    # x1 data
    for i in range(1, len(realtime_1)):
        time_2 = realtime_1[i]
        time2_struct = datetime.strptime(time_2, "%Y-%m-%d %H:%M:%S")
        seconds_1 = (time2_struct - time1_struct).seconds
        final_time_1.append(seconds_1/3660)
    # x2 data
    for i in range(1, len(realtime_2)):
        time_4 = realtime_2[i]
        time4_struct = datetime.strptime(time_4, "%Y-%m-%d %H:%M:%S")
        seconds_2 = (time4_struct - time3_struct).seconds
        final_time_2.append(seconds_2/3600)
'''
    #x1
    for i in range(1, df.shape[0]):
        final_time_1.append((int(df[0][i]) - int(df[0][1])) / 3600)

    #x2
    for i in range(1, df2.shape[0]):
        final_time_2.append((int(df2[0][i]) - int(df2[0][1])) / 3600)

    #x3
    for i in range(1, df3.shape[0]):
        final_time_3.append((int(df3[0][i]) - int(df3[0][1])) / 3600)

    # y1 data
    for i in range(1, df.shape[0]):
        map_size_percent_age = df[6][i].strip().replace("%", "")
        mapsize = float(map_size_percent_age) * 65536 / 100
        edge_1.append(mapsize)
    

    # y2 data
    for i in range(1, df2.shape[0]):
        map_size_percent_age2 = df2[6][i].strip().replace("%", "")
        mapsize2 = float(map_size_percent_age2) * 65536 / 100
        edge_2.append(mapsize2)

    # y3 data
    for i in range(1, df3.shape[0]):
        map_size_percent_age3 = df3[6][i].strip().replace("%", "")
        mapsize3 = float(map_size_percent_age3) * 65536 / 100
        edge_3.append(mapsize3)
    
    # generate picture
    plt.title(title_name)
    plt.xlabel('Time(Hour)')
    plt.ylabel('edge coverage')
    plt.plot(final_time_1, edge_1, color=(255/255, 0/255, 0/255), label=label_1 )
    plt.plot(final_time_2, edge_2, color=(0/255, 255/255, 0/255), label=label_2)
    plt.plot(final_time_3, edge_3, color=(0/255, 0/255, 255/255), label=label_3)
    plt.legend()
    plt.savefig(out_dir)
    plt.show()
