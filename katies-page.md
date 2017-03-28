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