
set PORT=9090

start chrome "http://localhost:%PORT%"

REM start powershell -noexit -Command "java -jar jenkins.war --httpPort=%PORT%"
java -jar jenkins.war --httpPort=%PORT%
