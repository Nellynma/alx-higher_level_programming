#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me  response "You got me!" in the repsonse body
curl -s -X PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
