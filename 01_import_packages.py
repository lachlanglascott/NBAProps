import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  

from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

from scipy import stats
import seaborn as sns

