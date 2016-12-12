f = open("episodes_link.txt", "r")

data = f.read()

out = open("episodes.csv", "w")
out.write("ID,title,link,date\n")

#print data[:500]

episodes = data.split("<tr>")[2:]

i = 1
for e in episodes:
    try:
        link = '"' + e.split('<a href="')[1].split('"')[0] + '"'
        title = '"' + e.split('title="')[1].split('"')[0] + '"'
        date = e.split('<center>')[1].split('</center>')[0].replace(",", "")
        out.write(str(i) + "," + str(title) + "," + str(link) + "," + str(date) + "\n")
        i+=1
    except IndexError:
        print e
        break
    
f.close()
out.close()
    
    
