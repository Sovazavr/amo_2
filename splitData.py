{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d94f35ef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order</th>\n",
       "      <th>Property Id</th>\n",
       "      <th>DOF Gross Floor Area</th>\n",
       "      <th>Year Built</th>\n",
       "      <th>Number of Buildings - Self-reported</th>\n",
       "      <th>Occupancy</th>\n",
       "      <th>Site EUI (kBtu/ft²)</th>\n",
       "      <th>Weather Normalized Site Electricity Intensity (kWh/ft²)</th>\n",
       "      <th>Weather Normalized Site Natural Gas Intensity (therms/ft²)</th>\n",
       "      <th>Water Intensity (All Water Sources) (gal/ft²)</th>\n",
       "      <th>...</th>\n",
       "      <th>Largest Property Use Type_Retail Store</th>\n",
       "      <th>Largest Property Use Type_Self-Storage Facility</th>\n",
       "      <th>Largest Property Use Type_Senior Care Community</th>\n",
       "      <th>Largest Property Use Type_Social/Meeting Hall</th>\n",
       "      <th>Largest Property Use Type_Strip Mall</th>\n",
       "      <th>Largest Property Use Type_Supermarket/Grocery Store</th>\n",
       "      <th>Largest Property Use Type_Urgent Care/Clinic/Other Outpatient</th>\n",
       "      <th>Largest Property Use Type_Wholesale Club/Supercenter</th>\n",
       "      <th>Largest Property Use Type_Worship Facility</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>15</td>\n",
       "      <td>2637863</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1903</td>\n",
       "      <td>2</td>\n",
       "      <td>100</td>\n",
       "      <td>32.0</td>\n",
       "      <td>7.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>51.01</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>93.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>20</td>\n",
       "      <td>2777309</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1907</td>\n",
       "      <td>7</td>\n",
       "      <td>100</td>\n",
       "      <td>120.0</td>\n",
       "      <td>8.7</td>\n",
       "      <td>0.9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>21</td>\n",
       "      <td>2780056</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1939</td>\n",
       "      <td>2</td>\n",
       "      <td>100</td>\n",
       "      <td>76.2</td>\n",
       "      <td>3.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>18.40</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>72.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>22</td>\n",
       "      <td>4988574</td>\n",
       "      <td>179130.0</td>\n",
       "      <td>1939</td>\n",
       "      <td>1</td>\n",
       "      <td>100</td>\n",
       "      <td>75.7</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>67.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>23</td>\n",
       "      <td>4988569</td>\n",
       "      <td>102150.0</td>\n",
       "      <td>1939</td>\n",
       "      <td>1</td>\n",
       "      <td>100</td>\n",
       "      <td>77.1</td>\n",
       "      <td>2.6</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>80.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 65 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Order  Property Id  DOF Gross Floor Area  Year Built  \\\n",
       "0     15      2637863                   NaN        1903   \n",
       "1     20      2777309                   NaN        1907   \n",
       "2     21      2780056                   NaN        1939   \n",
       "3     22      4988574              179130.0        1939   \n",
       "4     23      4988569              102150.0        1939   \n",
       "\n",
       "   Number of Buildings - Self-reported  Occupancy  Site EUI (kBtu/ft²)  \\\n",
       "0                                    2        100                 32.0   \n",
       "1                                    7        100                120.0   \n",
       "2                                    2        100                 76.2   \n",
       "3                                    1        100                 75.7   \n",
       "4                                    1        100                 77.1   \n",
       "\n",
       "   Weather Normalized Site Electricity Intensity (kWh/ft²)  \\\n",
       "0                                                7.5         \n",
       "1                                                8.7         \n",
       "2                                                3.5         \n",
       "3                                                4.0         \n",
       "4                                                2.6         \n",
       "\n",
       "   Weather Normalized Site Natural Gas Intensity (therms/ft²)  \\\n",
       "0                                                0.0            \n",
       "1                                                0.9            \n",
       "2                                                0.0            \n",
       "3                                                0.0            \n",
       "4                                                0.0            \n",
       "\n",
       "   Water Intensity (All Water Sources) (gal/ft²)  ...  \\\n",
       "0                                          51.01  ...   \n",
       "1                                            NaN  ...   \n",
       "2                                          18.40  ...   \n",
       "3                                            NaN  ...   \n",
       "4                                            NaN  ...   \n",
       "\n",
       "   Largest Property Use Type_Retail Store  \\\n",
       "0                                       0   \n",
       "1                                       0   \n",
       "2                                       0   \n",
       "3                                       0   \n",
       "4                                       0   \n",
       "\n",
       "   Largest Property Use Type_Self-Storage Facility  \\\n",
       "0                                                0   \n",
       "1                                                0   \n",
       "2                                                0   \n",
       "3                                                0   \n",
       "4                                                0   \n",
       "\n",
       "   Largest Property Use Type_Senior Care Community  \\\n",
       "0                                                0   \n",
       "1                                                0   \n",
       "2                                                0   \n",
       "3                                                0   \n",
       "4                                                0   \n",
       "\n",
       "   Largest Property Use Type_Social/Meeting Hall  \\\n",
       "0                                              0   \n",
       "1                                              0   \n",
       "2                                              0   \n",
       "3                                              0   \n",
       "4                                              0   \n",
       "\n",
       "   Largest Property Use Type_Strip Mall  \\\n",
       "0                                     0   \n",
       "1                                     0   \n",
       "2                                     0   \n",
       "3                                     0   \n",
       "4                                     0   \n",
       "\n",
       "   Largest Property Use Type_Supermarket/Grocery Store  \\\n",
       "0                                                  0     \n",
       "1                                                  0     \n",
       "2                                                  0     \n",
       "3                                                  0     \n",
       "4                                                  0     \n",
       "\n",
       "   Largest Property Use Type_Urgent Care/Clinic/Other Outpatient  \\\n",
       "0                                                  0               \n",
       "1                                                  0               \n",
       "2                                                  0               \n",
       "3                                                  0               \n",
       "4                                                  0               \n",
       "\n",
       "   Largest Property Use Type_Wholesale Club/Supercenter  \\\n",
       "0                                                  0      \n",
       "1                                                  0      \n",
       "2                                                  0      \n",
       "3                                                  0      \n",
       "4                                                  0      \n",
       "\n",
       "   Largest Property Use Type_Worship Facility  score  \n",
       "0                                           0   93.0  \n",
       "1                                           0    NaN  \n",
       "2                                           0   72.0  \n",
       "3                                           0   67.0  \n",
       "4                                           0   80.0  \n",
       "\n",
       "[5 rows x 65 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "features=pd.read_csv('data/processedData.csv')\n",
    "\n",
    "# Display top of dataframe\n",
    "features.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "376e39ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1858, 65)\n",
      "(9461, 65)\n"
     ]
    }
   ],
   "source": [
    "# Extract the buildings with no score and the buildings with a score\n",
    "no_score = features[features['score'].isna()]\n",
    "score = features[features['score'].notnull()]\n",
    "\n",
    "print(no_score.shape)\n",
    "print(score.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "655e34c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(6622, 64)\n",
      "(2839, 64)\n",
      "(6622, 1)\n",
      "(2839, 1)\n"
     ]
    }
   ],
   "source": [
    "# Splitting data into training and testing\n",
    "from sklearn.model_selection import train_test_split\n",
    "# Separate out the features and targets\n",
    "features = score.drop(columns='score')\n",
    "targets = pd.DataFrame(score['score'])\n",
    "\n",
    "# Replace the inf and -inf with nan (required for later imputation)\n",
    "features = features.replace({np.inf: np.nan, -np.inf: np.nan})\n",
    "\n",
    "# Split into 70% training and 30% testing set\n",
    "X, X_test, y, y_test = train_test_split(features, targets, test_size = 0.3, random_state = 42)\n",
    "\n",
    "print(X.shape)\n",
    "print(X_test.shape)\n",
    "print(y.shape)\n",
    "print(y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6e9ec369",
   "metadata": {},
   "outputs": [],
   "source": [
    "X.to_csv('data/training_features.csv', index = False)\n",
    "X_test.to_csv('data/testing_features.csv', index = False)\n",
    "y.to_csv('data/training_labels.csv', index = False)\n",
    "y_test.to_csv('data/testing_labels.csv', index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ff9d7fb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
