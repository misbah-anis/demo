# # from datetime import datetime
# # from pydantic import BaseModel, RootModel
# # from typing import Dict, List
# # from pydantic import BaseModel, ConfigDict
# # from pydantic import BaseModel
# # from datetime import datetime

# # class FrameSummaryCreate(BaseModel):
# #     frame_index: int
# #     wearing: int
# #     not_wearing: int
# #     persons: int
# #     in_count: int
# #     out_count: int
# #     inference_ms: float

# # class CountResponse(BaseModel):
# #     in_: int
# #     out: int
# #     total_inside: int

# # class PPESummaryResponse(BaseModel):
# #     total_detections: int
# #     wearing: int
# #     not_wearing: int
# #     compliance_rate: str

# # class LatestViolation(BaseModel):
# #     image_url: str
# #     gate: str
# #     issues: List[str]

# # class ViolationDailyResponse(RootModel[Dict[str, int]]):
# #     pass

# # class FrameNotificationCreate(BaseModel):
# #     frame_index: int
# #     person_id: int
# #     violation_type: str
# #     message: str
# #     image_url: str  # ✅ required



# # class FrameNotificationOut(BaseModel):
# #     frame_index: int
# #     person_id: int
# #     violation_type: str
# #     message: str
# #     timestamp: str  # changed from datetime to str

# #     class Config:
# #         from_attributes = True

# # class PersonPPEStatusCreate(BaseModel):
# #     frame_index: int
# #     person_id: int
# #     person: str
# #     gloves: str
# #     hardhat: str
# #     mask: str
# #     vest: str

# # class PersonPPEStatusOut(PersonPPEStatusCreate):
# #     timestamp: datetime


# from datetime import datetime
# from pydantic import BaseModel, RootModel
# from typing import Dict, List

# # ---------- Frame Summary ----------

# class FrameSummaryCreate(BaseModel):
#     frame_index: int
#     wearing: int
#     not_wearing: int
#     persons: int
#     in_count: int
#     out_count: int
#     inference_ms: float

# class CountResponse(BaseModel):
#     in_: int
#     out: int
#     total_inside: int

# # ---------- PPE Summary ----------

# class PPESummaryResponse(BaseModel):
#     hardhat: int
#     mask: int
#     gloves: int
#     vest: int
#     wearing: int
#     not_wearing: int
#     compliance_rate: str

# # ---------- Violation Chart ----------

# class ViolationDailyResponse(RootModel[Dict[str, int]]):
#     pass

# # ---------- Latest Violations ----------

# class LatestViolation(BaseModel):
#     image_url: str
#     gate: str
#     issues: List[str]

# # ---------- Frame Notifications ----------

# class FrameNotificationCreate(BaseModel):
#     frame_index: int
#     person_id: int
#     violation_type: str
#     message: str
#     image_url: str

# class FrameNotificationOut(BaseModel):
#     frame_index: int
#     person_id: int
#     violation_type: str
#     message: str
#     timestamp: str

#     class Config:
#         from_attributes = True


# class AlertCreate(BaseModel):
#     hardhat_count: int
#     hardhat_drop: float
#     vest_count: int
#     vest_drop: float
#     mask_count: int
#     mask_drop: float
#     gloves_count: int
#     gloves_drop: float


# # ---------- Person PPE Status ----------

# class PersonPPEStatusCreate(BaseModel):
#     frame_index: int
#     person_id: int
#     person: str
#     gloves: str
#     hardhat: str
#     mask: str
#     vest: str

# class PersonPPEStatusOut(PersonPPEStatusCreate):
#     timestamp: datetime

# # ---------- PPE Alert Summary ----------

# class PPEAlertItem(BaseModel):
#     count: int
#     drop: float

# class PPEAlertSummaryResponse(BaseModel):
#     hardhat: PPEAlertItem
#     vest: PPEAlertItem
#     mask: PPEAlertItem
#     gloves: PPEAlertItem
from pydantic import BaseModel, RootModel
from typing import List, Dict
from datetime import datetime


# ----------------- User & Camera -----------------

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class CameraCreate(BaseModel):
    user_id: int
    name: str
    source: str

class CameraOut(BaseModel):
    id: int
    user_id: int
    name: str
    source: str

    class Config:
        orm_mode = True


# ----------------- Frame Summary -----------------

class FrameSummaryCreate(BaseModel):
    user_id: int
    camera_id: int
    frame_index: int
    wearing: int
    not_wearing: int
    persons: int
    in_count: int
    out_count: int
    inference_ms: float


class CountResponse(BaseModel):
    in_: int
    out: int
    total_inside: int


# ----------------- PPE Summary -----------------

class PPESummaryResponse(BaseModel):
    hardhat: int
    mask: int
    gloves: int
    vest: int
    wearing: int
    not_wearing: int
    compliance_rate: str

# ----------------- Violation Chart -----------------

class ViolationDailyResponse(RootModel[Dict[str, int]]):
    pass


# ----------------- Latest Violations -----------------

class LatestViolation(BaseModel):
    image_url: str
    gate: str
    issues: List[str]


# ----------------- Frame Notifications -----------------

class FrameNotificationCreate(BaseModel):
    user_id: int
    camera_id: int
    frame_index: int
    person_id: int
    violation_type: str
    message: str
    image_url: str


class FrameNotificationOut(BaseModel):
    frame_index: int
    person_id: int
    violation_type: str
    message: str
    timestamp: str

    class Config:
        from_attributes = True


# ----------------- PPE Alerts -----------------

class AlertCreate(BaseModel):
    user_id: int
    camera_id: int
    hardhat_count: int
    hardhat_drop: float
    vest_count: int
    vest_drop: float
    mask_count: int
    mask_drop: float
    gloves_count: int
    gloves_drop: float


class PPEAlertItem(BaseModel):
    count: int
    drop: float


class PPEAlertSummaryResponse(BaseModel):
    hardhat: PPEAlertItem
    vest: PPEAlertItem
    mask: PPEAlertItem
    gloves: PPEAlertItem


# ----------------- Person PPE Status -----------------

class PersonPPEStatusCreate(BaseModel):
    user_id: int
    camera_id: int
    frame_index: int
    person_id: int
    person: str
    gloves: str
    hardhat: str
    mask: str
    vest: str


class PersonPPEStatusOut(PersonPPEStatusCreate):
    timestamp: datetime
