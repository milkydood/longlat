FROM python:alpine3.19

RUN mkdir /app
WORKDIR /app

COPY longlat.py run.sh requirements.txt ./

# override python3 entrypoint, so we can setup venv/pull in requirements
ENTRYPOINT /bin/ash

RUN python3 -m venv env && \
    source env/bin/activate && \
    python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt

CMD chown -R nobody.nogroup /app

ENV ACCESS_KEY undef
USER nobody
ENTRYPOINT ["./run.sh"]

