import pytest
from taskcli.model import Task
from taskcli.storage import TaskStore

def test_saves_on_success(tmp_path):
    path = tmp_path / "t.json"
    with TaskStore(path) as s:
        s.tasks.append(Task(1, "a"))
    with TaskStore(path) as s:
        assert len(s.tasks) == 1

def test_does_not_save_on_error(tmp_path):
    path = tmp_path / "t.json"
    with pytest.raises(RuntimeError):
        with TaskStore(path) as s:
            s.tasks.append(Task(1, "a"))
            raise RuntimeError
    assert not path.exists()