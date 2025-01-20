# If you want to delete output file
# s3 client
client = boto3.client('s3')

# created s3 object
s3_objects_key = []
s3_object_key_csv = query_execution_id + '.csv'
s3_objects_key.append({'Key': s3_object_key_csv})
s3_object_key_metadata = query_execution_id + '.csv.metadata'
s3_objects_key.append({'Key': s3_object_key_metadata})

# delete s3 object
for i in range(1, 1 + RETRY_COUNT):
    response = client.delete_objects(
        Bucket=S3_BUCKET,
        Delete={
            'Objects': s3_objects_key
            }
            )

if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print("delete %s complete" % s3_objects_key)
    break
else:
    print(response['ResponseMetadata']['HTTPStatusCode'])
    time.sleep(i)

else:
raise Exception('object %s delete failed' % s3_objects_key)