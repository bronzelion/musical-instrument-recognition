FROM yaafe/yaafe as yaafe-feature-extractor

RUN pip install django==1.7

COPY ./src /opt/musical-instrument-recognition/
COPY ./model /opt/musical-instrument-recognition/model

COPY ./yaafe /opt/miniconda/bin/yaafe

EXPOSE 8000

RUN cd /opt/musical-instrument-recognition/third-party-lib/libsvm/ && make

RUN cd /opt/musical-instrument-recognition/third-party-lib/libsvm/python && make

WORKDIR /opt/musical-instrument-recognition/

RUN  python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]