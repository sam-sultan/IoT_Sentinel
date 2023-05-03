
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn.ensemble import RandomForestClassifier

import argparse
import os


parser = argparse.ArgumentParser(
                    prog='IoT Sentinel',
                    description='This Program replicates the ML part of the paper')


parser.add_argument('-i', '--input-dir', help="Input directory", required=True)      # option that takes a value
#parser.add_argument('-v', '--verbose',
#                    action='store_true')  # on/off flag



# Parse the samples
args = parser.parse_args()


"""
DataSet Class
"""
class DataSet:

    def __init__(self, n=12):
        
        self.n = n
        self.n_features = 23

        self.X = np.empty((0, n, self.n_features))
        self.Y = np.empty((0, 1))


    def getDataSet(self, directory):

        # Loop through the list of devices
        for folder in os.listdir(directory):
            
            folder_path = os.path.join( directory, folder )

            # Folder name is the label
            label = folder

            # Get the Samples of each device
            # (sample x packet x features)
            dataset = [self.readFile( os.path.join(folder_path, f), n=self.n ) for f in os.listdir(folder_path) ]
            dataset = np.array(dataset)

            # X
            self.X = np.vstack((self.X, dataset))

            # Y
            self.Y = np.vstack( (self.Y, np.array([label for l in range(dataset.shape[0]) ]).reshape((-1, 1)) ) )


        return self.X, self.Y

    # path: is the path to the sample
    # n: is the number of packets to be extracted
    def readFile(self, path, n=12):

        headers_name=['ARP','LLC','EAPOL','Pck_size','Pck_rawdata','IP_padding',
                        'IP_ralert','IP_add_count','Portcl_src','Portcl_dst','ICMP','ICMP6','TCP','UDP',
                        'HTTPS','HTTP','DHCP','BOOTP','SSDP','DNS','MDNS','NTP', 'IP'] # 'Label'

        # Read the csv file into a dataframe
        df = pd.read_csv(path) # delimiter="\t", names=headers_name

        # Remove the label column
        df = df[headers_name]

        # Convert the dataframe into a matrix of 12x23 
        # and add padding of zeros if the length of the dataframe is less than 12
        F_prime = df.to_numpy()[:n, :]

        # Pad the rows if there are number of packets less than 12
        F = np.pad(F_prime, [(0, n - F_prime.shape[0]), (0, 0)], 'constant', constant_values=0)

        return F

    def getTotalDevices(self):
        return np.unique(self.Y).size

    def __str__(self):
        return "\nFingerprints: {} | Devices: {}\n".format(self.X.shape[0], self.getTotalDevices() ) \
                + "X: {} | Y: {}\n".format(self.X.shape, self.Y.shape)




"""
Classifier
"""
class IoTSentinelClassifier(ClassifierMixin, BaseEstimator):
    def __init__(self):
        pass

    def fit(self, X, y, **kwargs):

        if y is None:
            raise ValueError('requires y to be passed, but the target y is None')

        X, y = check_X_y(X, y)

        # TODO code below
        self.n_features_in_ = X.shape[1]
        self.classes_ = unique_labels(y)
        self.is_fitted_ = True

        self.X_ = X
        self.y_ = y

        return self

    def predict(self, X):
        check_is_fitted(self, ['is_fitted_', 'X_', 'y_'])
        X = check_array(X)

        # TODO predictions below
        closest = np.argmin(euclidean_distances(X, self.X_), axis=1)

        return self.y_[closest]





# Import Dataset generated by the iot_fingerprint.py
dataset = DataSet()
X, Y = dataset.getDataSet(args.input_dir)


print dataset


cls = RandomForestClassifier()
cls = cls.fit(X[:10, :], Y[:10, :])
