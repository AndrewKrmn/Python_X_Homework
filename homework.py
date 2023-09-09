import boto3
s3 = boto3.client('s3',aws_access_key_id = 'AKIAQGL7X2SFHGKZZBNZ',aws_secret_access_key = '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')
#aws_access_key_id = 'AKIA3JWEQ5JLWZEW6HB3'
file = open("tes1t.html", "mode")
content = file.read()
print(content)


#aws_secret_access_key = 'rwqmlACx+F1u4tI6C1L7RYTKaYhUtrwJS5rSQDWj'
name_bucket = 'chupapipepa'
name_folder = 'kakish'
name_file = 'test.html'
region='eu-north-1'
local_file_path = '/home/telephon/Стільниця/'

pepa = s3.create_bucket(Bucket=name_bucket)
kakashka = s3.put_object(Bucket=name_bucket, Key=name_folder)
chacha = s3.upload_file(name_file,name_bucket,name_folder/name_file)
akaka = s3.download_file(name_bucket,name_file, local_file_path)
delete = s3.delete_object(Bucket=name_bucket, Key=name_file)
kaka = s3.list_buckets()
print(pepa)
print("=========================================")
print(kakashka)
print('==========================================')
print(chacha)
print("==========================================")
print(akaka)
print("========================================")
print(delete)
print("======================================")
print(kaka)
