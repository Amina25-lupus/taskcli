import argparse , logging , sys 
from .model import Task,Recurring_task
from .storage import  TaskStore ,DEFAULT_PATH
from .decorators import logged
from .dates import parse_due

@logged
def cmd_add(args):
    with TaskStore() as store:
        due=parse_due(args.due) if args.due else None
        if args.every:
            task=Recurring_task(store.next_id(),args.title ,due ,every_days=args.every)
        else:
            task=Task(store.next_id(),args.title,due)
        store.tasks.append(task)
        print('Added ',task)

@logged
def cmd_list(args):
    with TaskStore() as store:
        tasks = sorted(store.tasks)
        if not args.all:
            tasks = [t for t in tasks if not  t.done]
        if not tasks:
            print('Nothing to do')
            return 
        for t in tasks:
            print (t)

@logged
def cmd_done(args):
    with TaskStore() as store:
        try:
            task = store.get(args.id)
        except KeyError:
            sys.exit(f'No task with ID {args.id}')
        task.mark_done()
        print('Updated:',task)

@logged
def cmd_rm(args):
    with TaskStore() as store:
        store.tasks = [t for t in store.tasks if t.id!=args.id]
        print('Removed : ',{args.id})

def build_parser():
    p = argparse.ArgumentParser(prog='task',description='Simple task manager')
    sub = p.add_subparsers(dest='command',required=True)

    a = sub.add_parser('add',help='add a task')
    a.add_argument('title')
    a.add_argument('--due' , help='Today,Tomarrow,Friday,YYYY/MM/DD')
    a.add_argument('--every',type=int,help='Every N days')
    a.set_defaults(func=cmd_add)

    l = sub.add_parser('list',help='show task')
    l.add_argument('--all',action='store_true',help='include finished')
    l.set_defaults(func=cmd_list)

    d=sub.add_parser('done',help='Mark a task done')
    d.add_argument('id',type=int)
    d.set_defaults(func=cmd_done)

    r=sub.add_parser('rm',help='delete a task')
    r.add_argument('id',type=int)
    r.set_defaults(func=cmd_rm)
    return p

def main(argv=None):
    DEFAULT_PATH.parent.mkdir(parents=True,exist_ok=True)
    logging.basicConfig(filename=DEFAULT_PATH.parent / 'taskcli.log',
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')
    args = build_parser().parse_args(argv)
    try:
        args.func(args)
    except ValueError as e:
        sys.exit(f'Error : {e}')

