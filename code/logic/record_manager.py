from typing import List, Dict, Any
from data.models import Record
from data.database import LocalDatabase

class RecordManager:
    """ 对应UML中的RecordManager类  """
    
    def __init__(self):
        self.db = LocalDatabase() # 依赖LocalDatabase 

    def createRecord(self, data: Dict) -> Record:
        """
        创建一条新记录 (对应UML方法) 
        (Req001, Req002, Req003, Req004) [cite: 14, 17, 20, 22]
        """
        print(f"TODO: [RecordManager] 正在创建记录...")
        # TODO: 1. 数据校验
        # TODO: 2. 调用 self.db.saveData(data) 
        # TODO: 3. (如果有关联图片) 保存图片到文件系统 (FS) [cite: 1, 22]
        
        # 返回一个模拟的Record对象
        new_id = self.db.saveData(data)
        return Record(
            record_id=new_id,
            type=data.get("type"),
            amount=data.get("amount"),
            date=data.get("date"),
            note=data.get("note")
        )

    def deleteRecord(self, record_id: str) -> bool:
        """
        删除一条记录 (对应UML方法) 
        (Req007) [cite: 35]
        """
        print(f"TODO: [RecordManager] 正在删除记录 {record_id}")
        # TODO: 1. (如果有关联图片) 从文件系统删除图片
        # TODO: 2. 调用 self.db.deleteData(record_id) 
        return self.db.deleteData(record_id)

    def getRecords(self, filter: Dict) -> List[Record]:
        """
        获取记录列表 (对应UML方法) 
        (Req009, Req010, Req012, Req013, Req014) [cite: 42, 45, 54, 57, 59]
        """
        print(f"TODO: [RecordManager] 正在根据 {filter} 获取记录")
        # TODO: 调用 self.db.fetchData(filter) 
        # 模拟返回数据
        raw_data = self.db.fetchData(filter)
        records = [Record(record_id=r['id'], type=r['type'], amount=r['amount'], date=r['date'], note=r['note']) for r in raw_data]
        return records

    def addTagToRecord(self, record_id: str, tag_name: str):
        """ (Req003) [cite: 20] """
        print(f"TODO: 为 {record_id} 添加标签 {tag_name}")
        pass

    def addPhotoToRecord(self, record_id: str, photo_path: str):
        """ (Req004) [cite: 22] """
        print(f"TODO: 为 {record_id} 添加图片 {photo_path}")
        pass