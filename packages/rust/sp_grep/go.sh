export SP_ENV_VARIABLE="SP"
cargo test 
if [ $? -eq 0 ] 
then
    echo "Test is Ok"
    cargo run good text.txt > output.txt 
else
    echo "Test is Fail"
fi