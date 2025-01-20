# AWS 서비스 사용하기 위한 방법
# AWS와 연결
# https://docs.aws.amazon.com/rekognition/latest/dg/images-bytes.html

#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def detect_labels_local_file(photo):

    client=boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    result = ''        
    # print(response['Labels'])

    # 강아지일 확률을 출력
    # 강아지일 확률 : 99.5%

    isPerson = False
    for label in response['Labels']:

        result += '{} : {}%</br>'.format(label['Name'], label['Confidence'])

    return result

def main():
    photo='../../Downloads/dog.jpg'

    label_count=detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()

