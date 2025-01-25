FROM centos:latest

RUN sed -i 's|mirrorlist=|#mirrorlist=|g' /etc/yum.repos.d/CentOS-*.repo && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*.repo && \
    yum clean all && \
    yum update -y 

RUN yum install -y python39 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip 

RUN pip3 install flask && pip3 install mysql-connector-python


#RUN yum update && pip install flask
WORKDIR /app
EXPOSE 5000
COPY . /app

CMD ["python3","app.py"]
