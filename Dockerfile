FROM rappdw/docker-java-python:openjdk1.8.0_171-python3.6.6

# install requirements
RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get install dos2unix
RUN apt-get install -y cmake
RUN mkdir /app
WORKDIR /app

# Bundle app source
COPY . /app
COPY requirements.txt .
COPY run.sh .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m pip install xgboost --no-cache-dir

RUN chmod a+x run.sh
RUN dos2unix run.sh
RUN dos2unix /app/code/bulkparselang.sh
RUN python /app/code/CreateDataset.py
RUN python /app/code/CreateMetaDataFile.py
RUN python /app/code/ErrorStats.py;
RUN /app/code/bulkparselang.sh /app/udp/czech-ud-2.0-170801.udpipe /app/Datasets/CZ/ /app/Datasets/CZ-Parsed/
RUN /app/code/bulkparselang.sh /app/udp/italian-ud-2.0-170801.udpipe /app/Datasets/IT/ /app/Datasets/IT-Parsed/
RUN /app/code/bulkparselang.sh /app/udp/german-ud-2.0-170801.udpipe /app/Datasets/DE/ /app/Datasets/DE-Parsed/
CMD ["sh","./run.sh"]
