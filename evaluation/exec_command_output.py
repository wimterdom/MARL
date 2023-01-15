#!/usr/bin/env python3
import glob
import pandas as pd
import sys

if(len(sys.argv) < 2):
    print("[Usage] python3 exec_command_output.py [input_src] [output_path]")
else:
    input_src = str(sys.argv[1])
    output_src = str(sys.argv[2])

    input_path = input_src + '/id*'
    filepath = glob.glob(input_path)

    df = pd.DataFrame(filepath)
    df = df.sort_values([0], ascending=True, ignore_index=True)
    result = pd.read_csv(df[0][0])

    b = []
    c = []
    for i in range(0, df.shape[0]):
        b.append(df[0][i])
    df2 = pd.DataFrame(b)

    for i in range(0, df2.shape[0]):
        temp = pd.read_csv(df2[0][i], header=None, index_col=None)
        c.append(temp[0][0])
    df3 = pd.DataFrame(c)
    output_path = output_src + '/multi_para_exec_command.txt'
    df3.to_csv(output_path, index=None, header=None)
