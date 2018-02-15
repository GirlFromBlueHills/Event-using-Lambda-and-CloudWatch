import shutil
import os
import boto3
#your code path which you want to upload
script_dir = os.path.dirname(__file__)
file_path =script_dir + '/path to file.py'
#create a zip of the path
newzip = shutil.make_archive(file_path, 'zip', script_dir)
print(newzip)
#connet to aws
session = boto3.Session(aws_access_key_id='AKIAIPHUUKDE346PRfcsdfsdSFA', aws_secret_access_key="134eKEz6psOJATc76dgHa2312fvvcQL5jxq/Jaj6O0quiOpFO",
                             region_name="us-east-1")

iam_client = session.client('iam')
lambda_client = session.client('lambda')
events_client = session.client('events')
#read the zip file
env_variables = dict() # Environment Variables
print(env_variables)
with open(newzip, 'rb') as f:
  zipped_code = f.read()

#ctreate a new function
fn_name = "newFunctionName"
fn_role = 'arn:aws:iam::30122333229531683:role/lambda_basic_execution'

fn_response = lambda_client.create_function(
  FunctionName=fn_name,
  Runtime='python3.6',
  Role=fn_role,
  Handler='RDSScripts.handler',
  Code=dict(ZipFile=zipped_code),
  Timeout=300, # Maximum allowable timeout
  Environment=dict(Variables=env_variables),
)

fn_arn = fn_response['FunctionArn']
#rate is the time when the code will run eg: rate(1 min) or cron(* * * *)
frequency = "rate(1 hour)"
name = "{0}-Trigger".format(fn_name)

rule_response = events_client.put_rule(
  Name=name,
  ScheduleExpression=frequency,
  State='ENABLED',
)
#add permissions
lambda_client.add_permission(
  FunctionName=fn_name,
  StatementId="{0}-Event".format(name),
  Action='lambda:InvokeFunction',
  Principal='events.amazonaws.com',
  SourceArn=rule_response['RuleArn'],
)

events_client.put_targets(
  Rule=name,
  Targets=[
    {
      'Id': "1",
      'Arn': fn_arn,
    },
  ]
)