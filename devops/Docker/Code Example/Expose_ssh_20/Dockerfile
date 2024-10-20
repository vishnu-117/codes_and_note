FROM ubuntu:16.04
ENV NAME vtu
ENV PASS 123
RUN mkdir -p /var/run/sshd
RUN apt-get update
RUN apt-get install -y openssh-server
RUN useradd -d /home/vtu -g root -G sudo -m -p $(echo $PASS | openssl passwd -1 -stdin) $NAME
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]



# ssh vtu@192.168.1.13 -p 32768
# username@leptopip -p mapped port(which can be seen by docker container ls)