# wth

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```


## Building + running this lovely thing

Install Docker.  Then, grab the `postgis/postgis-latest` Docker image.

Run the Docker.

`docker run --name mypostgis -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgis/postgis\n`

TODO remind myself how I got the HUCs in there!!

 9462  shp2pgsql ak_huc8s
 9463  shp2pgsql ak_huc8s > akhuc8s.sql
 9478  shp2pgsql -s 4326 ak_huc8s > akhuc8s.sql
 9510  shp2pgsql -s 4326 /tmp/merged_snap_polys > akpolys.sql
 9540  shp2pgsql -s 4326 /tmp/merged_snap_polys > akpolys.sql
 9549  shp2pgsql -s 4326 /tmp/merged_snap_polys > akpolys.sql
 9558  shp2pgsql -d -s 4326 /tmp/merged_snap_polys > akpolys.sql
 9584  shp2pgsql -d -s 3338 ./merged_snap_polys > akpolys.sql
 9587  shp2pgsql -d -s 3338 ./merged_snap_polys > akpolys.sql
 9590  shp2pgsql -d -s 3338 ./merged_snap_polys > akpolys.sql
 9591  shp2pgsql -d -s 3338 /tmp/merged_snap_polys > akpolys.sql
 9594  shp2pgsql -d -s 3338 /tmp/merged_snap_polys > akpolys.sql
 9618  shp2pgsql -d -s 3338 /tmp/merged_snap_polys.shp > /tmp/akpoints.sql
 9619  shp2pgsql -d -s 3338 /tmp/snap_points.shp > /tmp/points.sql
 9620  shp2pgsql -d -s 3338 /tmp/snap_points.shp > /tmp/snap_points.sql
 9623  shp2pgsql -d -s 3338 /tmp/snap_points.shp > /tmp/snap_points.sql
 9633  shp2pgsql -d -s 3338 /tmp/snap_points.shp > /tmp/snap_points.sql
 9638  shp2pgsql -d -s 3338 /tmp/merged_snap_polys > /tmp/akpolys.sql\n
 9639  shp2pgsql -d -s 3338 /tmp/snap_points.shp > /tmp/snap_points.sql\n


 9467  psql -h localhost -U postgres
 9468  psql -h localhost -U postgres -p mysecretpassword < akhuc8s.sql
 9469  psql -h localhost -U postgres -P mysecretpassword < akhuc8s.sql
 9470  man psql
 9472  psql -h localhost -U postgres < akhuc8s.sql
 9473  psql -h localhost -U postgres
 9482  psql -h localhost -U postgres < akhuc8s.sql
 9484  psql -h localhost -U postgres < akhuc8s.sql
 9517  history psql
 9518  history | grep psql
 9521  psql -h localhost -U postgres < akpolys.sql
 9522  psql -h localhost -U postgres
 9526  vi .psql_history
 9529  vi .psql_history
 9530  cat .psql_history
 9532  cd .psql
 9541  history | grep psql
 9542  man psql
 9543  psql -h localhost -U postgres --quiet < akpolys.sql
 9546  psql -h localhost -U postgres --quiet < akpolys.sql
 9547  psql -h localhost -U postgres < akpolys.sql
 9550  psql -h localhost -U postgres < akpolys.sql
 9556  psql -h localhost -U postgres < /tmp/akpolys.sql
 9559  psql -h localhost -U postgres < /tmp/akpolys.sql
 9560  psql --quiet -h localhost -U postgres < /tmp/akpolys.sql
 9561  psql -h localhost -U postgres
 9585  psql --quiet -h localhost -U postgres < akpolys.sql
 9588  psql --quiet -h localhost -U postgres < akpolys.sql
 9592  psql --quiet -h localhost -U postgres < akpolys.sql
 9595  psql --quiet -h localhost -U postgres < akpolys.sql
 9621  psql --quiet -h localhost -U postgres < /tmp/snap_points.sql
 9624  psql --quiet -h localhost -U postgres < /tmp/snap_points.sql
 9634  psql --quiet -h localhost -U postgres < /tmp/snap_points.sql
 9637  history | grep psql
 9640  psql --quiet -h localhost -U postgres < /tmp/akpolys.sql\n
 9641  psql --quiet -h localhost -U postgres < /tmp/snap_points.sql\n
 9642  psql --quiet -h localhost -U postgres -c "SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(t.*)::json) ) FROM (select id, name, alt_name, poly_type, ST_Transform( geom, 4326 ) as geom from merged_snap_polys m where ST_DWithin(m.geom, 'SRID=3338;POINT(303784.486450 1666276.643171)', 40000)) as t;" > t.json\n
 9651  psql --quiet -h localhost -U postgres -c "SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(t.*)::json) ) FROM (select id, name, alt_name, ST_Transform( geom, 4326 ) as geom from merged_snap_polys m where ST_DWithin(m.geom, 'SRID=3338;POINT(303784.486450 1666276.643171)', 40000)) as t;" > p.json
 9653  psql --quiet -h localhost -U postgres -c "SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(t.*)::json) ) FROM (select id, name, alt_name, ST_Transform( geom, 4326 ) as geom from snap_points m where ST_DWithin(m.geom, 'SRID=3338;POINT(303784.486450 1666276.643171)', 40000)) as t;" > p.json



 9642  psql --quiet -h localhost -U postgres -c "SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(t.*)::json) ) FROM (select id, name, alt_name, poly_type, ST_Transform( geom, 4326 ) as geom from merged_snap_polys m where ST_DWithin(m.geom, 'SRID=3338;POINT(303784.486450 1666276.643171)', 40000)) as t;" > t.json\n
 9651  psql --quiet -h localhost -U postgres -c "SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(t.*)::json) ) FROM (select id, name, alt_name, ST_Transform( geom, 4326 ) as geom from merged_snap_polys m where ST_DWithin(m.geom, 'SRID=3338;POINT(303784.486450 1666276.643171)', 40000)) as t;" > p.json
10040  history | merged_sn




9476  ogrinfo ak_huc12s.shp
 9478  shp2pgsql -s 4326 ak_huc8s > akhuc8s.sql
 9479  head akhuc8s.sql
 9482  psql -h localhost -U postgres < akhuc8s.sql
 9484  psql -h localhost -U postgres < akhuc8s.sql
 9570  cd alaska_hucs
 9572  ogrinfo -so ak_huc12s.shp
 9573  ogrinfo ak_huc12s.shp
 9574  ogrinfo -so ak_huc12s ak_huc12s.shp
 9575  ogrinfo -so ak_huc12s.shp
 9576  ogrinfo -so ak_huc12s.shp ak_huc12s
 9577  ogrinfo -so ak_huc8s.shp ak_huc8s
 9603  rm ../vector_data/polygon/boundaries/alaska_hucs/akhuc8s.sql



psql --quiet -h localhost -U postgres -c "SELECT json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(t.*)::json) ) FROM (select id, name, alt_name, ST_Transform( geom, 4326 ) as geom from snap_points m where ST_DWithin(m.geom, 'SRID=3338;POINT(303784.486450 1666276.643171)', 40000)) as t;" > p.json










### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```
