FROM ubuntu

COPY app .

RUN apt update
# RUN apt -y upgrade
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN python3.6 -m pip install pip --upgrade

RUN pip install -r "requirements.txt"

#ENTRYPOINT python "/${repo}/${api_launcher}"
ENTRYPOINT python3 lambda_function.py