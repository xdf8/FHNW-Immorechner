import numpy as np
import sklearn

def durbin_watson(res, y):
    """
    Calculates the Durbin Watson statistic. Its sorted by Price to see if there is autocorrelation
    """
    sort_index = np.argsort(y,axis=0)
    res_ = res.copy()
    res_ = res_.iloc[sort_index]
    res_sum_ = res_ - np.roll(res_, 1)
    res_sum_top = np.sum(res_sum_[1:]**2)
    res_sum_bot = np.sum(res**2)
    return res_sum_top / res_sum_bot

def mean_absolute_percentage_error(y_true, y_pred):
    """
    Calculates the mean absolute percentage error of two arrays
    """
    n = len(y_true)
    return np.sum(np.abs((y_true - y_pred)) / y_true) / n 

def negative_mean_absolute_percentage_error(y_true, y_pred):
    """
    Calculates the negative mean absolute percentage error of two arrays
    """
    return - mean_absolute_percentage_error(y_true, y_pred)

def xgb_n_mape(y_true, y_pred):
    """
    Mape for XGBoost.
    """
    y_pred = y_pred.get_label()
    return 'N-Mape:', negative_mean_absolute_percentage_error(y_true, y_pred)


def r2_mape(y_true, y_pred):
    print("R2-Score: {}. MAPE: {}".format(sklearn.metrics.r2_score(y_true, y_pred), mean_absolute_percentage_error(y_true, y_pred)))

    
