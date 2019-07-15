#/bin/bash
mkdir -p /app/log
touch /app/log/http.log
cd /app
ruby ./app/app.rb -s puma -e production