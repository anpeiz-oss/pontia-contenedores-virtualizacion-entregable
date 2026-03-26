from api.routers import tasks_router
from database.session import engine
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models.task import Base


import logging

# --- Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

# --- fastAPI app initialization ---
app = FastAPI(title="Task Management API", version="1.0.0")

@app.get("/")
def root():
    logger.info("Acceso a la raíz de la Task Management API.")
    return {"message": "This is the Task Management API root. Use /docs for more information."}

app.include_router(tasks_router.router, prefix="/tasks", tags=["tasks"])

@app.exception_handler(404)
def not_found_handler(request: Request, exc: HTTPException):
    logger.warning(f"Ruta no encontrada: {request.method} {request.url}")
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>404 - Not Found</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

            * { margin: 0; padding: 0; box-sizing: border-box; }

            body {
                background: #000;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                overflow: hidden;
                perspective: 400px;
            }

            .stars {
                position: fixed;
                top: 0; left: 0;
                width: 100%; height: 100%;
                background: radial-gradient(2px 2px at 20px 30px, #fff, transparent),
                            radial-gradient(2px 2px at 40px 70px, #fff, transparent),
                            radial-gradient(1px 1px at 90px 40px, #fff, transparent),
                            radial-gradient(2px 2px at 160px 120px, #fff, transparent),
                            radial-gradient(1px 1px at 200px 60px, #fff, transparent),
                            radial-gradient(2px 2px at 300px 200px, #fff, transparent),
                            radial-gradient(1px 1px at 400px 100px, #fff, transparent),
                            radial-gradient(2px 2px at 500px 300px, #fff, transparent),
                            radial-gradient(1px 1px at 600px 180px, #fff, transparent),
                            radial-gradient(2px 2px at 700px 250px, #fff, transparent);
                background-repeat: repeat;
                background-size: 800px 400px;
                animation: twinkle 4s ease-in-out infinite alternate;
                z-index: 0;
            }

            @keyframes twinkle {
                0% { opacity: 0.5; }
                100% { opacity: 1; }
            }

            .error-code {
                font-family: 'Press Start 2P', monospace;
                font-size: 6rem;
                color: #FFE81F;
                text-shadow: 0 0 20px rgba(255, 232, 31, 0.5),
                             0 0 40px rgba(255, 232, 31, 0.3);
                z-index: 1;
                margin-bottom: 2rem;
                animation: pulse 2s ease-in-out infinite;
            }

            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.7; }
            }

            .crawl-container {
                z-index: 1;
                transform: rotateX(25deg);
                animation: float 3s ease-in-out infinite;
            }

            @keyframes float {
                0%, 100% { transform: rotateX(25deg) translateY(0); }
                50% { transform: rotateX(25deg) translateY(-15px); }
            }

            .message {
                font-family: 'Press Start 2P', monospace;
                font-size: 1.6rem;
                color: #FFE81F;
                text-align: center;
                line-height: 2.2;
                text-shadow: 0 0 10px rgba(255, 232, 31, 0.4);
            }

            .home-btn {
                margin-top: 3rem;
                z-index: 1;
                font-family: 'Press Start 2P', monospace;
                font-size: 0.9rem;
                color: #FFE81F;
                background: transparent;
                border: 2px solid #FFE81F;
                padding: 1rem 2rem;
                cursor: pointer;
                text-decoration: none;
                transition: all 0.3s ease;
            }

            .home-btn:hover {
                background: #FFE81F;
                color: #000;
                box-shadow: 0 0 20px rgba(255, 232, 31, 0.6);
            }
        </style>
    </head>
    <body>
        <div class="stars"></div>
        <div class="error-code">404</div>
        <div class="crawl-container">
            <p class="message">This is not the page<br>you were looking for.</p>
        </div>
        <a href="/docs" class="home-btn">Return to safety</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=404)



