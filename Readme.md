git checkout -b <branch_name>

pip install kedro==<kedro_version>

rm -r spaceflights_temp **/*.pyc

kedro new --starter=spaceflights --config=config.yaml && mv spaceflights_temp/* temp 

rm -r spaceflights_temp

git add . && git commit -m "spaceflight starter"