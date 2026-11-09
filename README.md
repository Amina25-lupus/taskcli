# TaskCLI

A simple command-line task manager built with Python.

TaskCLI lets you add, list, complete, and remove tasks. It also supports due dates and recurring tasks.

## Features

- Add tasks
- List saved tasks
- Mark tasks as completed
- Remove tasks
- Set task due dates
- Create recurring tasks
- Store tasks locally in a JSON file

## Requirements

- Python 3.9 or later

## Installation

For development, clone or download the project and run:

```bash
pip install -e .
```

## Usage

### Add a task

```bash
task add "Learn Python"
```

### Add a task with a due date

```bash
task add "Complete DSA practice" --due tomorrow
```

### Add a recurring task

```bash
task add "Exercise" --every 3 --due today
```

### List tasks

```bash
task list
```

### Complete a task

```bash
task done 1
```

### Remove a task

```bash
task rm 1
```

## Data Storage

Tasks are stored locally in:

```text
~/.taskcli/task.json
```

On Windows, this corresponds to a folder under your user home directory.

## Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest -v
```

## License

This project is currently distributed without a declared open-source license.