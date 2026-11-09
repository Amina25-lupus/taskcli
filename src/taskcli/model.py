from datetime import date , timedelta

class Task():
    def __init__(self,id,title,due=None,done=False):
        self.id = id
        self.title = title
        self.due = due
        self.done = done

    def mark_done(self):
        self.done=True

    def to_dict(self):
        return {'type':'task','id':self.id,'title':self.title,
                'due':self.due.isoformat() if self.due else None,
                'done':self.done}

    @classmethod
    def from_dict(cls,d):
        due = date.fromisoformat(d['due']) if d.get('due') else None
        return cls(id=d['id'], title=d['title'],due=due,done=d['done'])

    def __str__(self):
        box = '[X]' if self.done else '[ ]'
        due = f' (due {self.due} )' if self.due else ''
        return f'{self.id} . {box} {self.title} {due} '

    def __repr__(self):
        return f'Task ({self.id!r} , {self.title!r})'

    def __lt__(self,other):
        return (self.due or date.max) < (other.due or date.max)

    # Recurring task 

class Recurring_task(Task):
    def __init__(self ,*args,every_days=7,**kwargs):
        super().__init__(*args,**kwargs)
        self.every_days = every_days

    def mark_done(self):
        base = self.due or date.today()
        self.due = base + timedelta(days=self.every_days)

    def to_dict(self):
        d = super().to_dict()
        d.update(type = 'recurring',every_days=self.every_days)
        return d

    @classmethod
    def from_dict(cls,d):
        due = date.fromisoformat(d['due']) if d.get('due') else None

        return cls(
            id=d['id'],
            title=d['title'],
            due=due,
            done=d['done'],
            every_days=d.get('every_days', 7)
        )

    def __str__(self):
        return super().__str__() + f' every {self.every_days} days '