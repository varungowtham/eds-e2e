#!/usr/sh

max=10

for number in `seq 1 $max10`
do
  ./create-app-structure -d TestApplication$number
  cp /tmp/eds-e2e/qe_1/TestApplication$number/test_application$number.py \
    apps/TestApplication$number/src/testapplication$number/
  cp /tmp/eds-e2e/qe_1/TestApplication$number/__main__.py \
    apps/TestApplication$number/src/testapplication$number/

  sh -c ./apps/test-application$number
  sleep 10
done

