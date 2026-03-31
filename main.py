# 파일이름 : main.py
# 작 성 자 : 다현

bucket_list={}
temp = ""

bucket_list.append(input("맛집 리스트 입력:"))

bucket_list.append(input("맛집 리스트 입력:"))

bucket_list.append(input("맛집 리스트 입력:"))
print(bucket_list, "\n")

temp= input("맛집 리스트 입력:")
bucket_list.insert(0, temp)
print(bucket_list, "\n")

temp = input("도장 깨기:")
bucket_list.remove(temp)
print(bucket_list)
