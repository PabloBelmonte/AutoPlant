
set PORT=8081

start chrome "http://localhost:%PORT%"

REM start powershell -noexit -Command "java -jar jenkins.war --httpPort=%PORT%"
java -jar jenkins.war --httpPort=%PORT%
