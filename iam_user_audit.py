# Lists IAM users in an AWS account.
# Can be used as a starting point for IAM auditing.

import boto3

iam = boto3.client('iam')

response = iam.list_users()

for user in response['Users']:
    print(user['UserName'])
