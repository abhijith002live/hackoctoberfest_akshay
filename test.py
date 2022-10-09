import os
c="aws s3 ls s3://dronelandinghuman | awk '{print $4}'"
m=os.popen(c).read().split("\n")
m.pop()
s1=" aws rekognition detect-faces \ --image '{"S3Object":{"Bucket":"dronelandinghuman","Name": \n "
s2="}}' \ --attributes "ALL" | tail | grep Confidence | awk '{print $2}'"

for i in m:
    command="aws rekognition detect-faces  --image '{\"S3Object\":{\"Bucket\":\"dronelandinghuman\",\"Name\": \""+i+"\" }}'  --attributes \"ALL\" | tail | grep Confidence | awk '{print $2}'"
    print(command)
    result=os.popen(command).read()
    if result > 93.5:
        count=count+1
if count>8:
    return 1
else:
    return 0

import os
c="aws s3 ls s3://dronelandinghuman | awk '{print $4}'"
m=os.popen(c).read().split("\n")
m.pop()
print(m)