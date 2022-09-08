```
BRANCH_NAME=ked-120
KED_VERSION=0.18.2 

git checkout -b $BRANCH_NAME

conda create -n sf_temp_$BRANCH_NAME python=3.8.13
conda activate sf_temp_$BRANCH_NAME
pip install kedro==$KED_VERSION

rm -r spaceflights_temp **/*.pyc

kedro new --starter=spaceflights --config=config.yaml && mv spaceflights_temp/* .

rm -r spaceflights_temp #delete original folder after move

git add . && git commit -m "base spaceflight starter $BRANCH_NAME"
```