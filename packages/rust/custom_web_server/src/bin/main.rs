use custom_web_server::ThreadPool;
use std::fs;
use std::io::prelude::{Read, Write};
use std::net::{TcpListener, TcpStream};

// define mut stream for TcpStreams
fn handle_connection(mut stream: TcpStream) {
    // buffer instance stroed stack as size 512byte
    let mut buffer = [0; 512];
    // fill data to buffer from stream
    stream.read(&mut buffer).unwrap();

    let get = b"GET / HTTP/1.1\r\n";
    let (status_line, filename) = if buffer.starts_with(get) {
        ("HTTP/1.1 200 OK\r\n\r\n", "index.html")
    } else {
        ("HTTP/1.1 404 NOT FOUND\r\n\r\n", "404.html")
    };

    let contents = fs::read_to_string(filename).unwrap();

    let response = format!("{}{}", status_line, contents);
    // send byte to connection
    stream.write(response.as_bytes()).unwrap();
    // wait to write
    stream.flush().unwrap();
}

fn main() {
    // wait to TCP Connection
    // return Result<_, E> if use other port
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    // Limit num of threads
    let pool = ThreadPool::new(4);
    // one stream means connection between client and server
    // connection means entire req and res
    for stream in listener.incoming() {
        let stream = stream.unwrap();
        pool.execute(|| {
            handle_connection(stream);
        });
    }
}
