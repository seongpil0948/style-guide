# build stage creates a Rust environment (we give it a name, rust-build)
FROM rust:latest as rust-build

RUN mkdir build
COPY with_python/src ./build/src
COPY with_python/Cargo.toml ./build/Cargo.toml

WORKDIR /build

#  makes sure the target is installed
RUN rustup target add x86_64-unknown-linux-gnu
# builds the binary. before also run cargo test if we had any unit-tests.
RUN cargo build --release --target x86_64-unknown-linux-gnu

FROM python:3.7-slim

RUN mkdir app

COPY web/main.py /app/main.py
COPY web/requirements.txt /app/requirements.txt
# for linux
COPY --from=rust-build /build/target/x86_64-unknown-linux-gnu/release/with_python.so /app/with_python.so

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "-p", "0.0.0.0:8000"]