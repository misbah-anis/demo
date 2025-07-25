# # # from sqlalchemy import Column, Integer, String, DateTime, Float, Text
# # # from sqlalchemy.sql import func
# # # from database import Base

# # # class FrameSummary(Base):
# # #     __tablename__ = "frame_summaries"
# # #     id = Column(Integer, primary_key=True, index=True)
# # #     timestamp = Column(DateTime(timezone=True), server_default=func.now())
# # #     frame_index = Column(Integer)
# # #     wearing = Column(Integer)
# # #     not_wearing = Column(Integer)
# # #     persons = Column(Integer)
# # #     in_count = Column(Integer)
# # #     out_count = Column(Integer)
# # #     inference_ms = Column(Float)

# # # class ViolationDaily(Base):
# # #     __tablename__ = "violation_daily"
# # #     day = Column(String(3), primary_key=True)
# # #     count = Column(Integer, default=0)

# # # class FrameNotification(Base):
# # #     __tablename__ = "frame_notifications"
# # #     id = Column(Integer, primary_key=True, index=True)
# # #     timestamp = Column(DateTime(timezone=True), server_default=func.now())
# # #     frame_index = Column(Integer)
# # #     person_id = Column(Integer)
# # #     violation_type = Column(String(100))
# # #     message = Column(Text)
# # #     image_url = Column(String(255))  # ✅ added

# # from sqlalchemy import Column, Integer, String, DateTime, Float, Text
# # from sqlalchemy.sql import func
# # from database import Base

# # class FrameSummary(Base):
# #     __tablename__ = "frame_summaries"
# #     id = Column(Integer, primary_key=True, index=True)
# #     timestamp = Column(DateTime(timezone=True), server_default=func.now())
# #     frame_index = Column(Integer)
# #     wearing = Column(Integer)       # Total items worn
# #     not_wearing = Column(Integer)   # Total violations
# #     persons = Column(Integer)
# #     in_count = Column(Integer)
# #     out_count = Column(Integer)
# #     inference_ms = Column(Float)

# # class ViolationDaily(Base):
# #     __tablename__ = "violation_daily"
# #     day = Column(String(3), primary_key=True)
# #     count = Column(Integer, default=0)

# # class FrameNotification(Base):
# #     __tablename__ = "frame_notifications"
# #     id = Column(Integer, primary_key=True, index=True)
# #     timestamp = Column(DateTime(timezone=True), server_default=func.now())
# #     frame_index = Column(Integer)
# #     person_id = Column(Integer)
# #     violation_type = Column(String(100))  # e.g., "NO-Mask"
# #     message = Column(Text)
# #     image_url = Column(String(255))       # Frame or cropped violation image

# # class PersonPPEStatus(Base):
# #     __tablename__ = "person_ppe_status"
# #     id = Column(Integer, primary_key=True, index=True)
# #     frame_index = Column(Integer, index=True)
# #     person_id = Column(Integer)
    
# #     # Based on class labels
# #     person = Column(String(10))         # always "detected"
# #     gloves = Column(String(10))         # "wearing"/"missing"
# #     hardhat = Column(String(10))        # "wearing"/"missing"
# #     mask = Column(String(10))           # "wearing"/"missing"
# #     vest = Column(String(10))           # "wearing"/"missing"
    
# #     # Optionally extendable (e.g., boots, glasses, etc.)
# #     timestamp = Column(DateTime(timezone=True), server_default=func.now())

# from sqlalchemy import Column, Integer, String, DateTime, Float, Text
# from sqlalchemy.sql import func
# from database import Base

# class FrameSummary(Base):
#     __tablename__ = "frame_summaries"
#     id = Column(Integer, primary_key=True, index=True)
#     timestamp = Column(DateTime(timezone=True), server_default=func.now())
#     frame_index = Column(Integer)
#     wearing = Column(Integer)       # Total items worn
#     not_wearing = Column(Integer)   # Total violations
#     persons = Column(Integer)
#     in_count = Column(Integer)
#     out_count = Column(Integer)
#     inference_ms = Column(Float)

# class ViolationDaily(Base):
#     __tablename__ = "violation_daily"
#     day = Column(String(3), primary_key=True)
#     count = Column(Integer, default=0)

# class FrameNotification(Base):
#     __tablename__ = "frame_notifications"
#     id = Column(Integer, primary_key=True, index=True)
#     timestamp = Column(DateTime(timezone=True), server_default=func.now())
#     frame_index = Column(Integer)
#     person_id = Column(Integer)
#     violation_type = Column(String(100))  # e.g., "NO-Mask"
#     message = Column(Text)
#     image_url = Column(String(255))       # Frame or cropped violation image

# class PersonPPEStatus(Base):
#     __tablename__ = "person_ppe_status"
#     id = Column(Integer, primary_key=True, index=True)
#     frame_index = Column(Integer, index=True)
#     person_id = Column(Integer)
    
#     # PPE status
#     person = Column(String(10))         # always "detected"
#     gloves = Column(String(10))         # "wearing"/"missing"
#     hardhat = Column(String(10))        # "wearing"/"missing"
#     mask = Column(String(10))           # "wearing"/"missing"
#     vest = Column(String(10))           # "wearing"/"missing"
    
#     timestamp = Column(DateTime(timezone=True), server_default=func.now())
# class PPEAlert(Base):
#     __tablename__ = "ppe_alerts"
#     id = Column(Integer, primary_key=True, index=True)
#     timestamp = Column(DateTime(timezone=True), server_default=func.now())
#     hardhat_count = Column(Integer)
#     hardhat_drop = Column(Float)
#     vest_count = Column(Integer)
#     vest_drop = Column(Float)
#     mask_count = Column(Integer)
#     mask_drop = Column(Float)
#     gloves_count = Column(Integer)
#     gloves_drop = Column(Float)

# class PPEAlertSummary(Base):
#     __tablename__ = "ppe_alerts_summary"

#     id = Column(Integer, primary_key=True, index=True)
#     hardhat_count = Column(Integer)
#     hardhat_drop = Column(Float)
#     vest_count = Column(Integer)
#     vest_drop = Column(Float)
#     mask_count = Column(Integer)
#     mask_drop = Column(Float)
#     gloves_count = Column(Integer)
#     gloves_drop = Column(Float)
#     timestamp = Column(DateTime(timezone=True), server_default=func.now())

from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from sqlalchemy.sql import func
from database import Base

# ----------------- User & Camera -----------------

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))  # Should be hashed

class Camera(Base):
    __tablename__ = "cameras"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String(100))
    source = Column(String(255))  # RTSP/HTTP/MP4/Webcam


# ----------------- PPE Detection Tables -----------------



class FrameSummary(Base):
    __tablename__ = "frame_summaries"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    camera_id = Column(Integer)  # Reference to Camera
    violation_id = Column(Integer)  # Reference to Violation (Optional if you want direct relation)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    frame_index = Column(Integer)
    wearing = Column(Integer)
    not_wearing = Column(Integer)
    persons = Column(Integer)
    in_count = Column(Integer)
    out_count = Column(Integer)
    inference_ms = Column(Float)

class ViolationDaily(Base):
    __tablename__ = "violation_daily"
    day = Column(String(3), primary_key=True)
    count = Column(Integer, default=0)
    user_id = Column(Integer)
    camera_id = Column(Integer)  # Reference to Camera
    violation_id = Column(Integer)  # Optional reference to Violation


class FrameNotification(Base):
    __tablename__ = "frame_notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    camera_id = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    frame_index = Column(Integer)
    person_id = Column(Integer)
    violation_type = Column(String(100))
    message = Column(Text)
    image_url = Column(String(255))

class PersonPPEStatus(Base):
    __tablename__ = "person_ppe_status"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    camera_id = Column(Integer)
    frame_index = Column(Integer, index=True)
    person_id = Column(Integer)
    person = Column(String(10))
    gloves = Column(String(10))
    hardhat = Column(String(10))
    mask = Column(String(10))
    vest = Column(String(10))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class PPEAlert(Base):
    __tablename__ = "ppe_alerts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    camera_id = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    hardhat_count = Column(Integer)
    hardhat_drop = Column(Float)
    vest_count = Column(Integer)
    vest_drop = Column(Float)
    mask_count = Column(Integer)
    mask_drop = Column(Float)
    gloves_count = Column(Integer)
    gloves_drop = Column(Float)

class PPEAlertSummary(Base):
    __tablename__ = "ppe_alerts_summary"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    camera_id = Column(Integer)
    hardhat_count = Column(Integer)
    hardhat_drop = Column(Float)
    vest_count = Column(Integer)
    vest_drop = Column(Float)
    mask_count = Column(Integer)
    mask_drop = Column(Float)
    gloves_count = Column(Integer)
    gloves_drop = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
