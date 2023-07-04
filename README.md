# linux_system_by_python

# 시작하기 
```
# RabbitMQ docker run이 필요합니다. 
git clone https://github.com/kimhyunsong/linux_system_by_python.git
# filebrowser 설치
curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash
# python3-prctl 설치
sudo apt-get install -y python3-prctl
# 실행
python3 main.py
```

# 시스템 아키텍처
![image](https://github.com/kimhyunsong/linux_system_by_python/assets/87460502/21f66127-5ff2-4785-b730-438504ad2cf1)


# 실행 callstack
![image](https://github.com/kimhyunsong/linux_system_by_python/assets/87460502/1566580f-810d-45ea-9381-ca0b33d99503)




### 후기
```
1. 장점
   - 파이썬이라 가독성이 높고 시스템콜도 접근성이 뛰어나서 쉽게 구현할 수 있다.
2. 아쉬운 점
   - GIL
     - pypy를 사용하면 된다고는 하는데 생각보다 모듈 버전 차이가 크다. (예를들어 prctl)
   - MQ를 지원하지 않는다. (RabbitMQ로 대체)
   - 시스템 콜 가독성이 지나치게 높다(?).
     - 메모리나 초기화한 영역의 반환을 어디서 하는지 명확하게 알 수 없다.
```
