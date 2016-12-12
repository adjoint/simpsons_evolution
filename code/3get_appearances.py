import urllib
import time
import csv
import copy
import operator

opener = urllib.URLopener()

with open('episodes.csv', 'rb') as f:
    reader = csv.reader(f)
    eps0 = map(list, reader)
    del eps0[0]
episodes = copy.deepcopy(eps0)

out = open("episode_appearances.csv", "w")
IDedges = open("edges_ID.csv", "w")
IDedges.write("id1,id2,date\n")
STRedges = open("edges_str.csv", "w")
STRedges.write("str1,str2,date\n")
errors = open("errors.csv", "w")
BIGerrors = open("big_errors.csv", "w")
chars = open("characters.csv", "w")

characters = {}

counter = 1
charID = 1000
for e in episodes:
    print counter
    counter += 1
    #print e
    ID = e[0]
    title = e[1]
    link = "http://simpsons.wikia.com" + e[2] + "/Appearances"
    date = e[3].strip(" ")
    #print ID
    if int(ID) == 484:
        episode_characters_IDs = []
        episode_characters = []
        char_list = ["Homer Simpson", "Marge Simpson","Lisa Simpson","Bart Simpson","Fit Tony (Fat Tony)","Louie","Legs","Johnny Tightlips","Frankie the Squealer","Clancy Wiggum","Selma","Patty","Luigi Risotto","Spider-Pig","Fit/Fat Tony's Nephews and Niece","Lenny Leonard","Carl Carlson","Unnamed girl with red glasses"]
        for name in char_list:
            if name not in characters:
                characters[name] = (charID, date)
                charID += 1
            episode_characters_IDs.append(characters[name][0])    
            episode_characters.append(name)
            out.write(str(ID) + "," + str(title) + "," + str(date) + ",")
            for i in range(len(episode_characters_IDs)):
                out.write(str(episode_characters_IDs[i]) + ",")
                for j in range(i+1, len(episode_characters_IDs)):
                    IDedges.write(str(episode_characters_IDs[i]) + "," + str(episode_characters_IDs[j]) + "," + date + "\n")
                    STRedges.write(str(episode_characters[i]) + "," + str(episode_characters[j]) + "," + date + "\n")
            out.write("\n")
    else:
        try:
            f = urllib.urlopen(link)
            data = f.read()
            str1 = 'id="Characters">'
            str2 = '>Add a photo to this gallery<'
            str3 = '<div class="lightbox-caption"'
            #str3 = '<div class="lightbox-caption" style="width:140px;">'
            #data1 = data.split(str1)[1]
            data2 = data.split(str2)[0]
            data3 = data2.split(str3)[1:]
            episode_characters_IDs = []
            episode_characters = []
            if data3 == []:
                str4 = "<ul><li>"#'class="sprite edit-pencil"'
                data4 = data.split(str4)[1]#[2]
                data5 = data4.split("</ul>")[0]
                data6 = data5.split("<li>")[1:]
                for d in data6:
                    try:
                        link = d.split('<a href="')[1].split('"')[0]
                        #print link
                        name = d.split('title="')[1].split('"')[0].replace(",", "") 
                        #name = '"' + name.strip(" (page does not exist)") + '"'
                        if name not in characters:
                            characters[name] = (charID, date)
                            charID += 1
                        episode_characters_IDs.append(characters[name][0])    
                        episode_characters.append(name)
                    except IndexError:
                        errors.write(str(ID) + "\n" + str(d) + "\n\n")
            else:
                for d in data3:
                    try:
                        try:
                            link = d.split('<a href="')[1].split('"')[0]
                            name = d.split('title="')[1].split('"')[0].replace(",", "") 
                        except IndexError:
                            name = d.split('>')[1].split('<')[0].replace(",", "")
                        #name = '"' + name.strip(" (page does not exist)") + '"'
                        if name not in characters:
                            characters[name] = (charID, date)
                            charID += 1
                        episode_characters_IDs.append(characters[name][0])    
                        episode_characters.append(name)
                    except IndexError:
                        str4 = "<ul><li>"#'class="sprite edit-pencil"'
                        data4 = data.split(str4)[1]#[2]
                        data5 = data4.split("</ul>")[0]
                        data6 = data5.split("<li>")[1:]
                        for d in data6:
                            try:
                                link = d.split('<a href="')[1].split('"')[0]
                                name = d.split('title="')[1].split('"')[0].replace(",", "") 
                                #name = '"' + name.strip(" (page does not exist)") + '"'
                                if name not in characters:
                                    characters[name] = (charID, date)
                                    charID += 1
                                episode_characters_IDs.append(characters[name][0])    
                                episode_characters.append(name)
                            except IndexError:
                                errors.write(str(ID) + "\n" + str(d) + "\n\n")
            out.write(str(ID) + "," + str(title) + "," + str(date) + ",")
            for i in range(len(episode_characters_IDs)):
                out.write(str(episode_characters_IDs[i]) + ",")
                for j in range(i+1, len(episode_characters_IDs)):
                    IDedges.write(str(episode_characters_IDs[i]) + "," + str(episode_characters_IDs[j]) + "," + date + "\n")
                    STRedges.write(str(episode_characters[i]) + "," + str(episode_characters[j]) + "," + date + "\n")
            out.write("\n")
            #time.sleep(1)
        except IndexError:
            BIGerrors.write(str(ID) + "\n")

for char in characters.keys():
    chars.write(str(characters[char][0]) + "," + str(characters[char][1]) + "," + str(char) + "\n")
#sorted_characters = sorted(characters.items(), key=operator.itemgetter(1))
#print sorted_x
#for char in sorted_characters:
    #chars.write(str(char[1]) + "," + str(char[0]) + "\n")
print str(charID-1)
            
out.close()
IDedges.close()
STRedges.close()
