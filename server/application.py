from flask import Flask, Response, request
import json
import psycopg2
from pyproj import Transformer

app = Flask(__name__)

conn = psycopg2.connect("host=localhost user=postgres password=mysecretpassword")

transformer = Transformer.from_crs(4326, 3338)

@app.route("/")
def fetch_polys():
    lat = float(request.args.get("lat"))
    lng = float(request.args.get("lng"))
    radiusKm = float(request.args.get("r"))
    coords = transformer.transform(lat, lng)
    params = (coords[0], coords[1], radiusKm)
    print(params)

    cur = conn.cursor()
    sql = f"SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(t.*)::json) ) FROM (select areasqkm, hucid, name, huclevel, ST_Transform( geom, 4326 ) as geom from hucs m where ST_DWithin(m.geom, 'SRID=3338;POINT(%s %s)', %s)) as t;"
    cur.execute(sql, params)
    res = cur.fetchone()  # because GeoJSON, just the one line is needed.
    cur.close()
    geoJson = json.dumps(res)  # Convert to stringy-thing.
    return Response(response=geoJson, status=200, mimetype="application/json")
