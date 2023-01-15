from datetime import datetime, date
import pandas as pd
import matplotlib.pyplot as plt
import sys

if(len(sys.argv) < 2):
    print("[Usage] python3 plot_crash.py [src1_plotdata_path] [label_1] [src2_plotdata_path] [label_2] [output_path] [output_name] [title]")
else:
    input_1 = str(sys.argv[1])
    label_1 = str(sys.argv[2])
    input_2 = str(sys.argv[3])
    label_2 = str(sys.argv[4])
    output_name = '/' + str(sys.argv[6]) + '.png'
    out_path = str(sys.argv[5]) + output_name
    title_name = str(sys.argv[7])
    
    # input data source
    df = pd.read_csv(input_1, header=None, index_col=None)
    df2 = pd.read_csv(input_2, header=None, index_col=None)
    #print(df.shape[0])

    # variable type defination
    final_time_1 = []
    final_time_2 = []
    unique_crash_1 = []
    unique_crash_2 = []

    '''
    # variable type defination
    unix_time_1 = []
    unix_time_2 = []
    realtime_1 = []
    realtime_2 = []
    final_time_1 = []
    final_time_2 = []
    unique_crash_1 = []
    unique_crash_2 = []

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
        final_time_1.append(seconds_1/3600)

    # x2 data
    for i in range(1, len(realtime_2)):
        time_4 = realtime_2[i]
        time4_struct = datetime.strptime(time_4, "%Y-%m-%d %H:%M:%S")
        seconds_2 = (time4_struct - time3_struct).seconds
        final_time_2.append(seconds_2/3600)
    '''

    # x1 data
    for i in range(1, df.shape[0]):
        final_time_1.append((int(df[0][i]) - int(df[0][1])) / 3600)

    # x2 data
    for i in range(1, df2.shape[0]):
        final_time_2.append((int(df2[0][i]) - int(df2[0][1])) / 3600)

    # y1 data
    for i in range(1, df.shape[0]):
        unique_crash_1.append(int(df[7][i]))

    # y2 data
    for i in range(1, df2.shape[0]):
        unique_crash_2.append(int(df2[7][i]))

     # generate picture
    plt.title(title_name)
    plt.xlabel('Time(Hour)')
    plt.ylabel('crashes')
    plt.plot(final_time_1, unique_crash_1, color=(255/255, 100/255, 100/255), label=label_1)
    plt.plot(final_time_2, unique_crash_2, color=(100/255, 100/255, 255/255), label=label_2)
    plt.legend()
    plt.savefig(out_path)
    plt.show()
