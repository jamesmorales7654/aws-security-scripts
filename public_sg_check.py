# Detects AWS security groups that allow public access (0.0.0.0/0)
# Useful for identifying overly permissive network rules that expose
# cloud resources to the public internet.

import boto3
import boto3

ec2 = boto3.client('ec2')

groups = ec2.describe_security_groups()

for g in groups['SecurityGroups']:
    for perm in g['IpPermissions']:
        for ip in perm.get('IpRanges', []):
            if ip['CidrIp'] == '0.0.0.0/0':
                print(f"Public SG detected: {g['GroupId']}")
