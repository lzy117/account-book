from typing import List
from data.models import Reminder
from data.database import LocalDatabase
from datetime import datetime

class ReminderService:
    """ (Req018) 待办提醒功能  """
    
    def __init__(self):
        self.db = LocalDatabase()

    def create_reminder(self, title: str, time: datetime):
        """ (Req019, Req020) [cite: 81, 85] """
        print(f"TODO: [ReminderService] 创建提醒: {title} at {time}")
        # TODO: 调用 self.db.saveData() 保存 Reminder
        pass

    def get_pending_reminders(self) -> List[Reminder]:
        print(f"TODO: [ReminderService] 获取所有未完成的提醒")
        # TODO: 调用 self.db.fetchData()
        return []

    def set_notification(self, reminder_id: str):
        """ (对应UML方法)  (Req020)  """
        print(f"TODO: [ReminderService] 为 {reminder_id} 设置系统通知")
        # TODO: 对接操作系统通知
        pass