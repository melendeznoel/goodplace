from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    RemovalPolicy,
    CfnOutput
)
from constructs import Construct

class DevopsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # define an s3 bucket
        apples_bucket = s3.Bucket(self,
                                  "apples",
                                  website_index_document="index.html",
                                  website_error_document="index.html",
                                  public_read_access=True,
                                  block_public_access=s3.BlockPublicAccess.BLOCK_ACLS,
                                  removal_policy=RemovalPolicy.DESTROY)

        CfnOutput(self, "BucketURL", value=apples_bucket.bucket_website_url)

        # example resource
        # queue = sqs.Queue(
        #     self, "DevopsQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
