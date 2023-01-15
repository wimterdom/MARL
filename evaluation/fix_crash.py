from datetime import datetime, date
import pandas as pd
import matplotlib.pyplot as plt
import sys

'''
input_1 = str(sys.argv[1])
label_1 = str(sys.argv[2])
input_2 = str(sys.argv[3])
label_2 = str(sys.argv[4])
output_name = '/' + str(sys.argv[6]) + '.png'
out_path = str(sys.argv[5]) + output_name
title_name = str(sys.argv[7])
'''

# input data source
df = pd.read_csv('../out/tiff2pdf_1h/plot_data', header=None, index_col=None)
df2 = pd.read_csv('~/software_test/Yuan-fuzz/out/test_1h/plot_data', header=None, index_col=None)
df3 = pd.read_csv('~/software_test/test/test_new_reward_1204/RLFuzz_yuan/out/tiff2pdf_1h/plot_data', header=None, index_col=None)
#print(df[0][1])
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
'''
init_time = 0
df_time = []
df2_time = []
df3_time = []
unique_crash_1 = []
unique_crash_2 = []
unique_crash_3 = []

for i in range(1, df.shape[0]):
    df_time.append((int(df[0][i]) - int(df[0][1])) / 60)

for i in range(1, df2.shape[0]):
    df2_time.append((int(df2[0][i]) - int(df2[0][1])) / 60)

for i in range(1, df3.shape[0]):
    df3_time.append((int(df3[0][i]) - int(df3[0][1])) / 60)
'''
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
    final_time_1.append(seconds_1/60)
    '''
# y1 data
for i in range(1, df.shape[0]):
    unique_crash_1.append(int(df[7][i]))
'''
# x2 data
for i in range(1, len(realtime_2)):
    time_4 = realtime_2[i]
    time4_struct = datetime.strptime(time_4, "%Y-%m-%d %H:%M:%S")
    seconds_2 = (time4_struct - time3_struct).seconds
    final_time_2.append(seconds_2/60)
    '''
# y2 data
for i in range(1, df2.shape[0]):
    unique_crash_2.append(int(df2[7][i]))

# z2
for i in range(1, df3.shape[0]):
    unique_crash_3.append(int(df3[7][i]))

 # generate picture
plt.title('Tiff2pdf')
plt.xlabel('Time(Minutes)')
plt.ylabel('crashes')
plt.plot(df_time, unique_crash_1, color=(255/255, 100/255, 100/255), label='RL-adaptive')
plt.plot(df2_time, unique_crash_2, '--', color=(100/255, 100/255, 255/255), label='Yuan')
plt.plot(df3_time, unique_crash_3, color=(255/255, 0/255, 255/255), label='RL-reward')
plt.legend()
plt.savefig('../out/tiff2pdf_1h/compare_crash.png')
plt.show()
