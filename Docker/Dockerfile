FROM debian:latest

COPY /app /app
COPY start.sh /start.sh
RUN apt update
RUN apt install -y ruby libxml2-dev ruby-dev openssl libmagick++-dev libxslt-dev make
RUN gem install sinatra
RUN gem install sinatra-contrib
RUN gem install jwt
RUN gem install puma
RUN gem install rubysl-securerandom

CMD ["/bin/bash","/start.sh"]
