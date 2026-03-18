print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.")
print("변환하고 싶은 섭씨온도를 입력하세요.")

celsius = float(input())
fahrenheit = celsius * 1.8 + 32

print()
print(f"섭씨온도: {celsius:g}")
print(f"화씨온도: {fahrenheit:.2f}")
