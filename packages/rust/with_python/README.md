# Rust With Python

## For Output
1. cargo build --release
2. $ `cp target/release/libwith_python.dylib ./with_python.so  `
    * The resulting binary is in target/release/libwith_python.dylib (it would be .so on Linux or .dll on Windows)
3. `python`
4. `import with_python as w`
5. `w.get_result("With Python")` >> 'Rust says: With Python'

--- 
## 여기부터 안되는 중
https://codeburst.io/how-to-use-rust-to-extend-python-360174ee5819
First of all, we’ll need our own PyPI repository to share our packages, without polluting the global index. You can setup devpi or any analogue, but for our little example 

* setup.py 를 통해 현재 [플랫폼(macosx_11_0_x86_64)].whl 파일을 만들어 바이너리 파일로 출력
    - A .whl file is essentially a zip archive with all the files plus metadata plus file name convention. The installer then uses the file name to find a wheel suitable for the current platform.

* We’re going to use a manylinux Docker image, and run the following script inside the container:
``` 
#!/bin/bash
set -ex
curl https://sh.rustup.rs -sSf | sh -s -- -y
export PATH="$HOME/.cargo/bin:$PATH"
cd /io
for PYBIN in /opt/python/{cp35-cp35m,cp36-cp36m,cp37-cp37m}/bin; do
    export PYTHON_SYS_EXECUTABLE="$PYBIN/python"
    "${PYBIN}/pip" install -U setuptools wheel setuptools-rust
    "${PYBIN}/python" setup.py bdist_wheel
done
for whl in dist/*.whl; do
    auditwheel repair "$whl" -w dist/
done
```

So, the following commands
```
docker pull quay.io/pypa/manylinux1_x86_64
docker run --rm -v `pwd`:/io quay.io/pypa/manylinux1_x86_64 /io/build-wheels.sh
```

* …will create wheels we could install on Linux.

` ls package/dist `

```
pip install twine

twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ package/dist/*
```

https://test.pypi.org/project/with_python-rust/. And see the wheels

* Finally, we can remove the Rust building stage from the Dockerfile. <br> We just need to add mylib-rust in requirements.txt and set an additional index URL for PIP:

```
FROM python:3.7-slim

RUN mkdir app

COPY web/main.py /app/main.py
COPY web/requirements.pypi.txt /app/requirements.txt

WORKDIR /app

RUN pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple -r requirements.txt

```
* If you run this build, you’ll see it doesn’t attempt to compile Rust source code but downloads a corresponding wheel instead:
    - 이 빌드를 실행하면 Rust 소스 코드 컴파일을 시도하지 않고 대신 해당 휠을 다운로드하는 것을 볼 수 있습니다.
    -  ``` docker build -f Dockerfile.pypi -t rust-python-web-pypi . ```