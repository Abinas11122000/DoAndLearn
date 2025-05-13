import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def get_user_input():
    print("Enter your AWS credentials:")
    access_key = input("AWS Access Key ID: ").strip()
    secret_key = input("AWS Secret Access Key: ").strip()
    session_token = input("Session Token (press Enter if not using temporary credentials): ").strip()
    bucket_name = input("Enter the S3 bucket name: ").strip()
    return access_key, secret_key, session_token, bucket_name

def list_s3_objects(access_key, secret_key, session_token, bucket_name):
    try:
        if session_token:
            session = boto3.session.Session(
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                aws_session_token=session_token
            )
        else:
            session = boto3.session.Session(
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key
            )

        s3_client = session.client('s3')

        print(f"\nListing objects in bucket: {bucket_name}\n")
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"{obj['Key']} (Size: {obj['Size']} bytes)")
        else:
            print("Bucket is empty or does not exist.")

    except NoCredentialsError:
        print("Invalid AWS credentials.")
    except ClientError as e:
        print(f"AWS Client Error: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    access_key, secret_key, session_token, bucket_name = get_user_input()
    list_s3_objects(access_key, secret_key, session_token, bucket_name)
