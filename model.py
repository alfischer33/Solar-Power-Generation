import pandas as pd
from database import query_to_df

def predict(ambient, module, irradiation):
    def merged_tables():
        g = query_to_df('SELECT * FROM generation')
        w = query_to_df('SELECT * FROM weather')

        g.loc[:,'date_time'] = pd.to_datetime(g.loc[:,'date_time'])
        w.loc[:,'date_time'] = pd.to_datetime(w.loc[:,'date_time'])

        df = g.merge(w, on=['plant_id', 'date_time'], how='inner')
        
        return df

    def get_Xy(df):
        df = df.drop(columns = ['date_time', 'ac_power', 'plant_id', 'source_key_x', 'daily_yield', 'total_yield', 'source_key_y'])
        X = df.drop(columns='dc_power')
        y = df.dc_power
        return X, y
    
    def sklearn_linear_model():
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        X,y = get_Xy(merged_tables())
        return model.fit(X,y)

    return sklearn_linear_model().predict([[ambient, module, irradiation]])
    