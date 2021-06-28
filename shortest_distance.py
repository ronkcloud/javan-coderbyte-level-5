inf = float('inf')
conn = {'A':{'B':6, 'D':1},
        'D':{'A':1, 'B':2, 'E':1},
        'B':{'A':6, 'D':2, 'E':2, 'C':5},
        'E':{'D':1, 'B':2, 'C':5},
        'C':{'B':5, 'E':5}}

conn = {'A':{'B':1, 'D':1},
        'D':{'A':1, 'B':1, 'E':1},
        'B':{'A':1, 'D':1, 'E':1, 'C':1},
        'E':{'D':1, 'B':1, 'C':1},
        'C':{'B':1, 'E':1},
        'F':{'G':1},
        'G':{'F':1}}

res = {'A':{'dist':0, 'prev':'start'},
       'B':{'dist':inf, 'prev':None},
       'C':{'dist':inf, 'prev':None},
       'D':{'dist':inf, 'prev':None},
       'E':{'dist':inf, 'prev':None},
       'F':{'dist':inf, 'prev':None},
       'G':{'dist':inf, 'prev':None}}

visited =['','','','']
unvisited =['A','B','D','C']


def shortest_distance(res, conn, visited=[]):
    # visit the unvisited vertex with the smallest dist

    if len(visited) == len(conn):
        return res

    smallest = {'key':None, 'smallest': float('inf')}

    for i in res:
        if i not in visited and res[i]['dist'] <= smallest['smallest']:
            smallest['key'] = i
            smallest['smallest'] = res[i]['dist']
    
    key = smallest['key']

    # key = A dist = 0
    #examine the unvisited neighboor of current vertex
    for i in conn[key]:
        calculated = res[key]['dist'] + conn[key][i] 
        if i not in visited and calculated <= res[i]['dist']:
            res[i]['dist'] = calculated
            res[i]['prev'] = key
    
    visited.append(key)

    return shortest_distance(res, conn, visited=visited)

short_dist = shortest_distance(res, conn)
print (short_dist)


def trace(endval, data, startval, path=[]):
    path.append(endval)
    if data[endval]['prev'] == None:
        return 'no path'
    if endval == startval:
        return path
    return trace(data[endval]['prev'], data, startval, path)

res = trace('G', short_dist, 'A')
print (res)

""""
1. For input ["2","First Street","Third Street"] the output was incorrect. The correct output is -1

2. For input ["7","D","A","N","I","E","L","B","D-A","A-N","E-B","E-L"] the output was incorrect. The correct output is -1
"""