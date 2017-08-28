#!/usr/bin/env python3


# TSbin - Convert time series into binary sequences.
# Copyright (C) 2017 João Baptista <baptista.joao33@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import csv
import argparse


def convert_csv(csv_file):
    """
    Reads the CSV and converts the name of the songs into dict keys and time series into values.
    """

    song_ts = {}
    
    with open(csv_file) as f:
        f_csv = csv.reader(f)
        f_list = list(f_csv)
        for row in f_list:
            song_ts[row[1]] = []
        for row in f_list:
            song_ts[row[1]].append(row[3])
            song_ts[row[1]].append(row[4])

    return song_ts

def measure(dict_ts, number):
    """
    Subtrates the end and start of time series and measures the distance between time series. 
    """

    song_dist = {}

    for k in dict_ts.keys():
        song_dist[k] = [str(round((float(dict_ts[k][val+1]) - float(dict_ts[k][val])) / number)) for val in range(0,len(dict_ts[k])-1)]

    return song_dist


def binary(dict_dist):
    """
    Transforms the time series in "1" and the distances between time series into "0".
    """
    
    song_seq = {}
    
    for k in dict_dist.keys():
        song_seq[k] = ""
        for n in range(0,len(dict_dist[k])):
            if n == 0:
                song_seq[k] += str("I " * int(dict_dist[k][n]))
            elif n % 2 == 0:
                song_seq[k] += str("I " * int(dict_dist[k][n]))
            else:
                song_seq[k] += str("O " * int(dict_dist[k][n]))

    return song_seq

def write(dict_seq, output):
    """
    Write the sequences in tsv format.
    """
    
    with open(output,"w+") as f:
        for k,v in dict_seq.items():
            f.write(k+"\t"+v+"\n")

def main():
    """
    Argument parser and handler
    """
    
    # Argument parser

    parser = argparse.ArgumentParser(description='Converts time series into binary sequences.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file.')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output file.')
    parser.add_argument('-n', '--number', type=float, default=0.01, help='Number to divide the distances.')
    args = parser.parse_args()

    # Argument handler

    func_convert = convert_csv(args.input)
    func_measure = measure(func_convert, args.number)
    func_binary = binary(func_measure)
    write(func_binary, args.output)

if __name__ == "__main__":
    main()
