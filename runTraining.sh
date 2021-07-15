cd data
unzip -n wirlernenonline2-dedup.txt.zip
cd ..
docker run -v `pwd`/data:/data -v `pwd`/src:/src wlo-dedup-py /usr/bin/python3 /src/createHashes.py 