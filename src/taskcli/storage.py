import json , os
from pathlib import Path
from .model import Task,Recurring_task

DEFAULT_PATH = Path.home()/ '.taskcli' / 'task.json'
TYPES = {'task':Task , 'recurring':Recurring_task}

class TaskStore():
    def __init__(self,path=DEFAULT_PATH):
        self.path = Path(path)
        self.tasks = []

    def __enter__(self):
        self.path.parent.mkdir(parents=True , exist_ok=True)
        if self.path.exists():
            data = json.loads(self.path.read_text())
            self.tasks = [TYPES[d['type']].from_dict(d) for d in data]
        return self
    def __exit__(self,exc_type,exc,tb):
        if exc_type is None:
            self._save()
        return False
    def _save(self):
        tmp = self.path.with_suffix('.tmp')
        tmp.write_text(json.dumps([t.to_dict() for t in self.tasks],indent=2))
        os.replace(tmp,self.path)     # Atomic Swap

    def next_id(self):
        return max((t.id for t in self.tasks) , default=0)+1

    def get(self,task_id):
        for t in self.tasks:
            if t.id==task_id:
                return t
        raise KeyError (task_id)
    



        
