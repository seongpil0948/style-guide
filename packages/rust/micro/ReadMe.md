# What isn’t covered

## For simplicity, some boring but easier-to-implement things are omitted from this article, notably:

- Testing: Rust features a built-in unit testing facility. Just try it — it’s amazing.
  Configuration: this is trivial to implement, but at the same time, very environment-specific.
- Logging: it is pretty straightforward.
- SSL: although we touched on this with regards to the building stage, usually you also have to deal with certificates and openssl initialisation code. However, exploring this topic may require another full-sized article.
- Other things that are specific to our environment.

# In conclusion

### All in all, we consider our experiment successful. Yes, you definitely can build microservices with Rust. Some aspects turned out to be easier than expected, some required more tinkering.

### However, in a limited period of time, we built a service that is ready to be shipped, doesn’t need any web or application server, and features advanced functionality like asynchronous execution — that is very encouraging.

### A microservice made with Rust has a few distinctive advantages:

- It enjoys great performance compared to traditional alternatives.
- It is free from most of the memory-related bugs which plague lower-level languages.
- It takes advantage of a powerful type system of Rust: many bugs can be caught at compile time.
- It requires no additional runtime (the runtime is compiled into a binary that is easily shipped.)
  This binary doesn’t run a garbage collector. This makes it easier to control the resources utilized by the service.

### We must mention the downsides as well:

- Rust has a steeper learning curve than Python or Java.
- It is also a relatively new language, so the ecosystem isn’t so established.
- The community, as welcoming as it is, is also significantly smaller.

---

Rust is an extremely useful tool in building reliable and performant architectures. Even though it’s still a relatively new technology, the results are promising. It’s definitely worth it to have it in your toolbox.
