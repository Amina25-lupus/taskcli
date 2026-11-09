from datetime import date
from taskcli.model import Task, Recurring_task
from taskcli.dates import parse_due
import pytest

def test_sort_puts_no_due_last():
    a = Task(1, "a", due=date(2026, 1, 1))
    b = Task(2, "b")
    assert sorted([b, a]) == [a, b]

def test_recurring_done_reschedules():
    t = Recurring_task(1, "gym", due=date(2026, 1, 1), every_days=7)
    t.mark_done()
    assert t.due == date(2026, 1, 8)
    assert not t.done

def test_roundtrip():
    t = Recurring_task(1, "x", due=date(2026, 1, 1), every_days=3)
    t2 = Recurring_task.from_dict(t.to_dict())
    assert (t2.every_days, t2.due) == (3, t.due)

def test_bad_date():
    with pytest.raises(ValueError):
        parse_due("blah")