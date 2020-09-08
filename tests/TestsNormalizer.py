import sys
sys.path.append('../')
from Normalizer.Normalizer import Normalizer
import unittest
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class TestNormalizer(unittest.TestCase):
    normalizer = Normalizer()
    test_data = [ 61.19499969,  57.31000137,  56.09249878,  61.72000122,
                61.38000107,  64.61000061,  61.93500137,  63.70249939,
                63.57249832,  60.22750092,  61.23249817,  60.35250092,
                65.61750031,  64.85749817,  66.51750183,  66.99749756,
                68.3125    ,  71.76249695,  71.10749817,  71.67250061,
                70.69999695,  69.23249817,  67.09249878,  69.02500153,
                68.75749969,  70.74250031,  70.79250336,  69.64499664,
                71.93250275,  73.44999695,  72.26750183,  73.29000092,
                74.38999939,  75.15750122,  75.93499756,  77.53250122,
                78.75250244,  77.85250092,  76.91249847,  77.38500214,
                76.92749786,  78.73999786,  78.28500366,  79.80750275,
                79.21250153,  79.72250366,  79.18250275,  79.52749634,
                79.5625    ,  79.48500061,  80.46250153,  80.83499908,
                81.27999878,  80.58000183,  82.875     ,  83.36499786,
                85.99749756,  88.20999908,  83.97499847,  84.69999695,
                85.74749756,  88.01999664,  87.89749908,  87.93250275,
                87.43000031,  89.71749878,  91.63249969,  90.01499939,
                91.20999908,  88.40750122,  90.44499969,  91.19999695,
                91.02749634,  91.02749634,  93.46250153,  93.17250061,
                95.34249878,  95.75250244,  95.91999817,  95.47750092,
                97.05750275,  97.72499847,  96.52249908,  96.32749939,
                98.35749817,  97.        ,  97.27249908,  92.84500122,
                92.61499786,  94.80999756,  93.25250244,  95.04000092,
                96.19000244, 106.26000214, 108.9375    , 109.66500092,
                110.0625    , 113.90249634, 111.11250305, 112.72750092]
    # test_data = np.array([round(t, 2) for t in test_data])
    test_data = np.array(test_data)
    test_data = np.reshape(test_data, (-1,1))

    def test_transform_featurescaler(self):
        result = self.normalizer.FeatureScaler.transform(self.test_data)
        scaler = MinMaxScaler()
        scaler.fit(self.test_data)
        correct = scaler.transform(self.test_data)
        self.assertTrue(np.allclose(result, correct))
    
    def test_reverse_transform_featurescaler(self):
        result = self.normalizer.FeatureScaler.transform(self.test_data)
        result = self.normalizer.FeatureScaler.reverse_transform(result)
        self.assertTrue(np.allclose(result, self.test_data))
    
    def test_raise_transform(self):
        test_data = self.test_data.tolist()
        with self.assertRaises(ValueError):
            self.normalizer.FeatureScaler.transform(test_data)
            self.normalizer.MeanScaler.transform(test_data)
            self.normalizer.ZScoreScaler.transform(test_data)
            self.normalizer.UnitLengthScaler.transform(test_data)
    