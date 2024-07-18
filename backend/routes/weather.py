# -*- coding: utf-8 -*-
from flask import jsonify
from datetime import datetime
from .. import app, etl


@app.get("/api/v2/weather/<location>/<forecast_type>")
@app.get("/api/v2/weather/<location>")
def weather(location: str, forecast_type: str = "weather"):

    clear_data = etl.extract(location, forecast_type)
    prepared_data = etl.transform(clear_data, forecast_type)
    return prepared_data
