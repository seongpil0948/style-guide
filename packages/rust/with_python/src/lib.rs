extern crate cpython;
use cpython::{PyResult, Python, py_module_initializer, py_fn};

// py_module_initializer macro provides a public interface that Python can read.
// The __doc__ part is not mandatory, 
// but when it is present, you can see it with help(with_python).
py_module_initializer!(with_python, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py, "get_result", py_fn!(py, get_result(val: &str)))?;
    Ok(())
});

fn get_result(_py: Python, val: &str) -> PyResult<String> {
    Ok("Rust says: ".to_owned() + val)
}
