from operator import itemgetter    

# for analysing plot keywords:
with open("plotkeywords_column.txt") as f:
    with open("plotkeywords_counted.txt", "w") as f1:
# with open("genre_column.txt") as f:
#     with open("genre_counted.txt", "w") as f1:
        d = dict()
        for line in f:
            genre_list = line.split('|')
            genre_list = [i.strip() for i in genre_list]          
            # print(genre_list)
            for x in genre_list:
                if x not in d:
                    d[x] = 1
                else:
                    d[x] +=1
        dc_sort = sorted(d.items(),key = itemgetter(1),reverse = True)
        f1.write('\n'.join('%s %s' % x for x in dc_sort))
