# # # from datetime import datetime
# # # from fastapi import BackgroundTasks, FastAPI, Depends, Form, Request
# # # from fastapi.templating import Jinja2Templates
# # # from fastapi.staticfiles import StaticFiles
# # # from sqlalchemy.orm import Session
# # # from typing import List
# # # from decimal import Decimal
# # # import models, crud, schemas
# # # from database import SessionLocal, engine

# # # from fastapi.responses import RedirectResponse

# # # from video_processor import process_video

# # # models.Base.metadata.create_all(bind=engine)

# # # app = FastAPI(
# # #     title="PPE Monitoring API",
# # #     description="Tracks people, PPE compliance, and violations with real-time analytics",
# # #     version="1.0.0"
# # # )

# # # app.mount("/static", StaticFiles(directory="static"), name="static")
# # # templates = Jinja2Templates(directory="templates")

# # # def safe_float(val):
# # #     return float(val) if isinstance(val, Decimal) else val

# # # # Dependency
# # # def get_db():
# # #     db = SessionLocal()
# # #     try:
# # #         yield db
# # #     finally:
# # #         db.close()

# # # # @app.get("/")
# # # # def read_dashboard(request: Request, db: Session = Depends(get_db)):
# # # #     counts = crud.get_latest_counts(db)
# # # #     summary = crud.get_ppe_summary(db)
# # # #     summary = {k: safe_float(v) for k, v in summary.items()}

# # # #     violations = crud.get_latest_violations()
# # # #     notifications = crud.get_all_notifications(db)

# # # #     violation_chart = {
# # # #         "labels": ["Mon", "Tue", "Wed"],
# # # #         "data": [5, 10, 3]
# # # #     }

# # # #     return templates.TemplateResponse("dashboard.html", {
# # # #         "request": request,
# # # #         "counts": counts,
# # # #         "summary": summary,
# # # #         "violations": violations,
# # # #         "notifications": notifications,
# # # #         "violation_chart": violation_chart
# # # #     })
# # # @app.get("/")
# # # def dashboard(request: Request, db: Session = Depends(get_db)):
# # #     counts = crud.get_latest_counts(db)
# # #     summary = crud.get_ppe_summary(db)
# # #     violations = crud.get_latest_violations()
# # #     notifications = crud.get_all_notifications(db)

# # #     alerts = crud.get_ppe_alerts(db)

# # #     return templates.TemplateResponse("dashboard.html", {
# # #         "request": request,
# # #         "counts": counts,
# # #         "summary": summary,
# # #         "violations": violations,
# # #         "notifications": notifications,
# # #         "violation_chart": {"labels": ["Mon", "Tue", "Wed"], "data": [5, 10, 3]},
# # #         "alerts": alerts,
# # #         "now": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# # #     })


# # # @app.post("/process")
# # # def run_processing(background_tasks: BackgroundTasks, source: str = Form(...)):
# # #     print("🎬 Starting video processing in background:", source)
# # #     background_tasks.add_task(process_video, source)
# # #     return RedirectResponse(url="/", status_code=303)

# # # @app.get("/api/ppe/totals")
# # # def get_ppe_totals(db: Session = Depends(get_db)):
# # #     return crud.get_ppe_totals(db)

# # # @app.post("/api/frame", response_model=schemas.FrameSummaryCreate)
# # # def create_frame(fs: schemas.FrameSummaryCreate, db: Session = Depends(get_db)):
# # #     return crud.create_frame_summary(db, fs)

# # # @app.get("/api/tracking/counts", response_model=schemas.CountResponse)
# # # def get_counts(db: Session = Depends(get_db)):
# # #     return crud.get_latest_counts(db)

# # # @app.get("/api/ppe/summary", response_model=schemas.PPESummaryResponse)
# # # def get_ppe_summary(db: Session = Depends(get_db)):
# # #     return crud.get_ppe_summary(db)

# # # @app.get("/api/violations/daily", response_model=schemas.ViolationDailyResponse)
# # # def get_violation_graph(db: Session = Depends(get_db)):
# # #     return crud.get_violation_daily(db)

# # # @app.get("/api/violations/latest", response_model=List[schemas.LatestViolation])
# # # def get_latest_violations():
# # #     return crud.get_latest_violations()

# # # @app.get("/api/latest-violation")
# # # def get_latest_violation(db: Session = Depends(get_db)):
# # #     latest = db.query(models.FrameNotification).order_by(models.FrameNotification.timestamp.desc()).first()
# # #     if not latest:
# # #         return {"message": None}
# # #     return {
# # #         "message": f"⚠️ Person {latest.person_id} is not wearing {latest.violation_type}"
# # #     }

# # # @app.post("/api/notification", response_model=schemas.FrameNotificationOut)
# # # def post_notification(n: schemas.FrameNotificationCreate, db: Session = Depends(get_db)):
# # #     return crud.create_frame_notification(db, n)

# # # @app.get("/api/notifications", response_model=List[schemas.FrameNotificationOut])
# # # def get_notifications(db: Session = Depends(get_db)):
# # #     return crud.get_all_notifications(db)



# # # @app.post("/api/person", response_model=schemas.PersonPPEStatusOut)
# # # def create_person_status(person: schemas.PersonPPEStatusCreate, db: Session = Depends(get_db)):
# # #     return crud.create_person_ppe_status(db, person)
# # # # ---------------- Run Server ----------------
# # # if __name__ == "__main__":
# # #     import uvicorn
# # #     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# # from datetime import datetime
# # from fastapi import BackgroundTasks, FastAPI, Depends, Form, Request
# # from fastapi.templating import Jinja2Templates
# # from fastapi.staticfiles import StaticFiles
# # from fastapi.responses import RedirectResponse
# # from sqlalchemy.orm import Session
# # from typing import List
# # from decimal import Decimal

# # import models, crud, schemas
# # from database import SessionLocal, engine
# # from video_processor import process_video

# # # DB Initialization
# # models.Base.metadata.create_all(bind=engine)

# # # App Configuration
# # app = FastAPI(
# #     title="PPE Monitoring API",
# #     description="Tracks people, PPE compliance, and violations with real-time analytics",
# #     version="1.0.0"
# # )
# # app.mount("/static", StaticFiles(directory="static"), name="static")
# # templates = Jinja2Templates(directory="templates")

# # # Utility
# # def safe_float(val):
# #     return float(val) if isinstance(val, Decimal) else val

# # # Dependency
# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# # # --------------------- ROUTES ---------------------

# # @app.get("/")
# # def dashboard(request: Request, db: Session = Depends(get_db)):
# #     counts = crud.get_latest_counts(db)
# #     summary = crud.get_ppe_summary(db)
# #     violations = crud.get_latest_violations()
# #     notifications = crud.get_all_notifications(db)
# #     alerts = crud.get_latest_ppe_alerts(db)

# #     return templates.TemplateResponse("dashboard.html", {
# #         "request": request,
# #         "counts": counts,
# #         "summary": summary,
# #         "violations": violations,
# #         "notifications": notifications,
# #         "alerts": alerts,
# #         "violation_chart": {"labels": ["Mon", "Tue", "Wed"], "data": [5, 10, 3]},
# #         "now": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #     })

# # @app.post("/process")
# # def run_processing(background_tasks: BackgroundTasks, source: str = Form(...)):
# #     print("🎬 Starting video processing in background:", source)
# #     background_tasks.add_task(process_video, source)
# #     return RedirectResponse(url="/", status_code=303)

# # @app.post("/api/frame", response_model=schemas.FrameSummaryCreate)
# # def create_frame(fs: schemas.FrameSummaryCreate, db: Session = Depends(get_db)):
# #     return crud.create_frame_summary(db, fs)

# # @app.get("/api/ppe/totals")
# # def get_ppe_totals(db: Session = Depends(get_db)):
# #     return crud.get_ppe_totals(db)

# # @app.get("/api/tracking/counts", response_model=schemas.CountResponse)
# # def get_counts(db: Session = Depends(get_db)):
# #     return crud.get_latest_counts(db)

# # @app.get("/api/ppe/summary", response_model=schemas.PPESummaryResponse)
# # def get_ppe_summary(db: Session = Depends(get_db)):
# #     return crud.get_ppe_summary(db)

# # @app.get("/api/violations/daily", response_model=schemas.ViolationDailyResponse)
# # def get_violation_graph(db: Session = Depends(get_db)):
# #     return crud.get_violation_daily(db)

# # @app.get("/api/violations/latest", response_model=List[schemas.LatestViolation])
# # def get_latest_violations():
# #     return crud.get_latest_violations()

# # @app.get("/api/latest-violation")
# # def get_latest_violation(db: Session = Depends(get_db)):
# #     latest = crud.get_latest_notification(db)
# #     if not latest:
# #         return {"message": None}
# #     return {
# #         "message": f"⚠️ Person {latest.person_id} is not wearing {latest.violation_type}"
# #     }
# # @app.post("/api/alerts")
# # async def post_alert_summary(data: dict, db: Session = Depends(get_db)):
# #     print("Received data:", data)

# #     # Process the alert summary and save to the database
# #     alert = models.PPEAlertSummary(
# #         hardhat_count=data["hardhat_count"],
# #         hardhat_drop=data["hardhat_drop"],
# #         vest_count=data["vest_count"],
# #         vest_drop=data["vest_drop"],
# #         mask_count=data["mask_count"],
# #         mask_drop=data["mask_drop"],
# #         gloves_count=data["gloves_count"],
# #         gloves_drop=data["gloves_drop"]
# #     )
# #     db.add(alert)
# #     db.commit()
# #     db.refresh(alert)
# #     print("Alert saved to DB:", alert)

# #     return {"message": "Alert summary processed successfully."}


# # @app.post("/api/notification", response_model=schemas.FrameNotificationOut)
# # def post_notification(n: schemas.FrameNotificationCreate, db: Session = Depends(get_db)):
# #     return crud.create_frame_notification(db, n)

# # @app.get("/api/notifications", response_model=List[schemas.FrameNotificationOut])
# # def get_notifications(db: Session = Depends(get_db)):
# #     return crud.get_all_notifications(db)

# # @app.post("/api/person", response_model=schemas.PersonPPEStatusOut)
# # def create_person_status(person: schemas.PersonPPEStatusCreate, db: Session = Depends(get_db)):
# #     return crud.create_person_ppe_status(db, person)

# # # ---------------- Run Server ----------------
# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# ____________________________________________________
# from datetime import datetime
# import time
# from fastapi import BackgroundTasks, FastAPI, Depends, Form, HTTPException, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import RedirectResponse
# from sqlalchemy.orm import Session
# from typing import List
# from decimal import Decimal
# from fastapi.responses import RedirectResponse
# from starlette.status import HTTP_303_SEE_OTHER
# from fastapi import Form
# from ultralytics import YOLO
# import models, crud, schemas
# from database import SessionLocal, engine
# from video_processor import  process_video
# from fastapi import BackgroundTasks, FastAPI, Depends
# from fastapi.responses import StreamingResponse
# import cv2
# import numpy as np
# from io import BytesIO
# import threading
# from video_processor import process_video
# models.Base.metadata.create_all(bind=engine)
# from fastapi import Form
# app = FastAPI(title="PPE Monitoring API")
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.on_event("startup")
# def startup_camera_threads():
#     start_all_camera_streams()

# @app.get("/")
# def dashboard(request: Request, db: Session = Depends(get_db)):
#     user_id = 1  # Replace with session/user logic
#     if not crud.get_user_cameras(db, user_id):
#         return RedirectResponse("/add-camera", status_code=303)

#     counts = crud.get_latest_counts(db)
#     summary = crud.get_ppe_summary(db)
#     violations = crud.get_latest_violations()
#     notifications = crud.get_all_notifications(db)
#     alerts = crud.get_latest_ppe_alerts(db)

#     return templates.TemplateResponse("dashboard.html", {
#         "request": request,
#         "counts": counts,
#         "summary": summary,
#         "violations": violations,
#         "notifications": notifications,
#         "alerts": alerts,
#         "violation_chart": {"labels": ["Mon", "Tue", "Wed"], "data": [5, 10, 3]},
#         "now": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     })



# @app.get("/signup")
# def signup_form(request: Request):
#     return templates.TemplateResponse("signup.html", {"request": request})

# @app.post("/signup")
# def signup(name: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
#     crud.create_user(db, schemas.UserCreate(name=name, email=email, password=password))
#     return RedirectResponse("/login", status_code=303)

# @app.get("/login")
# def login_form(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})

# @app.post("/login")
# def login(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
#     user = crud.get_user_by_email(db, email)
#     if user and user.password == password:  # No hash for now
#         response = RedirectResponse("/", status_code=303)
#         # Store user info in session if using auth/session manager
#         return response
#     return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})


# @app.get("/add-camera")
# def show_camera_form(request: Request, db: Session = Depends(get_db)):
#     user_id = 1  # Replace with session or cookie-based logic
#     cameras = crud.get_user_cameras(db, user_id)
#     return templates.TemplateResponse("camera.html", {
#         "request": request,
#         "user_id": user_id,
#         "cameras": cameras
#     })


# # Background processing for video
# def start_video_processing_in_background(cam_id: int, user_id: int, source: str):
#     threading.Thread(target=process_video, args=(cam_id, user_id, source), daemon=True).start()

# @app.post("/start-video")
# def start_video_processing(cam_id: int, user_id: int, source: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(start_video_processing_in_background, cam_id, user_id, source)
#     return {"message": "Video processing started in the background!"}

# # Start processing in a thread
# @app.post("/start-processing")
# def start_video_processing(cam_id: int = Form(...), user_id: int = Form(...), source: str = Form(...)):
#     threading.Thread(target=process_video_periodically, args=(cam_id, user_id, source), daemon=True).start()
#     return {"message": "Video processing started in the background!"}

# @app.post("/add-camera")
# def submit_camera_form(
#     user_id: int = Form(...),
#     name: str = Form(...),
#     source: str = Form(...),
#     db: Session = Depends(get_db)
# ):
#     camera = schemas.CameraCreate(user_id=user_id, name=name, source=source)
#     crud.create_camera(db, camera)

#     # ✅ Automatically start video processing for this camera
#     from threading import Thread
#     Thread(target=process_video, args=(source,), daemon=True).start()

#     return {"message": "Camera added successfully"}

# @app.post("/users/")
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return crud.create_user(db, user)

# def periodic_task(background_tasks: BackgroundTasks, user_id: int, cam_id: int, source: str):
#     # This function will execute the task every second
#     while True:
#         background_tasks.add_task(process_video, cam_id, user_id, source)
#         time.sleep(1)  # Sleep for 1 second



# # Function that processes video continuously in the background
# def process_video_periodically(cam_id, user_id, source):
#     while True:
#         process_video(cam_id, user_id, source)  # Call the existing process_video function
#         time.sleep(1)  # Process the video every second

# # Endpoint to trigger video processing in a background thread
# @app.post("/start-processing")
# def start_video_processing(cam_id: int = Form(...), user_id: int = Form(...), source: str = Form(...)):
#     # Start video processing in a separate thread
#     threading.Thread(target=process_video_periodically, args=(cam_id, user_id, source), daemon=True).start()
#     return {"message": "Video processing started in the background!"}

# @app.post("/process")
# def run_processing(background_tasks: BackgroundTasks, user_id: int = Form(...), cam_id: int = Form(...), source: str = Form(...)):
#     # Start the periodic task in the background when the /process endpoint is called
#     background_tasks.add_task(periodic_task, background_tasks, user_id, cam_id, source)
#     return {"message": "Processing started in the background!"}


# @app.post("/cameras/")
# def create_camera(
#     user_id: int = Form(...),
#     name: str = Form(...),
#     source: str = Form(...),
#     db: Session = Depends(get_db)
# ):
#     camera = schemas.CameraCreate(user_id=user_id, name=name, source=source)
#     crud.create_camera(db, camera)
#     return RedirectResponse(url="/add-camera", status_code=HTTP_303_SEE_OTHER)

# @app.get("/users/{user_id}/cameras/", response_model=List[schemas.CameraOut])
# def get_user_cameras(user_id: int, db: Session = Depends(get_db)):
#     return crud.get_user_cameras(db, user_id)

# @app.post("/api/frame", response_model=schemas.FrameSummaryCreate)
# def create_frame(fs: schemas.FrameSummaryCreate, db: Session = Depends(get_db)):
#     return crud.create_frame_summary(db, fs)

# @app.get("/api/tracking/counts", response_model=schemas.CountResponse)
# def get_counts(db: Session = Depends(get_db)):
#     return crud.get_latest_counts(db)

# @app.get("/api/ppe/summary", response_model=schemas.PPESummaryResponse)
# def get_ppe_summary(db: Session = Depends(get_db)):
#     return crud.get_ppe_summary(db)

# @app.get("/api/ppe/totals")
# def get_ppe_totals(db: Session = Depends(get_db)):
#     return crud.get_ppe_totals(db)

# # @app.post("/api/alerts")
# # async def post_alert_summary(data: dict, db: Session = Depends(get_db)):
# #     data["user_id"] = data.get("user_id", 1)
# #     data["camera_id"] = data.get("camera_id", 1)
# #     return crud.save_ppe_alert_summary(db, data)
# @app.post("/api/alerts")
# def save_alert(payload: schemas.AlertCreate, db: Session = Depends(get_db)):
#     return crud.save_ppe_alert_summary(db, payload.dict())

# @app.get("/api/alerts/latest")
# def get_latest_alerts(db: Session = Depends(get_db)):
#     # Fetch the latest PPE alert data
#     alerts = crud.get_latest_ppe_alerts(db)

#     # Check that data is returned from the database
#     if alerts:
#         return {"alerts": alerts}
#     else:
#         return {"alerts": {"hardhat_count": 0, "vest_count": 0, "mask_count": 0, "gloves_count": 0, 
#                             "hardhat_drop": 0, "vest_drop": 0, "mask_drop": 0, "gloves_drop": 0}}



# @app.post("/api/notification", response_model=schemas.FrameNotificationOut)
# def post_notification(n: schemas.FrameNotificationCreate, db: Session = Depends(get_db)):
#     return crud.create_frame_notification(db, n)

# @app.get("/api/notifications", response_model=List[schemas.FrameNotificationOut])
# def get_notifications(db: Session = Depends(get_db)):
#     return crud.get_all_notifications(db)

# @app.get("/api/latest-violation")
# def get_latest_violation(db: Session = Depends(get_db)):
#     latest = crud.get_latest_notification(db)
#     if not latest:
#         return {"message": None}

#     # Fetch camera name
#     camera = db.query(models.Camera).filter(models.Camera.id == latest.camera_id).first()
#     camera_name = camera.name if camera else "Unknown Camera"

#     return {
#         "message": f"📹 {camera_name} – ⚠️ Person {latest.person_id} is not wearing {latest.violation_type}",
#         "timestamp": str(latest.timestamp)
#     }

# @app.get("/api/violations/daily", response_model=schemas.ViolationDailyResponse)
# def get_violation_graph(db: Session = Depends(get_db)):
#     return crud.get_violation_daily(db)

# @app.get("/frame-notifications")
# def get_frame_notifications(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
#     # Query the most recent frame notification for each camera
#     notifications = crud.get_latest_frame_notifications(db, skip=skip, limit=limit)

#     # Format the data as per the frontend requirements
#     formatted_notifications = [
#         {
#             "id": notification.id,
#             "user_id": notification.user_id,
#             "camera_id": notification.camera_id,
#             "frame_index": notification.frame_index,
#             "person_id": notification.person_id,
#             "violation_type": notification.violation_type,
#             "message": notification.message,
#             "image_url": notification.image_url,
#             "timestamp": notification.timestamp.strftime("%Y-%m-%d %H:%M:%S")
#         }
#         for notification in notifications
#     ]

#     return formatted_notifications

# @app.post("/api/person", response_model=schemas.PersonPPEStatusOut)
# def create_person_status(person: schemas.PersonPPEStatusCreate, db: Session = Depends(get_db)):
#     return crud.create_person_ppe_status(db, person)

# @app.get("/add-camera")
# def show_camera_form(request: Request, db: Session = Depends(get_db)):
#     user_id = 1  # Replace with actual logged-in user
#     cameras = crud.get_user_cameras(db, user_id)
#     return templates.TemplateResponse("camera.html", {
#         "request": request,
#         "user_id": user_id,
#         "cameras": cameras
#     })

# model_det = YOLO("data/models/PPE_Model.pt")
# model_seg = YOLO("yolov8n-seg.pt")
# model_pose = YOLO("yolov8n-pose.pt")

# def get_video_capture(source):
#     cap = cv2.VideoCapture(source)
#     if not cap.isOpened():
#         raise HTTPException(status_code=500, detail="Failed to open video source")
#     return cap

# @app.get("/api/stream/detection")
# def stream_detection(source: str = "a.mp4"):
#     cap = get_video_capture(source)

#     def generate():
#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 break
#             frame = cv2.resize(frame, (480, 360))

#             results = model_det(frame)[0]
#             for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
#                 x1, y1, x2, y2 = map(int, box)
#                 label = model_det.names[int(cls)]
#                 color = (0, 0, 255) if "NO" in label else (0, 255, 0)
#                 cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
#                 cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)

#             _, jpeg = cv2.imencode('.jpg', frame)
#             yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n")

#         cap.release()

#     return StreamingResponse(generate(), media_type="multipart/x-mixed-replace; boundary=frame")
# @app.get("/api/stream/segpose")
# def stream_segpose(source: str = "a.mp4"):
#     cap = get_video_capture(source)

#     def generate():
#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             frame = cv2.resize(frame, (480, 360))

#             # --- Segmentation ---
#             seg_result = model_seg.predict(frame, task='segment')[0]
#             masks = seg_result.masks.data.cpu().numpy() if seg_result.masks is not None else []

#             overlay = np.zeros_like(frame)
#             for mask in masks:
#                 resized_mask = cv2.resize(mask.astype(np.uint8), (frame.shape[1], frame.shape[0]))
#                 overlay[resized_mask.astype(bool)] = (0, 255, 0)

#             frame = cv2.addWeighted(frame, 1, overlay, 0.5, 0)

#             # --- Pose Estimation ---
#             pose_result = model_pose.predict(frame, task='pose')[0]
#             frame = pose_result.plot()

#             try:
#                 _, jpeg = cv2.imencode('.jpg', frame)
#                 yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n")
#                 time.sleep(0.025)
#             except Exception as e:
#                 print("🔌 Client disconnected:", e)
#                 break

#         cap.release()

#     return StreamingResponse(generate(), media_type="multipart/x-mixed-replace; boundary=frame")



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
from datetime import datetime
import time
from fastapi import BackgroundTasks, FastAPI, Depends, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from typing import List
from decimal import Decimal
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from fastapi import Form
from ultralytics import YOLO
import models, crud, schemas
from database import SessionLocal, engine
from video_processor import  process_video
from fastapi import BackgroundTasks, FastAPI, Depends
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
from io import BytesIO
from starlette.concurrency import run_in_threadpool
import threading
from video_processor import process_video
from video_processor import start_all_camera_streams
models.Base.metadata.create_all(bind=engine)
from fastapi import Form
app = FastAPI(title="PPE Monitoring API")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_camera_threads():
    start_all_camera_streams()

@app.get("/")
def dashboard(request: Request, db: Session = Depends(get_db)):
    user_id = 1  # Replace with session/user logic
    if not crud.get_user_cameras(db, user_id):
        return RedirectResponse("/add-camera", status_code=303)

    counts = crud.get_latest_counts(db)
    summary = crud.get_ppe_summary(db)
    violations = crud.get_latest_violations()
    notifications = crud.get_all_notifications(db)
    alerts = crud.get_latest_ppe_alerts(db)

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "counts": counts,
        "summary": summary,
        "violations": violations,
        "notifications": notifications,
        "alerts": alerts,
        "violation_chart": {"labels": ["Mon", "Tue", "Wed"], "data": [5, 10, 3]},
        "now": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })



@app.get("/signup")
def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup")
def signup(name: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    crud.create_user(db, schemas.UserCreate(name=name, email=email, password=password))
    return RedirectResponse("/login", status_code=303)

@app.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email)
    if user and user.password == password:  # No hash for now
        response = RedirectResponse("/", status_code=303)
        # Store user info in session if using auth/session manager
        return response
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})


@app.get("/add-camera")
def show_camera_form(request: Request, db: Session = Depends(get_db)):
    user_id = 1  # Replace with session or cookie-based logic
    cameras = crud.get_user_cameras(db, user_id)
    return templates.TemplateResponse("camera.html", {
        "request": request,
        "user_id": user_id,
        "cameras": cameras
    })


# Background processing for video
def start_video_processing_in_background(cam_id: int, user_id: int, source: str):
    threading.Thread(target=process_video, args=(cam_id, user_id, source), daemon=True).start()

@app.post("/start-video")
def start_video_processing(cam_id: int, user_id: int, source: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(start_video_processing_in_background, cam_id, user_id, source)
    return {"message": "Video processing started in the background!"}

# Start processing in a thread
@app.post("/start-processing")
def start_video_processing(cam_id: int = Form(...), user_id: int = Form(...), source: str = Form(...)):
    threading.Thread(target=process_video_periodically, args=(cam_id, user_id, source), daemon=True).start()
    return {"message": "Video processing started in the background!"}

@app.post("/add-camera")
def submit_camera_form(
    user_id: int = Form(...),
    name: str = Form(...),
    source: str = Form(...),
    db: Session = Depends(get_db)
):
    camera = schemas.CameraCreate(user_id=user_id, name=name, source=source)
    crud.create_camera(db, camera)

    # ✅ Automatically start video processing for this camera
    from threading import Thread
    Thread(target=process_video, args=(source,), daemon=True).start()

    return {"message": "Camera added successfully"}

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

def periodic_task(background_tasks: BackgroundTasks, user_id: int, cam_id: int, source: str):
    # This function will execute the task every second
    while True:
        background_tasks.add_task(process_video, cam_id, user_id, source)
        time.sleep(1)  # Sleep for 1 second



# Function that processes video continuously in the background
def process_video_periodically(cam_id, user_id, source):
    while True:
        process_video(cam_id, user_id, source)  # Call the existing process_video function
        time.sleep(1)  # Process the video every second

# Endpoint to trigger video processing in a background thread
@app.post("/start-processing")
def start_video_processing(cam_id: int = Form(...), user_id: int = Form(...), source: str = Form(...)):
    # Start video processing in a separate thread
    threading.Thread(target=process_video_periodically, args=(cam_id, user_id, source), daemon=True).start()
    return {"message": "Video processing started in the background!"}

@app.post("/process")
def run_processing(background_tasks: BackgroundTasks, user_id: int = Form(...), cam_id: int = Form(...), source: str = Form(...)):
    # Start the periodic task in the background when the /process endpoint is called
    background_tasks.add_task(periodic_task, background_tasks, user_id, cam_id, source)
    return {"message": "Processing started in the background!"}


@app.post("/cameras/")
def create_camera(
    user_id: int = Form(...),
    name: str = Form(...),
    source: str = Form(...),
    db: Session = Depends(get_db)
):
    camera = schemas.CameraCreate(user_id=user_id, name=name, source=source)
    crud.create_camera(db, camera)
    return RedirectResponse(url="/add-camera", status_code=HTTP_303_SEE_OTHER)

@app.get("/users/{user_id}/cameras/", response_model=List[schemas.CameraOut])
def get_user_cameras(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_cameras(db, user_id)

@app.post("/api/frame", response_model=schemas.FrameSummaryCreate)
def create_frame(fs: schemas.FrameSummaryCreate, db: Session = Depends(get_db)):
    return crud.create_frame_summary(db, fs)

@app.get("/api/tracking/counts", response_model=schemas.CountResponse)
def get_counts(db: Session = Depends(get_db)):
    return crud.get_latest_counts(db)

@app.get("/api/ppe/summary", response_model=schemas.PPESummaryResponse)
def get_ppe_summary(db: Session = Depends(get_db)):
    return crud.get_ppe_summary(db)

@app.get("/api/ppe/totals")
def get_ppe_totals(db: Session = Depends(get_db)):
    return crud.get_ppe_totals(db)

# @app.post("/api/alerts")
# async def post_alert_summary(data: dict, db: Session = Depends(get_db)):
#     data["user_id"] = data.get("user_id", 1)
#     data["camera_id"] = data.get("camera_id", 1)
#     return crud.save_ppe_alert_summary(db, data)
@app.post("/api/alerts")
def save_alert(payload: schemas.AlertCreate, db: Session = Depends(get_db)):
    return crud.save_ppe_alert_summary(db, payload.dict())

@app.get("/api/alerts/latest")
def get_latest_alerts(db: Session = Depends(get_db)):
    # Fetch the latest PPE alert data
    alerts = crud.get_latest_ppe_alerts(db)

    # Check that data is returned from the database
    if alerts:
        return {"alerts": alerts}
    else:
        return {"alerts": {"hardhat_count": 0, "vest_count": 0, "mask_count": 0, "gloves_count": 0, 
                            "hardhat_drop": 0, "vest_drop": 0, "mask_drop": 0, "gloves_drop": 0}}



@app.post("/api/notification", response_model=schemas.FrameNotificationOut)
def post_notification(n: schemas.FrameNotificationCreate, db: Session = Depends(get_db)):
    return crud.create_frame_notification(db, n)

@app.get("/api/notifications", response_model=List[schemas.FrameNotificationOut])
def get_notifications(db: Session = Depends(get_db)):
    return crud.get_all_notifications(db)

@app.get("/api/latest-violation")
def get_latest_violation(db: Session = Depends(get_db)):
    latest = crud.get_latest_notification(db)
    if not latest:
        return {"message": None}

    # Fetch camera name
    camera = db.query(models.Camera).filter(models.Camera.id == latest.camera_id).first()
    camera_name = camera.name if camera else "Unknown Camera"

    return {
        "message": f"📹 {camera_name} – ⚠️ Person {latest.person_id} is not wearing {latest.violation_type}",
        "timestamp": str(latest.timestamp)
    }

@app.get("/api/violations/daily", response_model=schemas.ViolationDailyResponse)
def get_violation_graph(db: Session = Depends(get_db)):
    return crud.get_violation_daily(db)

@app.get("/frame-notifications")
def get_frame_notifications(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    # Query the most recent frame notification for each camera
    notifications = crud.get_latest_frame_notifications(db, skip=skip, limit=limit)

    # Format the data as per the frontend requirements
    formatted_notifications = [
        {
            "id": notification.id,
            "user_id": notification.user_id,
            "camera_id": notification.camera_id,
            "frame_index": notification.frame_index,
            "person_id": notification.person_id,
            "violation_type": notification.violation_type,
            "message": notification.message,
            "image_url": notification.image_url,
            "timestamp": notification.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
        for notification in notifications
    ]

    return formatted_notifications

@app.post("/api/person", response_model=schemas.PersonPPEStatusOut)
def create_person_status(person: schemas.PersonPPEStatusCreate, db: Session = Depends(get_db)):
    return crud.create_person_ppe_status(db, person)

@app.get("/add-camera")
def show_camera_form(request: Request, db: Session = Depends(get_db)):
    user_id = 1  # Replace with actual logged-in user
    cameras = crud.get_user_cameras(db, user_id)
    return templates.TemplateResponse("camera.html", {
        "request": request,
        "user_id": user_id,
        "cameras": cameras
    })

model_det = YOLO("data/models/PPE_Model.pt")
model_seg = YOLO("yolov8n-seg.pt")
model_pose = YOLO("yolov8n-pose.pt")
def get_camera_source(db: Session, camera_id: int) -> str:
    camera = db.query(models.Camera).filter(models.Camera.id == camera_id).first()
    if not camera:
        raise HTTPException(status_code=404, detail=f"Camera {camera_id} not found")
    return camera.source

def get_video_capture(source):
    # Convert "0" to int 0 for webcam
    if source.isdigit():
        source = int(source)
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise HTTPException(status_code=500, detail=f"Failed to open video source: {source}")
    return cap

@app.get("/api/stream/detection/{camera_id}")
def stream_detection(camera_id: int, db: Session = Depends(get_db)):
    source = get_camera_source(db, camera_id)
    cap = get_video_capture(source)

    def generate():
        frame_index = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            frame_index += 1
            if frame_index % 15 != 0:
                continue

            frame = cv2.resize(frame, (480, 360))
            results = model_det(frame)[0]

            for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
                x1, y1, x2, y2 = map(int, box)
                label = model_det.names[int(cls)]
                color = (0, 0, 255) if "NO" in label else (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)

            _, jpeg = cv2.imencode('.jpg', frame)
            yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n")

        cap.release()

    return StreamingResponse(generate(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/api/stream/segpose/{camera_id}")
def stream_segpose(camera_id: int, db: Session = Depends(get_db)):
    source = get_camera_source(db, camera_id)
    cap = get_video_capture(source)

    def generate():
        frame_index = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            frame_index += 1
            if frame_index % 15 != 0:
                continue

            frame = cv2.resize(frame, (480, 360))

            seg_result = model_seg.predict(frame, task='segment')[0]
            masks = seg_result.masks.data.cpu().numpy() if seg_result.masks is not None else []

            overlay = np.zeros_like(frame)
            for mask in masks:
                resized_mask = cv2.resize(mask.astype(np.uint8), (frame.shape[1], frame.shape[0]))
                overlay[resized_mask.astype(bool)] = (0, 255, 0)

            frame = cv2.addWeighted(frame, 1, overlay, 0.5, 0)

            pose_result = model_pose.predict(frame, task='pose')[0]
            frame = pose_result.plot()

            try:
                _, jpeg = cv2.imencode('.jpg', frame)
                yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n")
            except Exception as e:
                print("🔌 Client disconnected:", e)
                break

        cap.release()

    return StreamingResponse(generate(), media_type="multipart/x-mixed-replace; boundary=frame")


@app.get("/notification.html", response_class=HTMLResponse)
def notification_page(request: Request, db: Session = Depends(get_db)):
    notifications = crud.get_all_notifications(db)
    return templates.TemplateResponse("notification.html", {
        "request": request,
        "notifications": notifications
    })

@app.get("/notification", response_class=RedirectResponse)
def redirect_to_notification():
    return RedirectResponse(url="/notification.html")


@app.get("/streams", response_class=HTMLResponse)
def show_all_streams(request: Request, db: Session = Depends(get_db)):
    cameras = crud.get_all_cameras(db)  # You must define this function in crud.py
    return templates.TemplateResponse("streams.html", {"request": request, "cameras": cameras})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)