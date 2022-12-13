import json
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import random

page = urllib.request.urlopen('https://www.nflmockdraftdatabase.com/big-boards/2023/consensus-big-board-2023')
soup = bs(page)
names = soup.body.findAll('div', {"class": "player-name player-name-smaller"})
college = soup.body.findAll('div', {"class": "player-details college-details"})
# function_names = re.findall('class="player-name player-name-smaller"', str(names))

all_players = []
qb = []
rb = []
wr = []
te = []
ot = []
iol = []
idl = []
edge = []
lb = []
cb = []
s = []

description = 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lacus vel facilisis volutpat est velit. Amet consectetur adipiscing elit duis tristique sollicitudin. At in tellus integer feugiat scelerisque varius morbi. Non blandit massa enim nec. Vel eros donec ac odio tempor. In fermentum et sollicitudin ac orci phasellus egestas. Adipiscing tristique risus nec feugiat. Blandit volutpat maecenas volutpat blandit aliquam. Urna nunc id cursus metus aliquam. Eu ultrices vitae auctor eu augue ut lectus arcu bibendum. Eget egestas purus viverra accumsan. Risus nec feugiat in fermentum posuere urna nec. Sagittis purus sit amet volutpat consequat mauris nunc. Tellus molestie nunc non blandit massa. Quis viverra nibh cras pulvinar mattis nunc sed blandit libero. Justo laoreet sit amet cursus sit amet dictum sit. Eget duis at tellus at urna condimentum mattis pellentesque. Massa tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada. Hendrerit gravida rutrum quisque non tellus orci ac. Mauris augue neque gravida in fermentum et. Dapibus ultrices in iaculis nunc sed augue lacus viverra vitae. Nec ullamcorper sit amet risus nullam eget. Nisi lacus sed viverra tellus in hac habitasse platea dictumst. Integer enim neque volutpat ac tincidunt vitae. Amet commodo nulla facilisi nullam vehicula ipsum. Id donec ultrices tincidunt arcu. Magna fermentum iaculis eu non diam. Aliquam malesuada bibendum arcu vitae elementum curabitur. Metus aliquam eleifend mi in nulla posuere. Sed enim ut sem viverra. Et netus et malesuada fames. Et pharetra pharetra massa massa ultricies mi quis hendrerit dolor. Nunc mattis enim ut tellus elementum sagittis vitae et leo. Pulvinar sapien et ligula ullamcorper malesuada proin. Nulla at volutpat diam ut venenatis tellus in metus vulputate. Habitasse platea dictumst quisque sagittis purus sit. At augue eget arcu dictum varius duis at. Dignissim enim sit amet venenatis urna cursus eget nunc. Sed euismod nisi porta lorem mollis aliquam. Sit amet dictum sit amet justo donec. Ut etiam sit amet nisl purus in. Semper eget duis at tellus at urna. Facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat. Augue mauris augue neque gravida in fermentum et sollicitudin.'

for item in names:
    item = item.text
    item = re.sub("[\(\[].*?[\)\]]", "", item).replace("'", '').replace('.','').replace('’', '')
    all_players.append([item, None, None])

i = 0
for item in college:
    item = item.text
    items_split = groups = re.search("^([A-Z]+) \| (([a-zA-Z]|\s|&)+)", item).groups()
    all_players[i][1] = items_split[0]
    all_players[i][2] = items_split[1].replace('&','')
    i += 1

for player in all_players:
    if player[1] == 'LS' or player[1] == 'K' or player[1] == 'P':
        all_players.remove(player)
    if player[1] == 'QB':
        qb.append([player[0], player[2]])
    if player[1] == 'RB':
        rb.append([player[0], player[2]])
    if player[1] == 'WR':
        wr.append([player[0], player[2]])
    if player[1] == 'TE':
        te.append([player[0], player[2]])
    if player[1] == 'OT':
        ot.append([player[0], player[2]])
    if player[1] == 'IOL':
        iol.append([player[0], player[2]])
    if player[1] == 'DL':
        idl.append([player[0], player[2]])
    if player[1] == 'EDGE':
        edge.append([player[0], player[2]])
    if player[1] == 'LB':
        lb.append([player[0], player[2]])
    if player[1] == 'CB':
        cb.append([player[0], player[2]])
    if player[1] == 'S':
        s.append([player[0], player[2]])
    if "Byron Young" in player[0]:
        player[0] = "Byron Young"


for q in qb:
    for i in range (2, 13):
        q.append(random.randint(0,5))

for r in rb:
    for i in range (2, 11):
        r.append(random.randint(0,5))

for w in wr:
    for i in range (2, 13):
        w.append(random.randint(0,5))

for t in te:
    for i in range (2, 14):
        t.append(random.randint(0,5))

for ol in iol:
    for i in range (2, 12):
        ol.append(random.randint(0,5))

for ol in ot:
    for i in range (2, 13):
        ol.append(random.randint(0,5))

for d in idl:
    for i in range (2, 13):
        d.append(random.randint(0,5))

for e in edge:
    for i in range (2, 15):
        e.append(random.randint(0,5))

for l in lb:
    for i in range (2, 13):
        l.append(random.randint(0,5))

for c in cb:
    for i in range (2, 12):
        c.append(random.randint(0,5))

for sa in s:
    for i in range (2, 13):
        sa.append(random.randint(0,5))




# print(names)

with open('/Users/jonas/python-workspace/website/nfldraft/main/fixtures/players.json', 'r+') as f:
    i = 1
    j = 1
    data = json.load(f)
    for p in qb:
        grade = round(((
            p[2]*11 + 
            p[3]*4 + 
            p[4]*9 + 
            p[5]*14 + 
            p[6] * 17 + 
            p[7]*8 + 
            p[8]*9+ 
            p[9]*7 + 
            p[10]*7 +
            p[11]*9 + 
            p[12]*5
            )/100)*20, 2)

        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            "school": p[1],
            'description': description,
            "position": "QB",
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.Quarterback",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": p[0],
            "school": p[1],
            "arm_strength": p[2],
            "size": p[3],
            "short_acc": p[4],
            "deep_acc": p[5],
            "mobility": p[6],
            "process": p[7],
            "decision": p[8],
            "athleticism": p[9],
            "mechanics": p[10],
            "anticipation": p[11],
            "ball_carry": p[12],
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j += 1 

    i = 1
    for p in rb:
        grade = round(((
            p[2]*3 + 
            p[3]*15 + 
            p[4]*20 + 
            p[5]*15 + 
            p[6]*12 + 
            p[7]*10 + 
            p[8]*10+ 
            p[9]*5 + 
            p[10]*10
            )/100)*20, 2)
        
        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "school": p[1],
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            'description': description,
            "position": "RB",
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.Runningback",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": p[0],
            "school": p[1],
            "size": p[2],
            "vision": p[3],
            "balance": p[4],
            "elusiveness": p[5],
            "speed": p[6],
            "burst": p[7],
            "pass_block": p[8],
            "fumble": p[9],
            "cod": p[10],
            # "intangebles": 
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j += 1

    i = 1
    for p in wr:
        grade = round(((
            p[2]*8 + 
            p[3]*15 + 
            p[4]*9 + 
            p[5]*11 + 
            p[6]*15 + 
            p[7]*15 + 
            p[8]*5 + 
            p[9]*5 + 
            p[10]*8 +
            p[11]*8 + 
            p[12]*2
            )/100)*20, 2)

        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "school": p[1],
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            'description': description,
            "position": "WR",
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.Widereceiver",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": p[0],
            "school": p[1],
            "size": p[2],
            "speed": p[3],
            "cod": p[4],
            "release": p[5],
            "short_routes": p[6],
            "deep_routes": p[7],
            "hands":p[8],
            "cit":p[9],
            "ball_skills": p[10],
            "rac": p[11],
            "block": p[12],
            # "intangebles": 
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j += 1

    i = 1
    for t in te:
        grade = round(((
            t[2]*7 + 
            t[3]*7 + 
            t[4]*7 + 
            t[5]*3 + 
            t[6]*15 + 
            t[7]*9 + 
            t[8]*5 + 
            t[9]*7 + 
            t[10]*7 +
            t[11]*5 + 
            t[12]*17 + 
            t[13]*8
            )/100)*20, 2)

        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "school": p[1],
            "position": "TE",
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            'description': description,
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.Tightend",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": t[0],
            "school": t[1],
            "size": t[2],
            "speed": t[3],
            "cod": t[4],
            "release": t[5],
            "short_routes": t[6],
            "deep_routes": t[7],
            "hands":t[8],
            "cit":t[9],
            "ball_skills": t[10],
            "rac": t[11],
            "run_block": t[12],
            "pass_block": t[13],
            # "intangebles": 
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j += 1

    i = 1
    for p in iol:
        grade = round(((
            p[2]*9 + 
            p[3]*12 + 
            p[4]*15 + 
            p[5]*9 + 
            p[6]*9 + 
            p[7]*14 + 
            p[8]*13 + 
            p[9]*8 + 
            p[10]*7 + 
            p[11]*6 
            )/100)*20, 2)

        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "school": p[1],
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            'description': description,
            "position": "IOL",
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.IOL",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": p[0],
            "school": p[1],
            "size": p[2],
            "pass_set": p[3],
            "run_block": p[4],
            "impact": p[5],
            "move": p[6],
            "strength": p[7],
            "athleticism":p[8],
            "hands":p[9],
            "anchor": p[10],
            "lean": p[11],
            # "intangebles": 
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j += 1

    i = 1
    for p in ot:
        grade = round(((
            p[2]*10 + 
            p[3]*13 + 
            p[4]*13 + 
            p[5]*7 + 
            p[6]*9 + 
            p[7]*10 + 
            p[8]*20 + 
            p[9]*8 + 
            p[10]*5 + 
            p[11]*5 +
            p[12]*5
            )/100)*20, 2)

        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "school": p[1],
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            'description': description,
            "position": "OT",
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.Tackle",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": p[0],
            "school": p[1],
            "size": p[2],
            "pass_set": p[3],
            "run_block": p[4],
            "impact": p[5],
            "move": p[6],
            "strength": p[7],
            "athleticism":p[8],
            "hands":p[9],
            "anchor": p[10],
            "lean": p[11],
            "kick": p[12],
            # "intangebles": 
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j += 1

    i = 1
    for p in idl:
        grade = round(((
            p[2]*7 + 
            p[3]*10 + 
            p[4]*15 + 
            p[5]*10 + 
            p[6]*8 + 
            p[7]*5 + 
            p[8]*12 + 
            p[9]*8 + 
            p[10]*10 + 
            p[11]*10 +
            p[12]*5
            )/100)*20, 2)

        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "school": p[1],
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            'description': description,
            "position": "IDL",
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.IDL",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": p[0],
            "school": p[1],
            "size": p[2],
            "strength": p[3],
            "power_rush": p[4],
            "finesse_rush": p[5],
            "getoff": p[6],
            "bend": p[7],
            "athleticism":p[8],
            "hands":p[9],
            "shed": p[10],
            "poa": p[11],
            "motor": p[12],
            # "intangebles": 
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j += 1

    i = 1
    for p in edge:
        grade = round(((
            p[2]*7 + 
            p[3]*14 + 
            p[4]*14 + 
            p[5]*14 + 
            p[6]*11 + 
            p[7]*7 + 
            p[8]*10 + 
            p[9]*5 + 
            p[10]*5 + 
            p[11]*5 +
            p[12]*3 +
            p[13]*5 +
            p[14]*3
            )/100)*20, 2)

        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "school": p[1],
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            'description': description,
            "position": "Edge",
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.Edge",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": p[0],
            "school": p[1],
            "size": p[2],
            "power_rush": p[3],
            "finesse_rush": p[4],
            "speed_rush": p[5],
            "getoff": p[6],
            "bend": p[7],
            "athleticism":p[8],
            "hands":p[9],
            "shed": p[10],
            "poa": p[11],
            "tackle": p[12],
            "motor": p[13],
            "strength": p[14],
            # "intangebles": 
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j += 1

    i = 1
    for p in lb:
        grade = round(((
            p[2]*8 + 
            p[3]*9 + 
            p[4]*8 + 
            p[5]*5 + 
            p[6]*12 + 
            p[7]*12 + 
            p[8]*12 + 
            p[9]*9 + 
            p[10]*5 + 
            p[11]*15 +
            p[12]*5
            )/100)*20, 2)

        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "school": p[1],
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            'description': description,
            "position": "LB",
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.Linebacker",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": p[0],
            "school": p[1],
            "size": p[2],
            "speed": p[3],
            "cod": p[4],
            "man": p[5],
            "zone": p[6],
            "poa": p[7],
            "process":p[8],
            "shed":p[9],
            "strength": p[10],
            "tackle": p[11],
            "blitz": p[12],
            # "intangebles": 
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j += 1

    i = 1
    for p in cb:
        grade = round(((
            p[2]*9 + 
            p[3]*20 + 
            p[4]*15 + 
            p[5]*9 + 
            p[6]*12 + 
            p[7]*10 + 
            p[8]*8 + 
            p[9]*4 + 
            p[10]*3 + 
            p[11]*10 
            )/100)*20, 2)
        
        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "school": p[1],
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            'description': description,
            "position": "CB",
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.Cornerback",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": p[0],
            "school": p[1],
            "size": p[2],
            "speed": p[3],
            "cod": p[4],
            "press": p[5],
            "man": p[6],
            "zone": p[7],
            "ball_skills":p[8],
            "rund":p[9],
            "tackle": p[10],
            "transitions": p[11],
            # "intangebles": 
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j += 1

    i = 1
    for p in s:
        grade = round(((
            p[2]*6 + 
            p[3]*14 + 
            p[4]*12 + 
            p[5]*4 + 
            p[6]*9 + 
            p[7]*16 + 
            p[8]*15 + 
            p[9]*10 + 
            p[10]*6 + 
            p[11]*4 +
            p[12]*3 
            )/100)*20, 2)

        data.append({
        "model": "main.Prospect",
        "pk": j,
        "fields": {
            "name": p[0],
            "school": p[1],
            "name_link": p[0].replace(' ', '-'),
            "school_link": p[1].replace(' ', '-'),
            'description': description,
            "position": "S",
            "grade": grade
            } 
        })
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

        data.append({
        "model": "main.Safety",
        "pk": i,
        "fields": {
            "prospect": j,
            "name": p[0],
            "school": p[1],
            "size": p[2],
            "speed": p[3],
            "cod": p[4],
            "press": p[5],
            "man": p[6],
            "zone": p[7],
            "range":p[8],
            "ball_skills":p[9],
            "rund": p[10],
            "tackle": p[11],
            "strength": p[12],
            # "intangebles": 
            "grade": grade
            } 
        })

        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        i += 1
        j+=1
    

