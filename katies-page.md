Pre-processing data for looking at Facebook likes:
 - Had to delete a lot (~2k!) entries with 0 likes
 - Sorted by facebook likes and ranked - found 25%/75% rank with which to assign low/medium/high labels

Data visualisation
 - Managed to plot gross against likes labelled and colour coded with high/medium/low (line In[18] of notebook) but this took quite 
 some messing around with googling stuff on using pandas
- Went to tutorial on predicting movie score and saw use of correlation matrix on quantitative data only - can calculate this easily
using df.corr(). Used seaborn heatmap plot - possible correlations with num_cfritic, actor3_facebook, gross, num_voted, cast_total,
num_user, actor2_facebook, imdb_score. Question remains on how to do qualitative data? Example cose here: 
http://seaborn.pydata.org/examples/network_correlations.html
- NB had an issue of not seeing plots inside jupyter, this was due to needing comman 'matlib plot inline'
- Saving seaborn plots from within Jupyter - tried various methods of savefig but didn't seem to be working, actually looks like command
was just taking a long time to process so shutdown and re-opened notebook. This worked although output figure isn't great.

Feature Analysis
- Would like to know how to pick features to use in classifier based on correlation matrix. Useful webpage: 
http://blog.datadive.net/selecting-good-features-part-i-univariate-selection/
- Suggests that the df.corr() method (which I think by default uses pearson correlation} is fine but note only shows up linear 
relationships. Might therefore be worth plotting each individual feature anyway. Or perhaps trying one of those big seaborn matrix plots
with labelled data? To answer the question on how to pick features, probably we have to just go through the matrix and decide a selection
criteria based on their correlation values. 
- Tried to do sns.pairplot on all of the (labelled) quantitative data. First got an error to do with minimum values and histrograms - it 
seems that the histogram plotting doesn't like empty values so tried putting zeros in all blank cells in excel. Worked! Now have a pair 
plot for all quant data with labelled number of facebook likes (low/medium/high). This is a huge graph! Now need to go through it and 
figure out what it means. Diagnals are just individual features versus facebook likes right? I.e. how does the frequency of high/medium/low
facebook likes spread over the various values of that feature. So that's good for individual checking of feature importance.
- Next steps: what can we gain from that huge pairplot and how can we approach qualitative data (Katja's python script likely to be useful
here)

Feature Analysis Cont.
- Tried to access elements of correlation matrix to plot a bar chart and see which correlations are above a certain value (say 0.7) in order for inclusion in classifier. Proved difficult to access matrix elements in an easy way - i.e. to create an array based on one column of the matrix (tried standard matrix[:,1:-1] as well as .iloc and neither seemed to work right). Will go ahead and just try knn classifier based on all quantitative data. Cheaty solution/workaround would possibly be to import the correlation matrix into excel and manipulate it there and reimport.
- Knn classifier as used in class achieved 54.8% accuracy based on all quantitative data. Would now be really interested to re-run with selected, higher correlation data. Rough job would be to pick out correlations by eye (heatmap diagram and checking matrix numbers), manipulating csv in excel to delete irrelevant info and re-importing -> 'reduced_quant_only_movie_metadata.csv'
- Stat with correlations > 0.5 - this would feature set of num_critic_reviews, num_voted_users, num_users_reviews only. Decided to also include gross at 0.499. Improved the knn classifier accuracy to 60.2%. 

Qualitative Features Analysis
- Used Katjas script to produce a CSV of title, genres list and facebook likes. Then used another script to find total low/medium/high rated films for each genre. Need to go through this and figure out which (if any) genres are relevant to face book likes. 
- As proof of concept for dealing with qualitative data - Viv suggested taking Katja's yes/no type csv and made it binary 1s and 0s and then put that as raw data into quantiative knn classifier training. Found it slightly reduced accuracy - but as proof of concept discrete qualitative categories can be turned into quantitative data. Next question - what about data like actors and directors?

Workshop Day 5
- Did some python scripting with Katja to produce a two column data set with all genres and scores/facebook likes next to them, matching the iris data set layout such that we could make boxplots from them. 
- Spoke to Chew-Yean about the classifier and she suggested getting rid of the data with gross=0 and then normalising the remaining data and re-running the classifier to see if that improves accuracy; the huge difference in scales between gross and number of reviews for example will mess up knn which is distance based. 
