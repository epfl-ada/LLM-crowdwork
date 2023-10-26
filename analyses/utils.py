import statsmodels.formula.api as smf
import numpy as np

def cc(df_v):
    return (df_v["y_cc"] == "synthetic").mean()

def pcc(df_v):
    return (df_v["cal_prob"]).sum() / len(df_v)

def ols_adj(df_v, df_test_set):
    # following `https://harris.uchicago.edu/files/misclassification.pdf`
    df_v["y_cc_num"] = (df_v["y_cc"] == "synthetic").astype("int")
    alpha_0 = ((df_test_set["y_cc"] == "synthetic") & (df_test_set["target"] == "real")).sum() \
              / (df_test_set["target"] == "real").sum()  # FPR
    alpha_1 = ((df_test_set["y_cc"] == "real") & (df_test_set["target"] == "synthetic")).sum() \
              / (df_test_set["target"] == "synthetic").sum()  # FNR
    res = smf.ols("y_cc_num ~ 1", data=df_v).fit()
    beta = res.params["Intercept"]
    return (beta - alpha_0) / (1 - alpha_0 - alpha_1)


def bootstrap(func, df_v, extra_df=None, n=10000, is_dict=False, seed=78923476):
    np.random.seed(seed)
    stat = []
    for i in range(n):
        if extra_df is None:
            stat.append(func(df_v.sample(frac=1, replace=True)))
        else:
            stat.append(func(df_v.sample(frac=1, replace=True), extra_df))

    if is_dict:
        df_stat = pd.DataFrame(stat)
        return {
            key_v: (np.mean(df_stat[key_v].values),
                    np.quantile(df_stat[key_v].values, 0.025),
                    np.quantile(df_stat[key_v].values, 0.975))
            for key_v in df_stat.columns
        }
    else:
        stat = np.array(stat)
        return np.mean(stat), np.quantile(stat, 0.025), np.quantile(stat, 0.975)


form = lambda x: "{:.1f}".format((round(100 * x, 1))) + "\%"
