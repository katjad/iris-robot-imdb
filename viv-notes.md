## Preprocessing & Visualisation for Country

## Preprocessing
- country_adj
- dominant_lang

## Pass 1
- Categories (UK, United States, Other) in to country_adj
- Removed country

## Pass 2
- Categories (English, Spanish, Other) in to dominant_lang

## Now what? - as of 20th March
- E-mailed team as not sure how to proceed - need a stripped down data set to make meaningful visualisations? 

## NOTES
- Country is not necessarily the measure we think it is - lots of films in other languages (177) for instance
- As a poss response did pre-processing for dominant language (dominant_lang)
- Mac .csv can't be read in pandas - save as microsoft .csv

## Working on Visualisation - 27th March

- Lots of teething troubles and entirely avoidable errors - but this is helping me get to grips with what different functions do
- Managed to get the csv to load, convert to tsv, add headings etc
- Selected four categories of interest to contrast against country_adj - Number of Votes, Number of reviews, budget & score
- Removed any rows with blanks for any to keep the data clean-ish (lots of NaN displayed otherwise and I didn't know what this would do to any plots
- Finally managed to get a plot to run with just country_adj vs budget. However the budget numbers have so much variance yet start so high, I may have to decimalise it somehow.

## Working on Visualisation - 28th March

- I think I have a problem in that the four data types I am using are so different - even though they are all numbers, they are different orders, (millions vs single digits). So Boxplot does something supremely unhelpful, specifically because of the vast size of budgets. I will potentially try again with an artificially reduced budget figure (divide it by 1million?)
- The pairplot has revealed a few interesting things. A couple of unexpected correlations, but also some mega outliers, which I assume are faulty data (e.g. a Hungarian film that apparently had a budget of $2.5 billion that only took £190k in box office) - I assume we take these out, but wanted to check with you both first.

