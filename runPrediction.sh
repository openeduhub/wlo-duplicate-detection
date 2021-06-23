
docker run -v `pwd`/src:/src -v `pwd`/data:/data wlo-dedup-py python3 /src/predict.py  "$1"