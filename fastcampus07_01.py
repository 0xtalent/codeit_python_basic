# fastcampus07-1
# process, thread, crawling, web, API

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

"""
프로세스는 쓰레드에 비해 생성비용(자원)이 많이 든다.
쓰레드는 프로세스 안에서 생성됩니다.
생성된 쓰레드들은 프로세스에 할당된 메모리(자원)을 공유하게 되는데
전역변수로 할당된 변수에 동시에 접근하게 되면 문제가 생길 수 있다.
동시접근을 막기위해 나온 개념: 세모포어, 락, 뮤텍스

파이썬의 GIL(Global Interpreter Lock) 특성
GIL이란 여러개의 쓰레드가 있을 때 쓰레드간의 동기화를 위해 사용되는 기술 중 하나
파이썬 전역에 Lock을 두고 Lock점유 해야만 코드를 실행할 수 있도록 제한
따라 실제 실행되는 쓰레드는 오직 하나

race condition
컴퓨터 공학의 중요성

CPU BOUND: 작업시간이 CPU의 영향을 많이 받는 작업(계산, 인코, 정렬 등/병렬성으로 성능향상 가능)
I/O BOUND: 작업시간이 I/O의 영향을 많이 받는 작업
(입출력, 파일 읽기쓰기, 네트워크 요청보내기/동시성으로 성능향상 가능)

병렬성(parallelism): 한번에 여러작업을 실행하는 것,
실제로 여러작업을 동시에 실행
파이썬에서 병렬성은 process를 사용해서 성능향상 가능

동시성(Concurrency): 한번에 여러 작업을 다루는 것,
동시에 실행하는 것처럼 보이지만 실제로는 시간을 쪼개서 실행
파이썬에서 동시성은 thread, async를 사용해서 성능향상 가능
"""

# 비동기(async)

"""
동기와 비동기를 구분하는 기준은 피호출자의 작업을 피호출자가 신경쓰면 동(작업 순서의 보장)
피호출자가 신경쓰지 않으면 비동기(작업 순서의 보장 X)
"""

# 크롤링(Crawling)

"""
크롤링(Crawling): 자동화 된 방식으로 웹(web)을 탐색
스크래핑(Scraping): 데이터를 수집하는 행위
"""

# web

"""
TCP/IP란?
웹에서 데이터를 주고 받을 때 어떻게 주고 받는지에 대한 규칙이 담겨있는 통신규약(프로토콜)
wappalyzer
"""

# API

"""
응용 프로그래밍에서 사용할 수 있도록,
운영체제나 프로그래밍 언어가 제공하는 기능을
제어할 수 있게 만든 인터페이스

상당수의 Open API들은 REST 디자인 패턴을 사용하고 있다.
REST: 로이 필딩이라는 분이 제시한 API 패턴
REST 핵심: URL은 정보를 표현, 정보에 대한 행위는 HTTP Method로 표현
URL과 Method를 통해 정보를 가져옴

graphql: 페이스북에서 만든 API 디자인 패턴
REST를 사용하면서 생긴 불편함(URL이 너무 많아지는 점),
사용자(기기)별로 필요한 정보가 조금씩 다르다,
over-fetching, under-fetching

하나 혹은 소수의 endpoint 사용, 요청 데이터에 따라 달라지는 결과 응답
"""
