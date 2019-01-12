# Using Received Signal Strength to estimate location

!! The maps are not loaded in the Notebooks due to the HTML format printing of GitHub. They can be found in the "Maps" section. !!

## Context
Smart devices such as IoT sensors use low energy consuming networks such as the ones provided by Sigfox or Lora. But without using GPS networks, it becomes harder to estimate the position of the sensor. The aim of this study is to provide a geolocation estimation using Received Signal Strength Indicator in the context of IoT. The aim is to allow a geolocation of lowconsumption connected devices using the Sigfox network. State of the art modelsare able to be precise to the nearest kilometer in urban areas, and around tenkilometers in less populated areas.

## Datas
The data set can be found in the repository. It is made of :
- a training set : `mess_train_list.csv` that contains a message id, the base station that received the message (if several base stations, we have several lines), as well as its latitude and longitude, and the received signal strenght.
- a complementary training set : `pthat contains for each message the exact location of the message (measured with GPS) 
- a training set : `pos_train.csv`that contains a message id, the base station that received the message (if several base stations, we have several lines), as well as its latitude and longitude, and the received signal strenght.
- a test set : `mess_test_list.csv` used for prediction.

## Metrics
The accuracy metric we are focusing on is the 80% error distance. We compute the distance between our estimate and the true position, build a cimulative distribution function out of this, and compute the 80% percentile.

## How to use it ?
The project currently is under the form of a set of Jupyter notebooks that can be found in the TP_Geoloc section.

## Results ?
There are several possible approaches for this problem :
- We can consider the longitude and the latitude as independent observations. The independence hypothesis would hold if the targets (latitude and longitude) were more or less uncorrelated. In such case, we only need to fit a regressor on the latitude, and another on the longitude.
- In our case, we can observe a certain relationship among the latitude and the longitude of the datas used. We showed that using the predicted longitude as an additional column of the latitude feature marix happened to improve our results by over 6.6%.

Overall, the ExtraTrees Regressor outperformed all other regressors. Additional work could be provided regarding Artificial Neural Networks, but larger sets of data would be needed.

## Research paper
If you are interested in the research paper we are working on currently, feel free to check out this link :
https://www.overleaf.com/read/yjvckksdtxqd

The PDF version (might not always be the latest version) is also present in the project GitHub page.
