# import all the important libraries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pickle 

from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, plot_confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier

"""## load the dataset """

# specified the join path to read excel file, this will return DryBeanDataset/Dry_Bean_Dataset.xlsx
path = os.path.join("DryBeanDataset","Dry_Bean_Dataset.xlsx")

dry_bean = pd.read_excel(path)
dry_bean.head() # used head function to read in a view a few lines of data

# info function return the data type information and number of observation 
dry_bean.info()

"""* From the info() function above, it shows that there are 13611 number of observation with 17 attributes. It also indicates that there is not null value as the number of observation for each attributes are the same. 
* In all of the 17 attributes, there are 14 floating64 data type, 2 int64 type and 1 object types which is mainly a categorical data. 

"""

dry_bean.describe()

"""The describe() function shows the main descriptive statistics for quantitative data, includes, mean, standard deviation, min, max, median, 1st Quartile and 3rd Quartile. 
The 25% is the first quartile. For example, in the Area attributes, 25% = 36328 which mean that 25% of the area is less than 36328. The third quartile is the 75%. This descriptive statistics shows that all data are not in the same measurement which mean we will need to do a standard scaler later.  
"""

dry_bean.describe(include=object)

"""This show that there are 7 category in the Class attribute which is the categorical data. The most frequent category is DERMASON which occurs 3546 times. """

dry_bean.isnull().sum() # check for na

"""isnull() function check for any null value in each of the attributes and sum() function will add all of them up. In this case, it return 0, so there is no NA in this dataset.

## Visualize the data
"""

dry_bean.hist(figsize=(16,12))
plt.suptitle("Histogram for Numerical Data", size=14)
plt.show()

"""From the histogram of all the quantitative data, we can see that most of the attributes distribution is not normal distribution(bell-shaped). They are more likely to be either left-skewed or right-skewed. Except AspectRation and Compactness seem to be normal. Therefore, we will need to make it to be normal distribution later.

### Selecting 6 features
"""

sns.pairplot(dry_bean, 
             x_vars=["Area","AspectRation","Eccentricity","MinorAxisLength","EquivDiameter","roundness"],
             y_vars=["Area","AspectRation","Eccentricity","MinorAxisLength","EquivDiameter","roundness"],
             hue="Class",)
plt.show()

"""From the plot above, it shows different scatter plot for different pairs. 
For example, like the Area and AspectRation, the color shows the different classes. the hue() in the pairplot function will classify the number into each classes. 

We can see that there is a clear positive correlation between Area and Minor Axislength as well as MinorAxisLength and EquivDiameter. Moreover, some other features such as Equivdiameter and roundness shows some positive realationship but it is not a really clear.

## Data Imbalance
"""

# use function to check number of instances Class column 
dry_bean["Class"].value_counts()

fig, axes = plt.subplots(figsize=(12,8))
sns.countplot(x=dry_bean["Class"],ax=axes)
plt.show()

"""Value_counts() function count the number of instances in the Class attribute. This shows that the data is imbalance. The main category in this class is DERMASON which has 3546 occurence and the least category in this class is BOMBAY has 522 occurence.

## Split train, test set
"""

# split the dataset into train test dataset which train 80% of the data and test 20% of the data 
db_train , db_test = train_test_split(dry_bean,test_size=0.2,random_state=42)

# split the train set into x(independent) variable and y(dependent) variable
y_train = db_train["Class"] 
X_train = db_train.iloc[:,0:-1]

# split the test set into x(independent) variable and y(dependent) variable
y_test = db_test["Class"]
X_test = db_test.iloc[:,0:-1]

# check the instance in the training set 
len(db_train)

"""There are 10888 instances that have been splitted from the 13611 overall dataset, used for training which is around 80% of the dataset. """

# check the instance in the testing set 
len(db_test)

"""There are 2723 instances that have been splitted from the 13611 overall dataset, which is around 20% of the dataset, used for checking performance of the model on how it perform on a new dataset versus on a training dataset .

## Feature Scaling
"""

# standardize the dataset 
scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test) # we only need to transform because the StandardScaler function already see the data
with open('./backend/scaler', 'wb') as files:
    pickle.dump(scaler, files)

"""Support vector machine (SVM) occurs by minimizing the decision W, the optimal hyperplan is influenced by the scale of input features and it is therefore recommended that data be standardized either through the min-max scaling between 0 and 1 or standardscaler with mean 0 and standard deviation 1.

## SVC_model
"""

svc_model = SVC(kernel="rbf")
svc_model.fit(X_train_scale, y_train) 
with open('./backend/svc_model', 'wb') as files:
    pickle.dump(svc_model, files)
# fit the dataset into svc model using rbf kernel

# create a function for doing cross validation for scoring accuracy
def cross_validation(model,x,y,k):
    return cross_val_score(model,x,y,cv=k,scoring="accuracy")

cross_validation(svc_model,X_train_scale,y_train,3)

"""Cross-validation is used in order to avoid the model overfitting. So in this case, the data will split into 3 sets and each set will be passed into svc_model and check for accuracy score. The results look quite good, seems that the model is not overfitting. However, this is only a training set not testing set. """

# predict on testing set 
print(X_test_scale)
y_test_pred = svc_model.predict(X_test_scale)

confusion_matrix(y_test,y_test_pred)

fig , ax = plt.subplots(figsize=(10,10))
plot_confusion_matrix(svc_model,X_test_scale,y_test,cmap="coolwarm",ax=ax,values_format="d")
plt.show()

"""From the confusion matrix, the diagonal shows the number of instances that our models able to predict correctly. The darker of red color, the higher the model can predict correctly. Compare the number the model predicted correctly, to the actual number, we can see the model predict give quite a good result. For example, the category "BARBUNYA" predicted to be 240 and actual values are 261 and the BOMBAY categorical predict all correct.

## Stochastic Gradient Classifier
"""

sgd_clf = SGDClassifier(max_iter=1000,tol = 1e-3, random_state=42)
sgd_clf.fit(X_train_scale,y_train)
# used the sgd-classifier model with max_iter 1000 and tol(represent the stopping criterion for iteration)

cross_validation(sgd_clf,X_train_scale, y_train,3)

"""The cross validation for sgd_classifer is lower compared to the svc_model, however, model also seem to show that it is not overfitting. """

# make prediction on the test set 
y_test_predsgd = sgd_clf.predict(X_test_scale)

confusion_matrix(y_test,y_test_predsgd)

fig, ax = plt.subplots(figsize=(10,10))
plot_confusion_matrix(sgd_clf,X_test_scale, y_test, cmap="coolwarm",ax=ax,values_format="d")
plt.show()

"""From the confusion matrix, the diagonal shows the number of instances that our models able to predict correctly. The darker of red color, the higher the model can predict correctly. Compare the number the model predicted correctly, to the actual number, we can see the model predict give quite a good result. For example, the category "BARBUNYA" predicted to be 230 and actual values are 261 and the BOMBAY categorical predict all correct.

According to the classification report, the precision score and recall score for sgd classifier seem to be lower compare to svc_model, however, the score seem resonably good.

## Comparision
"""

# create a function to plot the 2 confusion matrix together 
def plot_2_cf_matrix(model1,X,model2,y):
    fig, axes = plt.subplots(1,2,figsize=(19,10))
    ax1= plot_confusion_matrix(model1,X,y,cmap="coolwarm",ax=axes[0],values_format="d")
    ax2= plot_confusion_matrix(model2,X,y, cmap="coolwarm",ax=axes[1],values_format="d")
    ax1.ax_.set_title("Support Vector Classifier")
    ax2.ax_.set_title("Stochastic Gradient Descent")
    plt.suptitle("Confusion Matrix for 2 Model",size=16)
    plt.show()

plot_2_cf_matrix(svc_model,X_test_scale,sgd_clf,y_test)

"""Comparing confusion matrix between the 2 model, we can see that both of the model perform similar, as there is only a small difference.Both of the model is good for using in high dimensional space like our dataset. 
* However, in general, we can see that support vector classifier model is 
perform better compared to the Stochastic Gradient Descent. According to the graph, it shows that overall the diagonal part which is the true positive is higher for support vector classifier compare to stochastic gradient descent. 
* Moreover, for stochastic gradient descent there is a wrong prediction in Barbunya, which the model predicted it to be Horoz.
* However, for support vector classifier, there is a wrong prediction in Horoz 
which the model predicted it to be Barbunya. 
* This might be due to the 2 types of beans have a lot of similar features. 
"""

def display_metric(model1,y_true,y_pred1,model2,y_pred2):
    print("Metrics score for: {0} ".format(model1))
    print("Accuracy {0}".format(accuracy_score(y_true,y_pred1)))
    print("Metrics score for: {0}".format(model2))
    print("Accuracy {0}".format(accuracy_score(y_true,y_pred2)))

display_metric("SVC",y_test,y_test_pred,"SGD Classifier",y_test_predsgd)

"""In summary, when we compared the overall accuracy score for 2 model, it shows that SVC model seem to outperform the SGD Classifiers. """