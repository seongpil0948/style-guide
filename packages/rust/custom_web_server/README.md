* __TCP(전송제어)__
    - A low-level Protocol that how transmitted infomation from one server is  <br>
        to other server
    - but, it does not defined what the infomation is
* __HTTP__
    - Based UDP/__TCP__


# HTTP
* Struct
    1. Method, Request_URI, Http-version = MRH
    2. headers CRLF
    3. Message-Body
* Terms
    - URI(Uniform(통합) Resource Identifier)
    - URL(Uniform Resource Locator)
    - CRLF(Carriage Return and line feed)
        - \r\n that combine \r(Carriage Return) and \n (line feed)
        - 결론은 줄바꿈 ㅋㅋㅋㅋㅋ
    - Reason-Phrase (응답구문)
        - 상태코드를 설명

* __GET__ Request
    ```
        // MRH
        GET(Method) /(Request_URI) HTTP/1.1(Http-version)

        // headers
        Host: localhost:7878
        Connection: keep-alive
        Cache-Control: max-age=0
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Sec-Fetch-Site: none
        Sec-Fetch-Mode: navigate
        Sec-Fetch-User: ?1
        Sec-Fetch-Dest: document
        Accept-Encoding: gzip,    
    ```
    - Response 
        - Struct
            1. Http-version, Status-Code, Reason-Phrase CRLF
            2. headers CRLF
            3. Message-Body
        - HTTP/1.1 200 OK \r\n\r\n

# Concurrency
    * __Trhread Pool__ (DONE)
        - 작업을 처리하기 위해 미리 생성해서 대기중인 스레드 그룹.
        - while each thread performing a tash,  other thread also do other task
        - 서비스 거부 공격(Denial of Service) 을 위하여 <br>
            Limit num of threads

    * Fork/Join (TODO)
    * Single-threaded async I/O (TODO)