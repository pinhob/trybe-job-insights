from src.sorting import sort_by

from mock_jobs import (
    jobs,
    jobs_filtered_by_max_salary,
    jobs_filtered_by_min_salary,
    jobs_filtered_by_date_posted,
)


def test_sort_by_criteria():
    sort_by(jobs, "max_salary")
    assert jobs == jobs_filtered_by_max_salary

    sort_by(jobs, "min_salary")
    assert jobs == jobs_filtered_by_min_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_filtered_by_date_posted
