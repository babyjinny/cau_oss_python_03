#박스 부피를 계산하여 우체국 택배 보내기

#사용자에게 입력받기
Width = float(input("width : "))
Length = float(input("length : "))
Height = float(input("height : "))

#총 길이 계산
total_length = Width + Length + Height

#80cm 이하 5000원
#80cm 초과 100cm 이하 8000원
#100cm 초과 120cm 이하 10000원
#120cm 초과 160cm 이하 13000원
#160cm 초과 배송불가

if total_length <= 80 :
	money = 5000
elif total_length <= 100 :
	money = 8000
elif total_length <= 120 :
	money = 10000 
elif total_length <= 160 :
	money = 13000
else :
	money = "unavailable"

print("Total Length : ",total_length,"money : ",money)
