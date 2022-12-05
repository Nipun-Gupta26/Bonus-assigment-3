import numpy as np
import pandas as pd
from flask import jsonify, Flask, request

@app.route("/priceIndex", methods=["POST"])
def restbyPriceandRating() : 
    if request.method == "POST" : 
        data = request.get_json()
        R = data['R']
        P = data['P']
        
        df = pd.read_csv('review_tags.csv')
    
        concat_string = R + " Rating " + "and " + P + " Price"
        df_filter = df[(df['cluster_description'] == concat_string)]
        df_filter = df_filter.sort_values(by=['tags_count'], ascending=False)
        
        dict_string = []
        
        
        for i in range(len(df_filter)) : 
            restaurant = df_filter.iloc[i].to_dict()
            dict_string.append(restaurant)
                    
        return jsonify(dict_string)

@app.route("/colName", methods=["GET"])
def colName() : 
    if request.method == "GET" : 
        df = pd.read_csv('review_tags.csv')
        colName = df.columns.tolist()
        return jsonify(colName[51:59])