FROM ubuntu

RUN apt-get update
RUN apt-get install -y python

COPY stp.py /opt/stp.py
CMD ["python","/opt/stp.py"]
