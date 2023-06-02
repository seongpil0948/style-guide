use actix_web::{get, web, App, HttpResponse, HttpServer, Responder};

#[get("/")]
async fn index() -> impl Responder {
    HttpResponse::Ok().body("Rust service prototype")
}

#[get("/healthcheck")]
async fn healthcheck() -> impl Responder {
    HttpResponse::Ok().body("I'm alive!")
}

pub fn init(config: &mut web::ServiceConfig) {
    config.service(web::scope("").service(index).service(healthcheck));
}

#[get("/vuln/{vulnerability_id}")]
pub async fn get_vulnerability(
    pool: web::Data<DbPool>,
    vuln_id: web::Path<i32>,
) -> Result<HttpResponse, Error> {
    let vuln_id = vuln_id.into_inner();
    let conn = pool.get().expect("couldn't get db connection");

    // Use web::block to offload blocking Diesel code without blocking server thread.
    // Omitting find_vulnerability_by_id() function that queries the database here, it's trivial.
    let vulnerability = web::block(move || find_vulnerability_by_id(vuln_id, &conn))
        .await
        .map_err(|e| {
            eprintln!("{}", e);
            HttpResponse::InternalServerError().finish()
        })?;

    if let Some(vulnerability) = vulnerability {
        Ok(HttpResponse::Ok().json(vulnerability))
    } else {
        let res = HttpResponse::NotFound().body(format!("No vuln found with id: {}", vuln_id));
        Ok(res)
    }
}

pub async fn receive_messages(cfg: ServiceConfig) {
    let consumer = create_consumer(...);
    let mut msg_stream = consumer.start();

    // iterate over all messages blocking
    while let Some(msg) = msg_stream.next().await {
        match msg {
            Ok(msg) => {
                // Process the message here...
            }
            Err(e) => error!("Could not receive and will not process message: {}", e),
        };
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let pool = connect_db();
    // Spawning the Kafka processor to run in parallel with the API 
    actix_web::rt::spawn(async move { receive_messages(config).await });
    HttpServer::new(move || App::new().data(pool.clone()).configure(init))
        .bind("0.0.0.0:8000")?
        .run()
        .await
}
