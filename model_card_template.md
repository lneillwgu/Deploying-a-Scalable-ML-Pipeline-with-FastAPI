# Model Card


## Model Details
This is developed by Lindsey Neill for Udacity ML DevOps course, completed on May 3rd, 2024.  This model uses the AdaBoostClassifier.

## Intended Use
The intended use of this model is for the prediction of salary category of less than or equal to $50k per year or greater than $50k per year.  This prediction allows a charity to predict potential donors. 

## Training Data
The data was obtained from  https://archive.ics.uci.edu/dataset/20/census+income.   I used train_test_split to select 75% of the data for model training. 

## Evaluation Data
The data was obtained from  https://archive.ics.uci.edu/dataset/20/census+income.   I used train_test_split to select 25% of the data for model testing. 

## Metrics
The metrics from this model were:
Precision: 0.7746,  Recall 0.6225, F1: 0.6902

## Ethical Considerations
This data has been aggregated and anonymized,  so there are no privacy concerns with this data set.    

## Caveats and Recommendations
The data used in this model is from 1994, which makes it approximately 30 years old.  This data, while useful for exploration and practice building models, would be significantly out of date for any current prediction of likely donors.   Inflation has likely greatly changed the threshold for income for those who are likely donors vs those who are not, so those variables would need to be revisted and salary categories adjusted before the model could be used on modern data. 
