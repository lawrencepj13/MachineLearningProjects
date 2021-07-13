#factor analysis
import pandas as pd
import matplotlib.pyplot as plt
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo
from pandas import read_csv
from sklearn.decomposition import FactorAnalysis
from sklearn.impute import SimpleImputer

print('Testing Factor Analysis')

#load your data into a dataframe
header_names =['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'diab_class']
my_data = read_csv(r'C:\Users\Lawre\Documents\MSc Applied AI\AE1 - AI and Business - Mental Health\pima_indians_diabetes_2.csv', names=header_names)

#get dimension
print('dimension:', my_data.shape)

#get row with empty values from data frame
empty_value_data = my_data[my_data.isna().any(axis=1)]
print(empty_value_data)
print(len(empty_value_data), '\n ----------empty rows of diabetic data----------\n')

#use the simple imputer function to replace the missing values
imputer = SimpleImputer(strategy='most_frequent')#replace with median, mean and observe
imputer.fit(my_data)
my_data = imputer.transform(my_data)

#normalisethedataset
#normalisecodehere

#convert data back to frame and bind the headers
my_data = pd.DataFrame(my_data, columns = header_names)

#extract the X data - independent variables
X_data=my_data.drop(['age'], axis=1) #for regression
X2_data=my_data.drop(['diab_class'], axis=1) #for classification

print('---------Computing Factor Analysis------------\n')
#checking for factorability
#calculate the chi2 value and the p-value - bartletts test of spherity check
#p-value less than .05 represents statistical significance hence employ a factor analysis
chi_square_value, p_value=calculate_bartlett_sphericity(X_data)
print('\nChi2 Value:', chi_square_value, '\nP-Value:', p_value)

#check the data suitability for factor analysis
kmo_all, kmo_model=calculate_kmo(X_data)
print('\nKMO:', kmo_model)# values usually between 0 and 1 = kmo, below 0.6 are considered inadequate for FA

print('\n Confirming the X Data:\n', X_data.head(2))

#implement factor analysis using the factor analyser
fa=FactorAnalyzer()
transformed_X = fa.fit(X_data)

#getting the eigenvalues
eigen_values, vectors = fa.get_eigenvalues()
print('\nEigen Values:', eigen_values, '\nVectors: \n', vectors)# eigen values greater than1  are considered fact

#create the Screen plot for cecking number of factors
plt.scatter(range(1, X_data.shape[1]+1), eigen_values)
plt.plot(range(1, X_data.shape[1]+1), eigen_values)
plt.title('Screen Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

#load the factors
loadings = fa.loadings_ #we can consider features above 0.5 as high, loading rule of thumb = 0.7
new_factor = pd.DataFrame(loadings, columns = ['Factor1', 'Factor2', 'Factor3'])
print(new_factor)

#get factors variance
fac_variance = fa.get_factor_variance()
print('\n Factors Variance', fac_variance)

#confirmatory factor analysis setting the numbers of factors
FA = FactorAnalysis(n_components=3, random_state=1)
transformed_X = FA.fit_transform(X_data.values)
print(transformed_X.Shape)

#plotting factors on 2d chart
plt.figure(figsize=(8,8))
plt.title('Factor Analysis Components')
plt.scatter(transformed_X[:, 0], transformed_X[:,1])
plt.scatter(transformed_X[:, 1], transformed_X[:,2])
plt.scatter(transformed_X[:, 2], transformed_X[:,0])
plt.show()