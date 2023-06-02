# Async, Parallel 

## TODO


* __Trhread Pool__ (DONE)
    - 다중 스레드 웹서버 프로젝트에서 다룬 알고리즘 라이브러리화
    - 작업을 처리하기 위해 미리 생성해서 대기중인 스레드 그룹.
    - while each thread performing a tash,  other thread also do other task
    - 서비스 거부 공격(Denial of Service) 을 위하여 <br>
        Limit num of threads

* Fork/Join (TODO)
    - Fork(분기) / Join(머지) 작업을 분할가능할 만큼 쪼개고 쪼개진 작업을 별도의 work thread를 통해 작업후 결과를 합치는 과정을 거쳐 결과를 만들어냅니다.
    - the fork–join model is a way of setting up and executing parallel programs, such that execution branches off(분기) in parallel at designated points(특정 지점) in the program, to "join" (merge) at a subsequent point and resume sequential  execution. Parallel sections may fork( 반복적으로 분기 될 수 있다 부분적으로) recursively until a certain task granularity(작업 세분화) is reached.

* Single-threaded async I/O (TODO)
* 변수 공유를 통한 통신(DSM : Distributed Shared Memory)


## For Parallel

### 병렬 프로그래밍이 왜 필요한가? 

CPU의 속도가 매우 빨라짐(1년에 0.5배, 반도체의 발전과 함께 발전했기 때문에 성장세는 더뎌짐)
파워가 너무 높아져서 성능 향상이 더뎌짐
주파수를 높여서 성능을 올리는 방법은 한계점에 도달
이는 프로세서 디자인에 큰 영향을 끼침
하나의 칩 안에 여러개의 CPU 코어를 넣는 CMP(Chip Multiple Processors) 방식으로 발전

* Data Parallelism
    - 동일한 데이터의 다른 하위 집합에서 동일한 작업을 수행한다.
    - 동기식 연산(Synchronous computation)을 수행한다.
    - 모든 데이터 세트에서 동작하는 실행 스레드가 하나뿐이기 때문에 속도 향상은 더욱 빠르다.
    - 병렬화의 양은 입력 크기에 비례한다.
    - 멀티프로세서 시스템의 최적 부하 균형을 위해 설계되었다.
* Task Paralism
    - 동일하거나 다른 데이터에 대해 다른 작업을 수행한다.
    - 비동기 연산(Asynchronous computation)을 수행한다.
    - 각 프로세서가 동일하거나 다른 데이터 집합에서 서로 다른 스레드 또는 프로세스를 실행하므로 속도 향상은 적다.
    - 병행화의 양은 독립적인 업무의 수에 비례한다.
    - 여기서 로드 밸런싱은 하드웨어의 가용성과 정적 및 동적 스케줄링과 같은 스케줄링 알고리즘에 따라 달라진다.

### Parallel system
---
* 공유 메모리 기반 (Rust)

    - 모든 프로세서가 메모리 공간을 공유하고 있다. 하나의 주소 공간을 가지고 모든 프로세서가 사용하고 있다. 즉, 특정한 메모리 공간을 모든 프로세서들이 같이 보고 있으며 공유되는 주소를 업데이트하는 것으로 통신을 할 수 있다.
    - 여러 개의 프로세서가 메모리를 공유함. 즉 메모리에 접근 속도가 다 같음.

* 분산 메모리 기반 (Python)

    - 모든 코어가 각각의 고유한 메모리를 가지고 있다. 공유 변수를 가지고 있지 않기 때문에 코어 A 에서 코어 B 로 통신을 하려면 다른 방법이 필요하다. send-receive communication이 일어나야 한다.
    - 메모리에 접근 속도가 각각 다름. 다른 프로세서의 메모리에 접근하려면 IPC(Inter-Process Communication)로 해야하기 때문


## Ref Thank for 
* https://sys09270883.github.io/parallel%20programming/72/
* https://ko.wikipedia.org/wiki/%EB%B3%91%EB%A0%AC_%EC%BB%B4%ED%93%A8%ED%8C%85