# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn.model_selection import GridSearchCV
# grid-search 
from sklearn.model_selection import RandomizedSearchCV

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 1200, stop = 2000, num = 8)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(70, 110, num = 8)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2,3, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4, 8]


param_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
print(random_grid)

clf_lat2 = RandomForestRegressor()
clf_lng2 = RandomForestRegressor()

# Instantiate the grid search model
clf_lat_CV2 = GridSearchCV(estimator = clf_lat2, param_grid = param_grid, 
                          cv = 3, n_jobs = -1, verbose = 2)
clf_lng_CV2 = GridSearchCV(estimator = clf_lng2, param_grid = param_grid, 
                          cv = 3, n_jobs = -1, verbose = 2)