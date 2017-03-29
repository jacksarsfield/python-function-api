import pandas as pd

def double (input):
    df = pd.read_json(input)
    df['29'] = df['29']*2
    return df.to_json(orient = 'records')
