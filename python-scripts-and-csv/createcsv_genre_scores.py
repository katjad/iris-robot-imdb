'''Creates a csv with really long rows - Genre plus the scores that have been given for each film in that genre. Variable col numbers'''
import csv

genres = ["Action","Adventure","Fantasy","Sci-Fi","Thriller","Documentary","Romance","Animation","Comedy","Family","Musical","Mystery","Western","Drama","History","Sport","Crime","Horror","War","Biography","Music"]

d = dict()

def getMaxLength(d):
    maxlength = 0
    for key, value in d.items():
        xlen = len(value)
        if xlen > maxlength:
            maxlength = xlen
    return maxlength

def generateList(maxlength):
    incrlist = []
    for x in range(maxlength):
        incrlist.append(x)
    return incrlist


with open("movie_metadata.csv", newline='') as f:
    with open("genre_scores.csv", "w", newline='') as f1:
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(f1, delimiter=',')
        for row in reader:
            genres_list = row[9].split('|')
            genres_cols = []
            for x in genres:
                if x in genres_list:
                    if x not in d:
                        d[x] = [row[25]]
                    else:
                        d[x].append(row[25])
        maxlength = getMaxLength(d)
        print(maxlength)
        headercols = generateList(maxlength)
        # print(generateList(maxlength))        
        writer.writerow(['Genre']+headercols)
        for key, value in d.items():
            last = value[-1]            
            #print([key]+[value])
            writer.writerow([key]+value)
