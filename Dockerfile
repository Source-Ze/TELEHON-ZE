FROM SOURCE-ZE/ZE:slim-buster

RUN git clone https://github.com/Source-Ze/TELEHON-ZE.git /root/ZE

WORKDIR /root/ZE

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/ZE/bin:$PATH"

CMD ["python3","-m","ZE"]
