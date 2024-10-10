from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    CfnOutput,
    aws_s3_deployment
)
from constructs import Construct

class DevopsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        s3_bucket_name = 'goodplace.cloud'

        # define an s3 bucket
        apples_bucket = s3.Bucket(self,
                                  s3_bucket_name,
                                  bucket_name=s3_bucket_name,
                                  website_index_document="index.html",
                                  website_error_document="index.html",
                                  public_read_access=True,
                                  block_public_access=s3.BlockPublicAccess(block_public_acls=False, block_public_policy=False, ignore_public_acls=False, restrict_public_buckets=False),
                                  removal_policy=RemovalPolicy.DESTROY)

        aws_s3_deployment.BucketDeployment(self, "Deploymment",
                                           sources=[aws_s3_deployment.Source.asset('./build')],
                                           destination_bucket=apples_bucket)

        # log the public url for the bucket
        CfnOutput(self, "BucketURL", value=apples_bucket.bucket_website_url)