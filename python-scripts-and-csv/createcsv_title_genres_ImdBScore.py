'''
This creates a csv file with row 1: Title, rows 2 - 22: Genres, row 23: ImdB Score
'''
import csv

genres = ["Action","Adventure","Fantasy","Sci-Fi","Thriller","Documentary","Romance","Animation","Comedy","Family","Musical","Mystery","Western","Drama","History","Sport","Crime","Horror","War","Biography","Music"]

with open("movie_metadata.csv", newline='') as f:
    with open("title_genre_ImdbScore.csv", "w", newline='') as f1:
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(f1, delimiter=',')
        for row in reader:
            genres_list = row[9].split('|')
            genres_cols = []
            for x in genres:
                if x in genres_list:
                    val = 'yes'
                else:
                    val = 'no'
                genres_cols.append(val)
            title = row[11].strip()
            all_cols = [title] + genres_cols + [row[25]]
            # print(all_cols)
            writer.writerow(all_cols)
