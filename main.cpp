#include <limits>
#include <ctime>
#include <iostream>

// Структура для підсумку завдань
struct TaskSummary {
    int completed;
    int not_completed;
};

extern "C" {
    // Функція для підрахунку виконаних та невиконаних завдань
    TaskSummary summarize_tasks(int tasks[], int size) {
        TaskSummary summary = {0, 0};
        for (int i = 0; i < size; ++i) {
            if (tasks[i] == 1) summary.completed++;
            else summary.not_completed++;
        }
        return summary;
    }

    // Функція для підрахунку кількості завдань із певним тегом
    int count_tasks_with_tag(int task_tags[], int size, int target_tag) {
        int count = 0;
        for (int i = 0; i < size; ++i) {
            if (task_tags[i] == target_tag) count++;
        }
        return count;
    }

    // Функція для розрахунку прогресу виконання (у відсотках)
    double calculate_progress(int tasks[], int size) {
        int completed = 0;
        for (int i = 0; i < size; ++i) {
            if (tasks[i] == 1) completed++;
        }
        if (size == 0) return 0.0; // Перевірка на нульовий розмір для уникнення ділення на нуль
        double progress = (static_cast<double>(completed) / size) * 1.0;
        return std::round(progress * 100.0) / 100.0; // Округлення до двох знаків після коми
    }
}