#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:57:56 2019

@author: glauberc
"""

#Entrada
"""
4
10:00 12:00 Lectures
12:00 13:00 Lunch, like always.
13:00 15:00 Boring lectures...
15:30 17:45 Reading
4
10:00 12:00 Lectures
12:00 13:00 Lunch, just lunch.
13:00 15:00 Lectures, lectures... oh, no!
16:45 17:45 Reading (to be or not to be?)
4
10:00 12:00 Lectures, as everyday.
12:00 13:00 Lunch, again!!!
13:00 15:00 Lectures, more lectures!
15:30 17:15 Reading (I love reading, but should I schedule it?)
1
12:00 13:00 I love lunch! Have you ever noticed it? :)

"""
#Saida
"""
Day #1: the longest nap starts at 15:00 and will last for 30 minutes.
Day #2: the longest nap starts at 15:00 and will last for 1 hours and 45 minutes.
Day #3: the longest nap starts at 17:15 and will last for 45 minutes.
Day #4: the longest nap starts at 13:00 and will last for 5 hours and 0 minutes.
"""
def toHhmm(min_time):
    hours = int(min_time / 60)
    minutes = min_time % 60
    
    hh = '0' + str(hours) if hours <10 else str(hours)
    mm = '0' + str(minutes) if minutes <10 else str(minutes)
    
    return hh +':' + mm
    
def toExtendTime(min_time):
    str_time = ""
    hours = int(min_time / 60)
    minutes = min_time % 60
    
    if(hours > 0):
        str_time = str(hours) + " hours and "
    str_time += str(minutes) + " minutes"
    return str_time

def reduce(l):
    new_list = []
    for i in range(len(l)):
        init = l[i][0]
        end = l[i][1]
        for c in range(len(l)):
            if(l[c][0] <= init and l[c][1] >= init):
                if(l[c][1] >= end):
                    end = l[c][1]
                init = l[c][0]
            elif(l[c][1] >= end and l[c][0] <= end):
                if(l[c][0] <= init):
                    init = l[c][0]
                end = l[c][1]
        if([init, end] not in new_list):
            if(len(new_list) != 0):
                if(end > new_list[len(new_list)-1][1]):
                   new_list.append([init, end])
            else:
                new_list.append([init, end])
    return new_list

def getKey(el):
    return el[0]

ent = ["13:00 15:00 Lectures, more lectures!", "15:30 17:15 Reading (I love reading, but should I schedule it?)", "10:00 12:00 Lectures, as everyday.", "12:00 13:00 Lunch, again!!!"]
day = 0
n_case = 'a'
while(n_case != ''):
    n_case = input()
    if(n_case != ''):
        n_case = int(n_case)
        time1, time2 = 0, 0
        work_time = []
        day += 1
        for case in range(n_case):
            entrada = input()
            time1 = int(entrada[0] + entrada[1]) * 60 + int(entrada[3] + entrada[4])
            time2 = int(entrada[6] + entrada[7]) * 60 + int(entrada[9] + entrada[10])
            
            work_time.append([time1, time2])        
        work_time = reduce(sorted(work_time, key=getKey))
        best_nap_time = 0
        nap_time_begin = 0
        end_past = 600
        dif = 0
        
        for i in range(len(work_time)):
            dif = work_time[i][0] - end_past
            if dif > best_nap_time:
                best_nap_time = dif
                nap_time_begin = end_past
            if(i == len(work_time) - 1 and work_time[i][1] < 1080):
                dif = 1080 - work_time[i][1]
                if dif > best_nap_time:
                    best_nap_time = dif
                    nap_time_begin = work_time[i][1]
            end_past = work_time[i][1]                 
        print("Day #{}: the longest nap starts at {} and will last for {}.".format(day, toHhmm(nap_time_begin), toExtendTime(best_nap_time)))
        
        