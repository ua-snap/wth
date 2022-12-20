from flask import Flask, Response, request
import json
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("host=localhost user=postgres password=mysecretpassword")


@app.route("/")
def fetch_polys():
    lat = request.args.get("lat")
    lng = request.args.get("lng")
    radiusKm = request.args.get("r")
    print(lat, lng, radiusKm)
    cur = conn.cursor()
    sql = "SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(t.*)::json) ) FROM (select id, name, alt_name, ST_Transform( geom, 4326 ) as geom from merged_snap_polys m where ST_DWithin(m.geom, 'SRID=3338;POINT(303784.486450 1666276.643171)', 40000)) as t;"
    cur.execute(sql)
    res = cur.fetchone()  # because GeoJSON, just the one line is needed.
    cur.close()
    geoJson = json.dumps(res)  # Convert to stringy-thing.
    return Response(response=geoJson, status=200, mimetype="application/json")
