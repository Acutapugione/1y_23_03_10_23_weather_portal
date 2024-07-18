# -*- coding: utf-8 -*-
from flask import jsonify
from .. import app, etl


@app.get("/api/v1/weather/<location>/<forecast_type>")
@app.get("/api/v1/weather/<location>")
def weather_old(location: str, forecast_type: str = "weather"):
    """
    DEPRECATED
    """
    clear_data = etl.extract(location, forecast_type)
    prepared_data = etl.transform(clear_data, forecast_type)
    # mimetype_params = {"charset": "utf-8"}
    # response = jsonify(prepared_data)
    # response.mimetype_params.update(mimetype_params)
    return prepared_data
