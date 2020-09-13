FROM yaafe/yaafe as yaafe-feature-extractor

COPY ./src /opt/musical-instrument-recognition/src
WORKDIR /opt/musical-instrument-recognition
COPY ./setup.py /opt/musical-instrument-recognition/

RUN pip -qq install --upgrade pip
RUN pip install .

COPY ./model /opt/musical-instrument-recognition/model
COPY ./yaafe /opt/miniconda/bin/yaafe

EXPOSE 8000

RUN cd /opt/musical-instrument-recognition/src/third-party-lib/libsvm/ && make
RUN cd /opt/musical-instrument-recognition/src/third-party-lib/libsvm/python && make
RUN python /opt/musical-instrument-recognition/src/manage.py migrate && mv /opt/musical-instrument-recognition/src/db.sqlite3 /opt/musical-instrument-recognition/

ENV SQLITE_DB_PATH="/opt/musical-instrument-recognition/db.sqlite3"
ENV MIR_MODEL_PATH="/opt/musical-instrument-recognition/model/four_instruments.model"
ENV MIR_UPLOAD_DIR="/opt/musical-instrument-recognition/uploads/"
ENV PYTHONPATH="/opt/musical-instrument-recognition/src/third-party-lib/libsvm/python/:${PYTHONPATH}"

ENTRYPOINT ["gunicorn", "mir.wsgi", "-b", "0.0.0.0:8000"]