import ctypes
from pathlib import Path

# Завантаження бібліотеки
LIB_PATH = Path(__file__).resolve().parent / "libtask_status.so"
task_lib = ctypes.CDLL(str(LIB_PATH))


# Структура TaskSummary
class TaskSummary(ctypes.Structure):
    _fields_ = [("completed", ctypes.c_int), ("not_completed", ctypes.c_int)]


# Налаштування функцій
task_lib.summarize_tasks.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
task_lib.summarize_tasks.restype = TaskSummary

task_lib.count_tasks_with_tag.argtypes = (
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
    ctypes.c_int,
)
task_lib.count_tasks_with_tag.restype = ctypes.c_int


task_lib.calculate_progress.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
task_lib.calculate_progress.restype = ctypes.c_double


# Функції-обгортки
def get_task_summary(statuses):
    size = len(statuses)
    arr_type = ctypes.c_int * size
    result = task_lib.summarize_tasks(arr_type(*statuses), size)
    return {"completed": result.completed, "not_completed": result.not_completed}


def count_tasks_with_tag(tags, target_tag):
    size = len(tags)
    arr_type = ctypes.c_int * size
    return task_lib.count_tasks_with_tag(arr_type(*tags), size, target_tag)


def calculate_progress(statuses):
    size = len(statuses)
    arr_type = ctypes.c_int * size
    return task_lib.calculate_progress(arr_type(*statuses), size)
