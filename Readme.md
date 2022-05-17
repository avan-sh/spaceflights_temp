git checkout -b <branch_name>

pip install kedro==<kedro_version>

kedro new --starter=spaceflights --config=config.yaml && mv -r spaceflights_temp/* . && git commit -m "spaceflight starter"