# For the build stage, use the official Rust image
FROM rust:latest as rust-build

# Add the source code (+fix file permissions) 
ADD --chown=rust:rust src src
ADD --chown=rust:rust Cargo.toml Cargo.toml

# Build
RUN cargo build --release

FROM scratch

# Copy the binary to a minimal Linux OS
COPY --from=rust-build /home/rust/src/target/x86_64-unknown-linux-musl/release/micro .

CMD ["./micro"]